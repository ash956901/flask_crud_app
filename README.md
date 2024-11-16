# FLASK CRUD APP

## HOW TO SETUP 

### PREREQUISITES


- Docker 
- Docker Compose 

### Steps

1. Clone the repository:

```
git clone https://github.com/ash956901/flask_crud_app
```

2. Change directory to  the app directory 

```
cd flask_crud_app
```

3. Build the application by docker compose and run it

```
docker-compose up --build
```

4. Access the API at `http://localhost:5002/users` 



### Testing 

- Use Postman to test the endpoints
- `GET /users`
- `GET /users/<id>`
- `POST /users`
- `PUT /users/<id>`
- `DELETE /users/<id>`

### Note

- Create your users by the post request first 
- Make sure you have docker daemon running in the bg
- I have used the regular libararies i use while creating a flask app


