from polls.globals import secretHash
from hashlib import sha256
from random import randint
from .models import TokenID

# [5 digits][sha256 hash of that number]
def authenticate(rollNo, password, token):

    if not valToken(token):
        return 'Invalid Token!'

    tokenID = token[:5]
    if TokenID.objects.get(tokenID=tokenID).used:
        return 'Token already used!'

    return True


# Checks valid format if present in table
def valToken(token):
    tokenID = token[:5]
    if sha256(( str(tokenID)+secretHash).encode('utf-8')).hexdigest()[:5] != token[5:]:
        return False
    # not present
    if len(TokenID.objects.filter(tokenID=tokenID)) == 0:
        return False
    
    return True

def markTokenUsed(token):
    tokenID = token[:6]
    if not valToken(token):
        return False
    #mark as used on DB
    return True

# def isUsed(token):

#     tokenID = token[:5]
#     if not valToken(token):
#         return False
#     # check as used in DB
#     return True

def genToken():
    # fetch random 5 digit unused number
    while True:
        tokenID = randint(10000,99999)
        if len(TokenID.objects.filter(tokenID=tokenID)) == 0:
            break
    t = TokenID(tokenID=tokenID)
    t.save()
    return str(tokenID)+sha256((str(tokenID)+secretHash).encode('utf-8')).hexdigest()[:5]
