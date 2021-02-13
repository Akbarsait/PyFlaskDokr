# Base App
The first base app includes the following. 
- **Dockerfile** - Install the Docker, add add the *Dockerfile* to the directory. The contents of the file are self-explantory. One thing to note though is the use of slim-buster version of python docker image. 
- **docker-compose.yml** - Add the docker compose file to the directory. 
- **baseapp/app.py** - Add this file with Hello World return text. 

## Let's build and Run
1. Let's build the image using the command and run the container. Make sure you run this command from the app directory root. 

```cmd
$ docker-compose up --build
```
2. You will be seeing something similar like below based on your setup. 
```cmd 
Successfully built 09b229a8b9f0
Successfully tagged baseapp_website:latest
Creating baseapp_website_1 ... done
Attaching to baseapp_website_1
website_1  | [2021-02-06 09:19:00 +0000] [1] [INFO] Starting gunicorn 20.0.4
website_1  | [2021-02-06 09:19:00 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
website_1  | [2021-02-06 09:19:00 +0000] [1] [INFO] Using worker: sync
website_1  | [2021-02-06 09:19:00 +0000] [9] [INFO] Booting worker with pid: 9
website_1  | [2021-02-06 10:19:33 +0000] [9] [INFO] Worker reloading: /baseapp/baseapp/app.py modified
website_1  | [2021-02-06 10:19:33 +0000] [9] [INFO] Worker exiting (pid: 9)
website_1  | [2021-02-06 10:19:33 +0000] [11] [INFO] Booting worker with pid: 11
```
3. Navigate to http://localhost:8000/ to view the hello world page. Port 8000 is used as we defined it in the *Dockerfile*. 

