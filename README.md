# Zprava-server
Server side implementation for Zprava application

# INSTALL


### Linux/Unix and MacOS X Installation

Pre-requirements:

Zprava have a official domain and host on [Zprava](https://zprava.ir/admin/). but to run the code with the server capabilities on a local machine do as follow:
If you dont have Django installed on your system please install it from the following link:
- [Install Django](https://docs.djangoproject.com/en/2.0/topics/install/)
- [Install Django REST API](http://www.django-rest-framework.org/#installation)

or just run the following command in the command line:
```bash
$ pip install Django==2.0.5
$ pip install djangorestframework
```

Next run the server from your terminal:

```bash
$ git clone https://github.com/kianbehzad/Zprava-server.git 
$ cd Zprava-server/Zprava
$ python3 manage.py makemigrations signup
$ python3 manage.py makemigrations chat
$ python3 manage.py migrate
$ python3 manage.py runserver
```

you can find the client application in [Client](https://github.com/kianbehzad/Zprava) repository.



### Windows Installation

Pre-requirements:

Zprava have a official domain and host on [Zprava](https://zprava.ir/admin/). but to run the code with the server capabilities on a local machine do as follow:
If you dont have Django installed on your system please install it from the following link:
- [Install Django](https://docs.djangoproject.com/en/2.0/topics/install/)
- [Install Django REST API](http://www.django-rest-framework.org/#installation)

Next run the server from your terminal:

```bash
$ git clone https://github.com/kianbehzad/Zprava-server.git 
$ cd Zprava-server/Zprava
$ python3 manage.py makemigrations signup
$ python3 manage.py makemigrations chat
$ python3 manage.py migrate
$ python3 manage.py runserver
```

you can find the client application in [Client](https://github.com/kianbehzad/Zprava) repository.



