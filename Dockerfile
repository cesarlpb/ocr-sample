FROM tiangolo/uwsgi-nginx-flask:python3.8
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt
WORKDIR /app
COPY . .
CMD python3 app.py