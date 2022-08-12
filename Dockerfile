FROM python:3.7   ## base image from ubuntu system
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT               ## $Port is a variable provided for port no  by heroku
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app    ## workers can be modified according to system 





