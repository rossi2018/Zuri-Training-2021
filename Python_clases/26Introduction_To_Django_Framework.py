#Installing Django in ubuntu 
#Django source code is available as Github repository. You can also use pip to install Django on Ubuntu systems
#use this comand to install django= 
# pip3 install Django
#---------------------------------------------------->>
#Create A Django Application
#use this command to create django application=
#django-admin startproject <name of application>
#---------------------------------------------------->>
#To run our first django server ,use this command=
#python3 manage.py runserver 
#---------------------------------------------------->>
#To create your django application, use this command =
#python3 manage.py startapp <name of app>
#Note: Make sure you are in the django application directory before running the  aboved command
#---------------------------------------------------->>
#The first thing to do after creating your django app is adding urls because it doesnt come with its 
#urls files so you have to create its own urls file and copy the content of the application urls to the new urls
#====================================================>>
#Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, 
# etc.) into your database schema. They're designed to be mostly automatic, but you'll need to know when to 
# make migrations, when to run them, and the common problems you might run into.

#To run migration use this command=
#python3 manage.py migrate
#===================================================>>
#Creating a Super User for Django Application=
#python3 manage.py createsuperuser
#Note:You use your django admin to register your model 



