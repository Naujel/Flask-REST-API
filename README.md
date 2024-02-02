# REST API con Flask y MySQL

La aplicacion consiste en una REST API que realiza las operaciones básicas de consultas a una base de datos MySQL con el framework de Python Flask.

## Clone el repositorio de trabajo

```txt
git init https://github.com/Naujel/Flask-REST-API.git
```

## Crear entorno virtual

```txt
python -m virtualenv env
```
___
## Instale los requerimientos de la aplicación

```txt
python install -r requirements.txt
```
___
## Diseñe su base de datos

Utilice la base de datos de referencia del archivo /src/database/flask_db.sql y cree sus variables de entorno del archivo .env

___
## Realice consultas HTTP

Utilice una aplicación de consultas HTTP como Postman o Insomnia a las rutas:

- READ: /api/users/
- DELETE: /api/users/delete
- UPDATE: /api/users/update
