FROM ubuntu:latest
RUN apt-get update
RUN apt-get install python3 -y
RUN apt install python3-pip -y
RUN apt install gunicorn -y
WORKDIR /home/nof/Escritorio/deploy/P2-NOF
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY narcis_app.py narcis_app.py
COPY ./templates ./templates
COPY ./static ./static
COPY db.db db.db
COPY db_esports.py db_esports.py
COPY narcis_app.swgi narcis_app.swgi
COPY gunicorn.sh gunicorn.sh
ENTRYPOINT [ "./gunicorn.sh" ]
