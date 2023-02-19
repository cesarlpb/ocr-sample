# ocr-sample
Simple OCR app using API with Python

```
pip install paddleocr
pip install paddlepaddle
```

- Created `requirements.txt`
- Created `Dockerfile`
- To check if port available:
```bash
sudo nc localhost 8080 < /dev/null; echo $?
```
- Updated to Python 3: [https://phoenixnap.com/kb/how-to-install-python-3-ubuntu](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) 
- Deploy Flask app: [https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04)

```
version: '2.13.0'
services:
  jnb:
    image: stefanoandre/jupyter
    container_name: jupyter
    ports:
    - "8888:8888"
    stdin_open: true 
    tty: true
    volumes:
      - c:\jnbs:/stefanos   
    networks:
      - mynet
networks:
  mynet:
    driver: bridge
``` 
Comandos útiles:

```
docker-compose --build
```
Detached (segundo plano):
```
docker-compose up --build -d
```
Borrar las imágenes no activas:
```
docker-compose down --rmi all
```

Dependencias - Añadido a `docker-compose.yaml`:
```
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
```