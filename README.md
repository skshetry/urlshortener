## URLShortener implemented using Django.


## How to use
1. Install `pipenv` if you don't have by `pip install pipenv`    
2. Then, create a virtual environment using `pipenv --three` command inside the root directory.
3. Activate the shell by `pipenv --shell`,
4. Install all dependencies: `pipenv install`.
5. Install Postgres if you want. Or, edit the `settings.py` and change the `nodefault` in `DATABASES` list to `default` and remove the Postgres one. 
6. Then, create migrations file and then migrate using `cd urlshortener && python manage.py makemigrations && python manage.py migrate`.
7. Create a superuser using `python manage.py createsuperuser`.
8. Run server using `python manage.py runserver`.
