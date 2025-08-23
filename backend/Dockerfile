# filepath: /my-django-project/my-django-project/backend/Dockerfile
# pull official base image
FROM python:3.10-slim-bullseye

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install gnu utils that include yes command to make sure the setup script for postgres works 
RUN apt-get update && apt-get install -y gnupg2

# install system dependencies
RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install -y --no-install-recommends gcc 

RUN apt-get update && \
    apt-get install -y gettext

# to make the graphviz python library work for django extensions
RUN apt update && apt -y upgrade
RUN apt -y install graphviz

# Install netcat so we can check for establishing connection with postgres
RUN apt install netcat-traditional

# Install postgres tooling
RUN apt install -y postgresql-common
RUN yes | /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
RUN yes | apt install postgresql-client-15

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/backend/entrypoint.sh
RUN chmod +x /usr/src/backend/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]