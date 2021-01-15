# InstaPic-API
RESTful API built with Flask (Python) for InstaPic web-app. 

### Link - https://instapic-backend-api.herokuapp.com/

## Terminal Commands

	Initial installation: make install

	To run test: make tests

	To run application: make run

	To run all commands at once : make all

	To test and check coverage: make coverage


## Commands to initialize the database

	> python manage.py db init

	> python manage.py db migrate

	> python manage.py db upgrade`
	
## Viewing the app
	
	http://127.0.0.1:5000/  
or
	localhost:5000/
	 
## Postman Instructions

	Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"
	

## Acknowledgement
	
Built using FLASK RESTX BOILER-PLATE WITH JWT by Greg Obinna.


## Key Points

* Coverage is 100%
* Images stored as base64 instead of blobs since it might be messy.
* User specific requests aren't implemented yet.
* Lack of documentation.
	