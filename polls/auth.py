from  polls.globals import secretHash
from hashlib import sha256
from random import randint
# [5 digits][sha256 hash of that number]
def authenticate(rollNo, password, token):
    return False
    pass
def valToken(token):
    tokenID = token[:6]
    if sha256((str(tokenID)+secretHash).encode('utf-8')).hexdigest() != token[6:] or isUsed(token):
        return False
    return True
def markTokenUsed(token):
    tokenID = token[:6]
    if not valToken(token):
        return False
    #mark as used on DB
    return True

def isUsed(token):
    tokenID = token[:6]
    if not valToken(token):
        return False
    # check as used in DB
    return True

def genToken(token):
    # fetch random 5 digit unused number
    tokenID = randint(10000,99999)
    return str(tokenID)+sha256((str(tokenID)+secretHash).encode('utf-8')).hexdigest()