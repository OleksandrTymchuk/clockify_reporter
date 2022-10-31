# Clockify Reporter
## Daily CLI reporter from Clockify


### Required modules
Install all modules from `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### API Key
Go to **https://app.clockify.me/user/settings** and generate API key

Open `.env.example` file and paste your API Key

Rename `.env.example` to `.env` and don't forget to fill another variables like: MYSQL_USER, MYSQL_PASSWORD, ETC ...
### Run with Docker 

You can start the project with docker using this command:
```bash
docker-compose up --build
```
This command exposes the web application on port 8000, mounts current directory

### Admin Panel

First of all we need to go inside the docker container with command (docker container should be running at this moment):
```bash
docker-compose exec web bash
```
To create Superuser write the next command:
```bash
python manage.py createsuperuser
```
To access the login panel use this url address: **http://0.0.0.0:8000/admin**