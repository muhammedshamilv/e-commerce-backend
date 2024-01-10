## Local development

### Database

For setting up a local database follow below instruction.
To run the application locally, you need to setup a postgres database on your system.
Install postgres

```
sudo apt install postgresql libpq-dev
```

Login as the 'postgres' user and start postgres shell

```
sudo su - postgres
psql
```

Create a database

```
create database ecommerce;
```

Create a user

```
create user ecomerceuser with password ‘pswd’
```

Grant all privileges to user

```
grant all privileges on database ecommerce to ecomerceuser;

ALTER USER ecomerceuser CREATEDB;
```

Follow below instructions after setting up database.

create a .env file and replace your DATABASE_URL

```
cp env.example .env
```

To install dependencies:

To apply existing migration file:

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

Whenever a database migration needs to be made. Run the following commands

```
python manage.py makemigrations
```

This will generate a new migration script. Then run

```
python manage.py migrate
```

To apply the migration.

### To run the application :

make your way to the repo root

```
python manage.py runserver
```

To view API documentation go to

admin should be logged in to admin site to access API documentation and redoc

```
http://127.0.0.1:8000/swagger/
```

redoc url

```
http://127.0.0.1:8000/redoc/
```

admin site url

```
http://127.0.0.1:8000/admin/
```

To create admin user

email is used to login to admin account

```
python manage.py createsuperuser
```

To run test

```
pytest
```
