## test flask server

### following ENV params are required to run app:
* MONGODB_HOST - hostname or ip of mongodb
* MONGODB_PORT - mongodb port
* MONGODB_USER - mongodb user
* MONGODB_PASSWORD - mongodb user's password
* MONGODB_DATABASE - mongodb database

### Install requirements:
`pip install -r requirements.txt`

### Build docker container:
`docker build -t example-backend .`

### Run:
* Application runs on default flask port 5000 
