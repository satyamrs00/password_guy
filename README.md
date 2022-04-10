# PASSWORD_GUY

It is a web-based password manager application

## Video demo : 

## Description

Now-a-days there are a lot of websites we visit and sign up for. 
Remembering the sign up credentials is no easy task.
Thats why i created this app called Password Guy like "there is always a guy".
This app stores information like websites , username and its password.
You have to manually input the data through our website.
Dont worry the passwords you input are encrypted before adding to our records.
So, even during a data breach your passwords are safe with us.


### Files in this project

#### app.py

This is the main app of the project.
It is written in python using Flask framework.
Libraries included in this file are sqlite3 , flask , flask-session , werkzeug.security.

I used the werkzeug security for password hashing because of the fact that the password cannot be retreived from the hash of the password.

I used sqlite for this project because it is light weight and simple.
I might not be using huge sets of data in this project. So, its good for this project.

#### helpers.py

This is a python file for declaring custom functions to use in the main app.
Libraries included are flask and functools.

Functools library is included for @wraps function.

The functions declared are login_required , apology , and a custom hashing algorithm so we dont store passwords directly in database.

#### templates/

This folder includes all the HTML files needed for the project.

The HTML files uses **jinja syntax** for better management.
**Bootstrap** is also used for easier implementation of css, and maintain a consistency over the pages.

#### static/

This folder includes favicon and a css file.
Only basic css functionality is given through the file.
Most of css is used through bootstrap only.

## Extras

Feedbacks and Suggestions are much appreciated.