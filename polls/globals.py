secretHash = ''
clientKey = 'a'
globals = {
    'electionName' : 'Gymkhana Elections 2018',
    'hasBegun' : True,
    'hostels' : (('BH1', 'Boys-Hostel1'), ('GH1', 'Girls-Hostel1')),
    'gender' : (('F', 'Female'), ('M', 'Male')),
    'year' : ((0, 'All'),(15, '15'), (16, '16'), (17, '17'), (18, '18')),
    'course' : (('B', 'BTech'), ('M', 'MTech'), ('P', 'Phd')),
    'user' : False, # remove
    'messages' : [],
    'positions' : []
    'smtp':{
        'host':'mail.iitp.ac.in',
        'port': 587,
        'sender' : 'email@iitp.ac.in',
        'pass' : ' '
    }
}
setDuringInit = ['hostels','gender']