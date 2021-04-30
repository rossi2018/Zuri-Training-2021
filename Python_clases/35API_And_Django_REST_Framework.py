#====================== API ===============================================
# API stands for application programming interface, a concept that applies everywhere from command-line tools to 
# enterprise Java code to Ruby on Rails web apps. An API is a way to programmatically interact with a separate software
# component or resource.

#  Unless you write every single line of code from scratch, you’re going to be interacting with external software components,
#  each with its own API. Even if you do write something entirely from scratch, a well-designed software application will have 
#  internal APIs to help organize code and make components more reusable. And there are numerous public APIs that allow you 
#  to tap into functionality developed elsewhere over the web.

#========Whats is  an API? In English===========================================================
# An API is defined as a specification of possible interactions with a software component.

#API  is the part of the server that receives requests and sends responses.

#At its core, an API is essentially an interface which allows two pieces of software to talk to each other. This usually 
# refers to a request that reaches across the web to a third-party service, although it can also be used to allow two of your
#  own apps to talk to each other.

#API stands for Application Programming Interface. In basic terms, APIs are a set of functions and procedures that allow for
# the creation of applications that access data and features of other applications, services, or operating systems.

#===========Why do we need an API?==============================================================
# Imagine the following scenario: You (as in, your application, or your client, say a web browser or mobile app) wants to access
# another app’s data or functionality.
#For example, perhaps you want to access all Twitter tweets that mention the #jimmychoo hashtag.
#You could email Twitter and ask for a spreadsheet of all these tweets. But then you’d have to find a way to import that 
# spreadsheet into your application.
#Even if you stored them in a database, as we have been, the data would become outdated very quickly. It would be impossible 
# to keep it up to date.
#It would be better and simpler for Twitter to just provide you a way to query their application to get that data so that you 
# can view or use it in your application. It would stay up to date automatically that way.
#So, the API provides access to data, so this data can be included in different applications.

#===============A is for “Application” in API ==================================================
#“Application” can refer to many things. Here are some of them in the context of API:

# 1.A piece of software with a distinct function.
# 2.The whole server, the whole app, or just a small part of an app.
# Basically any piece of software that can be distinctively separated from its environment, can be an “A” in API, and will 
# probably also have some sort of API.

# Let’s say you’re using a third-party library in your code. Once incorporated into your code, a library becomes part of 
# your overall app. Being a distinct piece of software, the library would likely have an API which allows it to interact with 
# the rest of your code.

#=================Public APIs and API integration===============================================
#APIs are a longstanding concept in computer programming, and they have been part of developers’ toolsets for years.
#  Traditionally, APIs were used to connect code components running on the same machine. With the rise of ubiquitous 
# networking, more and more public APIs, sometimes called open APIs, have become available. Public APIs are outward facing 
# and accessible over the Internet, allowing you to write code that interacts with other vendors’ code online; this process 
# is known as API integration.

# These kinds of code mashups allow users to mix and match functionality from different vendors on their own systems. 

#=======History of APIs: SOAP XML V/S REST JSON APIs===========================================
#In 2000, Roy Fielding’s started what we know as modern web APIs thanks to his dissertation “Architectural Styles and the 
# Design of Network-based Software Architectures,” other forms came later.

# All of this is not new. During the 2000s, we had SOAP Services which were leveraged for some of the same use cases.

# REST provides a lighter-weight alternative. Many developers found SOAP cumbersome and hard to use. REST is easy to understand, 
# and it’s simple to write and document.

# This ease of use also makes it easy for other developers to understand and write applications.

#=======================REST API===============================================================
#REST also makes efficient use of bandwidth, as it’s much less verbose than SOAP.

# REST supports many data formats, but the predominant use of JSON means better support for browser clients.

# JSON sets a standardized method for consuming API payloads so that you can take advantage of its connection to JavaScript
#  and the browser. So, what is JSON and why do we use it?

# JSON stands for JavaScript Object Notation and is a way of representing data that looks like JavaScript objects.

# Let’s look at a very typical JavaScript Object for a Restaurant on Yelp, which might look a bit like this:

#            {  "login": "petrgazarov",  "id": 5581195,  "avatar_url": "https://avatars.githubusercontent.com/u/5581195?v=3", 
#                "gravatar_id": "",  "url": "https://api.github.com/users/petrgazarov", 
#                "html_url": "https://github.com/petrgazarov",  "followers_url":  
#                 "https://api.github.com/users/petrgazarov/followers",  "following_url":  
#               "https://api.github.com/users/petrgazarov/following{/other_user}",  "gists_url": 
#               "https://api.github.com/users/petrgazarov/gists{/gist_id}",  "starred_url":
#                "https://api.github.com/users/petrgazarov/starred{/owner}{/repo}",  "subscriptions_url":
#                "https://api.github.com/users/petrgazarov/subscriptions",  "organizations_url": 
#               "https://api.github.com/users/petrgazarov/orgs",  "repos_url": 
#               "https://api.github.com/users/petrgazarov/repos",  "events_url": 
#               "https://api.github.com/users/petrgazarov/events{/privacy}", 
#                "received_events_url": "https://api.github.com/users/petrgazarov/received_events", 
#                "type": "User",  "site_admin": false,  "name": "Petr Gazarov",  "company": "PolicyGenius",  
#               "blog": "http://petrgazarov.com/",  "location": "NYC",  "email": "petrgazarov@gmail.com", 
#                "hireable": null,  "bio": null,  "public_repos": 23,  "public_gists": 0,  "followers": 7, 
#                  "following": 14,  "created_at": "2013-10-01T00:33:23Z",  "updated_at": "2016-08-02T05:44:01Z"}


#Neat. This is fairly easy to read — our data is stored as key/value pairs.

# This means that we can see the key on the left, and the value on the right. The key stays the same for each Restaurant
#  object, but the value would be different.

# A different Restaurant would have a different address, but its properties would be the same — it would always have a name, 
# address, zip, phone, and email.

# So JSON is everywhere in the modern web, mobile, and IoT applications. It’s readable, it’s lightweight, and it works super
#  well with applications written in JavaScript, as it is JavaScript.

# But is also comparatively easy to get applications written in other languages to read it and generate it as well — including 
# Java.

# This means that an API that returns JSON can be accessed by an application written in Java, Ruby, Python, JS, PHP, and many
#  more.

# This makes an API developer-friendly, highly scalable, and platform-independent.

# Aha! Scalable! Platform Independent! Good words, powerful words, $$ words.

#Key takeaways
# It’s important to remember key takeaways for APIs are as follows:

# 1.APIs are prevailing tools that are used to fast-track your business.
# 2.APIs make connections and product shopping possible at a rapid speed such as booking a hotel or ordering a movie ticket.
# 3.APIs provide key insights into real-time possibilities for analytics delivery on the spot.
# 4.APIs give the developer the ability to make an API call or “request” to obtain information.

#===================Why REST API?===================================================================
#Before we get to the code, it’s worth considering why you would want to build an API. If someone had explained these basic
#  concepts to me before I started, I would have been so much better off.
# A REST API is a standardized way to provide data to other applications. Those applications can then use the data however 
# they want. Sometimes, APIs also offer a way for other applications to make changes to the data.

#=====================Using Django REST API framework =======================================================
# First of all,create django project and app in a virtual environment in python 
# Before you use django REST API you must import some models in view.py file of your project which are
# 1. from django.shortcuts import render,get_object_or_404
# 2. from django.http import JasonResponse 

# after adding the model ,add this function to return jason respons

# def home(request):
#     data={
#         'message' : 'This is a jason response'
#     }

#     return JasonResponse(data)


#Next creat app  urls.py file  and configure the project urls.py file to accept the new app urls.py file path in urlpatterns 
#by adding this model and line in urlpattern

# from django.urls import path, include 

# urlpatterns= [
#               path( 'api/', include('nameofapp.urls'))
# ]

# Fill later *****************


#========Installing django REST frame work in ubuntu python virtual virtual environment ======================
# This is the  django REST frame work documentation https://www.django-rest-framework.org/

# Installation
# Install using pip, 
# $ pip install djangorestframework

#Add 'rest_framework' to your INSTALLED_APPS setting.

#INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]


#If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views.
#  Add the following to your root urls.py file.

# urlpatterns = [
#     ...
#     path('api-auth/', include('rest_framework.urls'))
# ]

# Note that the URL path can be whatever you want.