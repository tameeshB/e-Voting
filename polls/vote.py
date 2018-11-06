import os
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

		voteJSON = str(request.POST)
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


def tallyVotes():
	from polls.models import Positions, Candidate

	pass