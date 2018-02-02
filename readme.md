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
- 