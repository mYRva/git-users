# git-users
Excersice 

# Arquitecture Decision

I decided made the app architecture as simple as possible, trying to make sure any changes that a new developer want to make it can be easily integrate 
like managing a folder named "templates" where basically I placed all the views that the app may requiered for future optimization and a static/styles 
folder as well.

I have no experience (yet) on unit testing programming, so I couldn't integrate it in the code, sorry.

I created an access point (run.py) just to separte the command to start the application from the rest of the scripts

For practicality and security reasonsI store the personal token from github in a env variable on the my Heroku dashboard.

# Mobile View 

![image](https://user-images.githubusercontent.com/5473501/113395863-c581fb80-9357-11eb-83a8-6b593bb04f68.png)
