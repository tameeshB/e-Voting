wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
apt-get update && apt-get -y install google-chrome-stable
LATEST_RELEASE=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/$LATEST_RELEASE/chromedriver_linux64.zip -O /evoting/chromedriver_linux64.zip
unzip /evoting/chromedriver_linux64.zip -d /evoting
ls -l /evoting
chmod +x /evoting/chromedriver
export webdriver_chrome=/evoting/chromedriver
export PATH=$PATH:/evoting/chromedriver
test -e $webdriver_chrome && echo file exists || echo file not found 
