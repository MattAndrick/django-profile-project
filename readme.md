## Steps to setup django
### in local directory
- install virtualbox
- install vagrant, vagrant init, & use vagrantfile to determine OS
- mkdir src
- touch .gitignore (add python ignore from github)
- vagrant up to run server
- vagrant ssh to login to server
### in vagrant server:   
- mkvirtualenv "env name" --python=python3
- (deactivate / workon "env name")
- pip install django=="version"
- pip install djangorestframework=="version"
- cd /vagrant/src
- django-admin.py startproject "project name"
- cd "project-name"
- python manage.py startapp "app name"

### add apps
- open src >project_dir >project_dir >settings.py 
- add apps to INSTALLED_APPS list
    - rest_framework
    - rest_framework.authtoken
    - "app_name"
### create requirements file
- in vagrant server, logged in to virtualenv, in /vagrant/ folder:
- pip freeze (view packages installed)
- pip freeze > requirements.txt

### run test server
- in vagrant server, logged into virtualenv:
- cd /vagrant/src/"project name"
- python manage.py runserver 0.0.0.0:8080
- This runs the server on all ip's, out of port 8080. This means on the local computer, the server will be accessible at the ip address specified in the vagrantfile

### creating models
- creating the models: see models.py file for example
- update settings.py to update any defaults to the new one (like default user model)
- in vagrant server, logged into virtualenv:
- cd /vagrant/src/"project name"
- python manage.py makemigrations (creates the blueprint for updating the database with the model)
- python manage.py migrate (creates the database)