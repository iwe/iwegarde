FROM python:3.6-alpine
RUN apk add --no-cache openssh-client

RUN adduser -D iwegarde -u 5000 -g 5000

WORKDIR /home/iwegarde

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY iwegarde.py config.py boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP iwegarde.py

RUN chown -R iwegarde:iwegarde ./

USER iwegarde
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
