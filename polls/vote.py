import os
from polls.models import Votes1, Voters, TokenID, Positions, Candidate
from hashlib import sha256

from django.shortcuts import render
from django.template.loader import render_to_string

import evoting.settings

from polls.models import Votes1, Voters, TokenID
from polls.globals import secretHash,emailTemplates,globals
from polls.util import sendMail

def storeVote(request):
	# result = {'status': False, 'data': 'Error! Vote not recorded!'}
	# result = {'status': True, 'data': 'ivoted<3'}
	# print(request.POST)
	try:
		token = request.session['token']
		voterID = request.session['rollno'].lower()
		
		if hasVoted(voterID):
			return {'status': False, 'data': 'User {} has already voted!'.format(voterID)}

		tokenID = token[:5]

		voteJSON = str(request.POST.dict())
		signature = genSignature(tokenID, voteJSON)
		
		# Add vote to database
		v = Votes1(tokenID=tokenID)
		v.voteJSON = voteJSON
		v.signature = signature
		v.save()

		# Mark token as used, mark user as voted
		markTokenUsed(tokenID)
		markVoted(voterID)
		htmlData = ""
		templateData = globals.copy()
		templateData.update({ 'hash' : signature })
		htmlData = render_to_string('email/verifyToken.html', templateData) 
		
		sendMail(
			request.session['webmail'] or '' ,
			"Thank you for voting.",
			emailTemplates['voteSignature'].format(globals['baseURL'],signature),
			htmlData
		)
		return {'status': True, 'data': signature}

	except TokenID.DoesNotExist as e:
		return {'status': False, 'data': 'Invalid Token! Vote not recorded!'}


def hasVoted(voterID):
	return len(Voters.objects.filter(voterID=voterID)) > 0


def markTokenUsed(tokenID):
	t = TokenID.objects.get(tokenID=tokenID)
	t.used = True
	t.save()


def markVoted(voterID):
	voter = Voters(voterID=voterID, hasVoted=True)
	voter.save()


def genSignature(tokenID, voteJSON):
	return sha256((str(tokenID)+secretHash+voteJSON).encode('utf-8')).hexdigest()


def verifyVote(tokenID):
	vote = Votes1.objects.get(tokenID=tokenID)
	return genSignature(vote.tokenID, vote.voteJSON) == vote.signature


# Re hashes all votes and compares the
#  signatures against those stored in the table
def verifyAllVotes():
	for vote in Votes1.objects.values_list('tokenID', 'voteJSON', 'signature'):
		if genSignature(vote[0], vote[1]) != vote[2]:
			return False
	return True


def tallyAllVotes(verify_votes=False, commit_tally=False):
	result = {'status': False, 'data': None}
	if verify_votes:
		if not verifyAllVotes():
			result['data'] = 'Vote Verification Failed!'
			return result

	from polls.bucket import fetchPositions
	from ast import literal_eval

	positionsList = fetchPositions(bucketID=None)

	# tallyDict : {posID: {candID: voteCount}}
	tallyDict = {}
	for pos in positionsList:
		candDict = {}
		for cand in pos['candidates']:
			candDict[cand['id']] = 0
		tallyDict[pos['posID']] = candDict

	for vote in Votes1.objects.values('voteJSON'):
		try:
			vote_dict = literal_eval(vote['voteJSON'])
		except SyntaxError:
			# Invalid vote json
			result['data'] = 'Invalid vote encountered!'
			return result

		for posID, candID in vote_dict.items():
			if posID == 'csrfmiddlewaretoken':
				continue
			tallyDict[posID][int(candID)] += 1

	if commit_tally:
		commit_result = commitTally(tallyDict)
		if not commit_result:
			result['data'] = 'Vote counts could not be committed!'
			return result

	result['status'] = True
	result['data'] = tallyDict

	return result


def commitTally(tallyDict):
	candidate_list = []
	try:
		for posID, candDict in tallyDict.items():
			for candID, voteCount in candDict.items():
				candidate = Positions.objects.get(posID=posID).candidate_set.get(id=candID)
				candidate.votes = voteCount
				candidate_list.append(candidate)
	except (Positions.DoesNotExist, Candidate.DoesNotExist):
		return False

	for candidate in candidate_list:
		candidate.save()

	return True

# Reset all candidate vote counts to 0
def resetVoteCounts():
	Candidate.objects.update(votes=0)
	return True
