#==============================Building A Rest API Endpoint=========================================
#First, let’s explain some terms. REST stands for Representational State Transfer and it is a software architectural design. 
# The API stands for Application Programming Interface; it is an application interface that we interact with programmatically 
# and its based on request and response.
#And generally when you see the word RESTful API, you should know that we are talking about Web Services or Web APIs. 
# It’s like a method expose parts of your application to third-parties i.e external applications and Websites. Its usually 
# data-oriented and like I said earlier, it deals with request and response.
# The good thing about RESTful API is that it can be used by any application built with any language on any platform. As 
# long as the language has support for HTTP, then you are good to go.

#Since Django was built basically for Web Apps, it’ll be time consuming and slightly difficult to build a standard Web APIs 
# endpoint quickly, so we will be using Django Rest Framework; a Django framework specially built for Rest API.
# Django Rest Framework (DRF) is a powerful Django framework for building web APIs. It’s very easy to build model-backed APIs 
# that have authentication, viewset, session and other batteries included.

#===================================Why  use  DRF (Django Rest Framework)?============================
#1. Authentication — It is the best from basic and session-based authentication to token-based and Oauth2 capabilities.
#2. Serialization — It has support for both ORM and Non-ORM data sources and seemlessly integrates with any database.
#3. Viewsets — It has support for viewsets which can replace the Django normal views.
#4.  Good Documentation — If you get stuck somewhere, you can refer to it’s vast online documentation.
#5. Large Community: The community behind it is quite large and has great community support.

#-----------------Another reason to use Django rest framework---------------------
#The biggest reason to use Django REST Framework is because it makes serialization so easy!
# In Django, you define your models for your database using Python. While you can write raw SQL, for the most part the Django 
# ORM(Object Relational Mapper) handles all the database migrations and queries.

# One of the most powerful features of Django is its Object-Relational Mapper (ORM), which enables you to interact with your 
# database, like you would with SQL. In fact, Django's ORM is just a pythonical way to create SQL to query and manipulate your
#  database and get results in a pythonic fashion.

#Think of the Django ORM like a librarian, pulling the information you need for you, so you don’t have to go get it yourself.

# As a developer, this frees you up to worry about the business logic of your application and forget about the low level 
# implementation details. Django ORM handles all that for you.

# The Django REST Framework, then, plays nicely with the Django ORM that’s already doing all the heavy lifting of querying 
# the database. Just a few lines of code using Django REST Framework, and you can serialize your database models to REST-ful
#  formats.
#==========================The Rest API Structure==============================================
#The first step in creating the API, is to define the endpoints (or data) we want to expose. 
#There are a few key options for a REST API request:
# 1. GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
# 2. POST — Creates a new record that gets appended to the database
# 3. PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
# 4. DELETE — Deletes the record at the given URI
# 5. PATCH — Update individual fields of a record

#Typically, an API is a window into a database. The API backend handles querying the database and formatting the response. 
# What you receive is a static response, usually in JSON format, of whatever resource you requested.

# REST APIs are so commonplace in software development, it’s an essential skill for a developer to know how they work.
#  APIs are how applications communicate with one another or even within themselves.
#For example, in web development, many applications rely on REST APIs to allow the front end to talk to the back end. If 
# you’re deploying a React application atop Django, for instance, you’ll need an API to allow React to consume information 
# from the database.
#The process of querying and converting tabular database values into JSON or another format is called serialization. 
# When you’re creating an API, correct serialization of data is the major challenge.

#===============When making a request they are four things you should be mindful of=====================================
# The four things which are the anatomy of the request 
# 1. Endpoint (is the url which you are making your request to)
# 2. Methods . This method are in five which are 
    #1.POST : creating 
    #2.GET : Read
    #3.PUT/PATCH: Updating
    #4.DELETE: Deleting
# 3. Headers: Headers are like information along when you are  making your request, this information allows you to have access to
# some kind of endpoint properly that need to be authenticated to you .
#Each header contain Token or content pipe
