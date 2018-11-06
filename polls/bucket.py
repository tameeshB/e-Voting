from polls.models import Bucket,Candidate,Positions

def process(rollNo, hostel, gender):
    print(rollNo, hostel, gender)
    course = {
        '0':'B',
        '1':'M',
        '2':'P',
    }[rollNo[2]]
    year = rollNo[:2] if course == 'B' else '0'
    matchingBuckets = Bucket.objects.filter(gender=gender,year=year,course=course,hostel=hostel)
    if len(matchingBuckets)==1:
        return {'status':True,'data':matchingBuckets[0].id}
    else:
        return {'status':False,'data':'No buckets found.'}

# Pass bucketID=None for obtaining all positions
def fetchPositions(bucketID):
    # 'positions' : [
    #     {
    #         'posName':'VP',
    #         'posID' : 'vp',
    #         'candidates':[
    #             {'voterID':'1601CS20','name':'Parth Kulkarni','agendaURL':'https://facebook.com'},
    #             {'voterID':'1601CS21','name':'Manish Kumar','agendaURL':'https://facebook.com'},
    #             {'voterID':'1601CS22','name':'Mayank Vaidya','agendaURL':'https://facebook.com'}
    #         ]
    #     },
    #     {
    #         'posName':'TechSec',
    #         'posID' : 'techsec',
    #         'candidates':[
    #             {'voterID':'1601CS20','name':'Parth Kulkarni','agendaURL':'https://facebook.com'},
    #             {'voterID':'1601CS21','name':'Manish Kumar','agendaURL':'https://facebook.com'},
    #             {'voterID':'1601CS22','name':'Mayank Vaidya','agendaURL':'https://facebook.com'}
    #         ]
    #     }
    # ]
    if bucketID is None:
        positions = Positions.objects.values()
    else:
        positions = Positions.objects.filter(buckets__id=bucketID).values()
    positionList = []
    for i,position in enumerate(positions):
        posDict = position.copy()
        posDict['candidates'] = list(Candidate.objects.filter(position__posID=position['posID']).values())
        positionList.append(posDict)
    
    return positionList
