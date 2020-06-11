# e-Voting   
![Travis-CI](https://travis-ci.com/tameeshB/e-Voting.svg?token=yq4nW8BVWTzVvWaLxEXv&branch=master)
![Django](https://img.shields.io/badge/Django-2.1+-orange.svg)
![Python](https://img.shields.io/badge/Python-3.5%2B-blue.svg)

Polling app with a simple, intuitive UX that also takes care of the complexities like privacy, integrity and security behind the scenes.

## Docker Deployment:
1. `docker-compose --env-file .env build`
2. `docker-compose --env-file .env up -d`
3. `docker exec -it [name of django service] bash`
4. `./init_migrate_db.sh`


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

## Admin Actions and Initialization
1. Replace necessary global variables in the `polls/globals.py` file. Make sure to set a random secret key in `secretHash` and `clientKey` to desired password for the init console at `/init`.
2. Create an admin user with the credentials: `source .env;python manage.py createsuperuser` and enter desired credentials.
3. Login with the generated credentials at `http://localhost/admin`.
4. Use the "Token Dashboard" to generate one-time login tokens to hand out to voters.
5. Use the "Poll Control Panel" to control the poll status: Start/Stop the Poll. Count and Publish/Unpublish the results.
6. Before the poll starts, all computers that will be used by the voters must be initialized by visiting `/init` the client-key to be used here is the one in the `polls/globals.py`.

## Run Tests (continue from above setup step 8)
1. `wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip` # linux
2. `unzip chromedriver_linux64.zip`
3. `sudo chmod +x chromedriver`
7. `export webdriver_chrome=$PWD/chromedriver`
8. `export PATH=$PATH:$PWD/chromedriver`
9. `python manage.py runserver &` # run server in background if not already started
10. `python manage.py test tests/` # run the tests
11. `kill %1` # stop server running in background
    
## Problems this app addresses
1. Eliminating manual ballot system.
2. Counting of ballots is a long and laborious process.
3. Wastage of paper.
4. Any simple app made for this purpose might have privacy, security and integrity issues.

## Some screenshots

![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.14.png)
![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.20.png)
![alt text](https://github.com/tameeshB/e-Voting/raw/master/polls/static/polls/images/screen.27.png)
