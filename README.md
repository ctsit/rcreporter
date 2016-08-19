# Reporting Tool

Web app for user friendly represntation of Data containing reporting statistics from REDCap and analysis.

##How to install

Requires charit, django-filter, bootstrap-toolkit and django-tables2

pip install django_chartit
pip install django-filter
pip install django-bootstrap-toolkit
pip install django-tables2

Add 'charit', 'django-filter', 'bootstrap-toolkit', 'django-tables2' 
to INSTALLED_APPS

##Location of database
The sqlite database path should be mentioned to the web app.

This can be done by mentioning it 'settings.py' under CTSI folder.
There is a 'DATABASES' dictionary where we need to mention the path
of the database in the 'NAME' key with respect to sqlite3. 


The main folder rcreporter is basically a Project which can house various apps. 
Currently this project contains only one app, which is reportingTool. 

##How to handle changes made to models.
After making a change to a model, we need to let the django know about the changes.

Run:
./manage.py makemigrations reportingTool

This will generate the relevant ORM queries for the new changes in the models
for the reportingTool app. 

Django needs to still pass this info to the database. Inorder to commit these changes to 
the database, use:
./manage.py migrate

This will commit the unsaved changes to the database.

##How to run
./manage.py runserver
