# e-Voting   
![Travis-CI](https://travis-ci.com/tameeshB/e-Voting.svg?token=yq4nW8BVWTzVvWaLxEXv&branch=master)
![Django](https://img.shields.io/badge/Django-2.1+-orange.svg)
![Python](https://img.shields.io/badge/Python-3.5%2B-blue.svg)
## apt/brew Dependencies
1. Python : >=3.5
2. Chrome : >=68 (for running functional tests)
3. virtualenv : *
4. MySQL Server : >=8.0.13
  
## Install
1. `virtualenv -p python3 voting`
2. `source voting/bin/activate`
3. `clone https://github.com/tameeshB/e-Voting.git`
4. `cd e-Voting`
5. `nano .env;source .env` # and edit with mysql and webmail credentials.
5. `pip install -r REQUIREMENTS.txt`
6. `python manage.py makemigrations`
7. `python manage.py migrate`
8. `python manage.py loaddata templateMigrationData.json`
9. `python manage.py runserver`

## Run Tests (continue from above setup step 8)
1. `wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip` # linux
2. `unzip chromedriver_linux64.zip`
3. `sudo chmod +x chromedriver`
7. `export webdriver_chrome=$PWD/chromedriver`
8. `export PATH=$PATH:$PWD/chromedriver`
9. `python manage.py runserver &` # run server in background if not already started
10. `python manage.py test tests/` # run the tests
11. `kill %1` # stop server running in background
    
## Some screenshots

![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.14.png)
![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.20.png)
![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.27.png)
