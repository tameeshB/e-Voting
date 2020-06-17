FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /evoting
WORKDIR /evoting
ADD REQUIREMENTS.txt /evoting/
RUN pip install virtualenv
RUN virtualenv -p python3 voting_
RUN . voting_/bin/activate
RUN pip install -r REQUIREMENTS.txt
ADD . /evoting/
RUN chmod +x init_migrate_db.sh
