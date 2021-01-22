# SibDev test task
#Global dependencies
* Docker
    * Ubuntu/Debian: sudo apt install docker
* Docker-compose
    * Ubuntu/Debian: sudo apt install docker-compose

# First start
* docker-compose up --build
* docker-compose run --rm api sh -c "./manage.py makemigrations"
* docker-compose run --rm api sh -c "./manage.py migrate"

# Start project
docker-compose up

# API Method
URL | Method | Payload | Description
--- | --- | --- | ---
api/v1/ | POST | {deals: 'csv file'} | Adding deals to database
api/v1/ | GET | None | View top five clients and popular gems

