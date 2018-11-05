from django.db import models

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
    gender = models.CharField(max_length=1, choices=(('F', 'Female'), ('M', 'Male')))
    hostel = models.CharField(max_length=3, choices=(('BH1', 'Boys-Hostel1'), ('GH1', 'Girls-Hostel1')))
    year = models.IntegerField(choices=((0, 'All'),(15, '15'), (16, '16'), (17, '17'), (18, '18')))
    course = models.CharField(max_length=1, choices=(('B', 'BTech'), ('M', 'MTech'), ('P', 'Phd')))

    def __str__(self):
        return self.bucketName


class Positions(models.Model):
    posID = models.CharField(max_length=200,primary_key=True) # concat noormalised string unique for position
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


class votes1(models.Model):
    batch = models.CharField(max_length=15) # batch
    voteJSON = models.CharField(max_length=1000)


class votes2(models.Model):
    batch = models.CharField(max_length=15) # batch
    voteJSON = models.CharField(max_length=1000)


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
            genToken() #optimise
        super(TokenNo, self).save()
        TokenNo.objects.all().delete()

class TokenDash(TokenNo):
    class Meta:
        proxy = True
        verbose_name = 'Token Dashboard'
        verbose_name_plural = 'Token Dashboard'
