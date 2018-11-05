from django.db import models
from polls.globals import globals
# Create your models here.
class Voters(models.Model):
    voterID = models.CharField(max_length=200,primary_key=True) # is roll No.
    hasVoted = models.BooleanField(default=False)
    #TODO: add bucket
    def __str__(self):
        return self.voterID
    def __rep__(self):
        return self.voterID


class Bucket(models.Model):
    bucketName = models.CharField(max_length=200,null=False)
    # rollnoRegex = models.CharField(max_length=200,null=False)
    gender = models.CharField(max_length=1, choices=globals['gender'])
    hostel = models.CharField(max_length=3, choices=globals['hostels'])
    year = models.IntegerField(choices=globals['year'])
    course = models.CharField(max_length=1, choices=globals['course'])

    def __str__(self):
        return self.bucketName


class Positions(models.Model):
    # @todo: posID - auto generate
    posID = models.CharField(max_length=200,primary_key=True) # concat normalised string unique for position
    buckets = models.ManyToManyField(Bucket)
    posName = models.CharField(max_length=200)
    def __str__(self):
        return self.posID
    class Meta:
        verbose_name_plural = "Positions"


class Candidate(models.Model):
    votes = models.IntegerField(default=0) # 0 votes initially
    name = models.CharField(max_length=200,null=False,default="")
    agendaURL = models.CharField(max_length=1000,null=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE) # candidate is also a voter. 
    def __str__(self):
        return self.name


class Votes1(models.Model):
    tokenID = models.CharField(max_length=5,primary_key=True)
    voteJSON = models.CharField(max_length=1000)
    signature = models.CharField(max_length=100)


# class votes2(models.Model):
#     batch = models.CharField(max_length=15) # batch
#     voteJSON = models.CharField(max_length=1000)


class TokenID(models.Model):
    tokenID = models.CharField(max_length=5,primary_key=True)
    used = models.BooleanField(default=False)


class TokenNo(models.Model):
    tokenNo = models.IntegerField(default=0)
    def save(self):
        from polls.auth import genToken
        if self.pk is not None:
            orig = TokenNo.objects.get(pk=self.pk)
        for i in range(self.tokenNo):
            genToken() # @todo: optimise
        super(TokenNo, self).save()
        TokenNo.objects.all().delete()

class TokenDash(TokenNo):
    pass
    class Meta:
        proxy = True
        verbose_name = 'Token Dashboard'
        verbose_name_plural = 'Token Dashboard'
