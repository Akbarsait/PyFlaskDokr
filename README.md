# Python, Flask, and Docker (PyFlaskDokr)
A Simple learning series of Python, Flask, and Docker. This is a document for myself and my fellow learners. 

1. [**Base App**](https://github.com/Akbarsait/PyFlaskDokr/tree/main/01-BaseApp) - Create a base app with docker, python and flask. 
2. [**The Template App**](https://github.com/Akbarsait/PyFlaskDokr/tree/main/02-Templates) - This app enhances the base app with a couple of templates added with the bootstrap framework and uses *render_template* function in the flask. 
3. [**Dynamic Templates**](https://github.com/Akbarsait/PyFlaskDokr/tree/main/03-DynamicTemplates) - Using more dynamic improved templates from the earlier application. 
4. [**Adding Forms**](https://github.com/Akbarsait/PyFlaskDokr/tree/main/04-Forms) - Adding forms/validation in Flask application using Flask-WTF.
5. Database & Models
6. Form Validations 
7. User Authentication
8. Error Managements
9. Deployments.

## How to run the application.

1. Build and start with Docker Compose
```docker
docker-compose up --build
```
2. Visit the site in browser. Use the correct port as mentioned in the *docker-compose.yml*
```html
http://localhost:8080/
```
3. To Stop the docker
```docker
docker-compose stop
```
4. Once the images are done building, we can use the following command to bring the site up. 
```docker
docker-compose up
```