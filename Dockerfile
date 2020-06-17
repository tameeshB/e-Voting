FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /evoting
WORKDIR /evoting
ADD . /evoting/
RUN pip install -r REQUIREMENTS.txt && \
    chmod +x init_migrate_db.sh
