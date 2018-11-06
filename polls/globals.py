secretHash = ''
clientKey = 'a'
globals = {
    'electionName' : 'Gymkhana Elections 2018',
    'baseURL' : 'https://evoting18.herokuapp.com',
    'hasBegun' : True,
    'hostels' : (('BH1', 'Boys-Hostel1'), ('GH1', 'Girls-Hostel1')),
    'gender' : (('F', 'Female'), ('M', 'Male')),
    'year' : ((0, 'All'),(15, '15'), (16, '16'), (17, '17'), (18, '18')),
    'course' : (('B', 'BTech'), ('M', 'MTech'), ('P', 'Phd')),
    'user' : False, # remove
    'messages' : [],
    'positions' : [],
    'smtp':{
        'host':'mail.iitp.ac.in',
        'port': 587,
        'sender' : 'email@iitp.ac.in',
        'pass' : ' '
    }
}
emailTemplates = {
    'voteSignature' : """
        Hi!
        Thank you for voting!
        This email is an acknowledgement of your ballot.
        You can verify your vote at any time by going to {}/verify and entering the 10-character token that you recieved before voting and comparing it with the signature given below.
        Your vote signature is: {}

        Thanks,
        Gymkhana Election Committee
    """
}
setDuringInit = ['hostels','gender']