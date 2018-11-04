from django.db import models

# Create your models here.
class Voters(models.Model):
    voterID = models.CharField(max_length=200,primary_key=True) # is roll No.
    name = models.CharField(max_length=200)
    hasVoted = models.BooleanField(default=False)
    dateTime = models.DateTimeField('date voted',null=True)
    batch = models.IntegerField(default=0) # first 4 digits of rollNo.
    hostel = models.CharField(max_length=4)
    def __str__(self):
        return self.voterID
    def __rep__(self):
        return self.voterID


class Positions(models.Model):
    posID = models.CharField(max_length=200,primary_key=True) # concat noormalised string unique for position
    canVoteFor = models.CharField(max_length=100) # regex string for which batches can vote for this position.
    posName = models.CharField(max_length=200)
    batch = models.IntegerField(default=0) # first 4 digits of rollNo.
    def __str__(self):
        return self.posID


class Candidate(models.Model):
    voterID = models.ForeignKey(Voters, on_delete=models.CASCADE) # candidate is also a voter. 
    votes = models.IntegerField(default=0) # 0 votes initially
    agendaURL = models.CharField(max_length=1000,null=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE) # candidate is also a voter. 


class votes1(models.Model):
    batch = models.CharField(max_length=15) # batch
    voteJSON = models.CharField(max_length=1000)


class votes2(models.Model):
    batch = models.CharField(max_length=15) # batch
    voteJSON = models.CharField(max_length=1000)


class TokenID(models.Model):
    tokenID = models.CharField(max_length=5,primary_key=True)
    used = models.BooleanField(default=False)
