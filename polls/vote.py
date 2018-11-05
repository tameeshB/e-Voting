from polls.models import Votes1, Voters, TokenID
from hashlib import sha256
from polls.globals import secretHash


def storeVote(request):
	# result = {'status': False, 'data': 'Error! Vote not recorded!'}
	# result = {'status': True, 'data': 'ivoted<3'}
	# print(request.POST)
	try:
		token = request.session['token']
		voterID = request.session['rollno']
		tokenID = token[:5]

		voteJSON = str(request.POST)
		# Add vote to database
		v = Votes1(tokenID=tokenID)
		v.voteJSON = voteJSON
		v.save()

		# Mark token as used, mark user as voted
		markTokenUsed(tokenID)
		markVoted(voterID.lower())

		signature = genSignature(tokenID, voteJSON)
		result = {'status': True, 'data': signature}
	except TokenID.DoesNotExist as e:
		result = {'status': False, 'data': 'Invalid Token! Vote not recorded!'}

	return result


def markTokenUsed(tokenID):
	t = TokenID.objects.get(tokenID=tokenID)
	t.used = True
	t.save()


def markVoted(voterID):
	voter = Voters(voterID=voterID, hasVoted=True)
	voter.save()


def genSignature(tokenID, voteJSON):
	return sha256((str(tokenID)+secretHash+voteJSON).encode('utf-8')).hexdigest()
