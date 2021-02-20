#Docker image name to be downloaded from docker hub if not available locally. 
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# These var set during image build also available after container launched. 
ENV INSTALL_PATH /baseapp
RUN mkdir -p $INSTALL_PATH

# Keeps to set the working dir
WORKDIR $INSTALL_PATH

#copy files, dir and remote url files to destination within the filesystem of Docker images. 
COPY requirements.txt requirements.txt

#used to execute any commands on top of the current image and it will create a new layer. 
RUN pip install -r requirements.txt

COPY . .

#used to set a command to be executed when running a container. There must be only one CMD in a dockerfile. Last CMD will takes effect if more exists. 
CMD gunicorn -b 0.0.0.0:5000  "baseapp.app:app"