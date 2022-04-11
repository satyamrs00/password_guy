# PASSWORD_GUY

It is a web-based password manager application

## Video demo : https://youtu.be/iNvzLyZ2rB0

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

I used the werkzeug security for password hashing because of the fact that the password cannot be retreived from the hash of the password. Werkzeug security uses a salt for the hashed password and that salt is randomly generated. so , its impossible to guess your login password even during a potential database leak.

But the website passwords that you give by "add password" is not salted after hashing.
Because I have to retreive it to show you when you login.
The hashing algorithm used for that passwords is written by me.
It follows basic substitution and as-it-is depending on the characters.

I made the retreiving function as a filter for jinja syntax because the values returned from cursor.fetchall() cannot be modified as it is a tuple.
But I can apply filter to it in the corresponding HTML page.

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

There are 6 HTML pages in this directory.
Of which, one is layout that is extended for every other HTML pages so that I dont have to copy paste those lines of code.
That would just make it cluttered and difficult to read.
and that is a bad design.

#### static/

This folder includes favicon and a css file.
Only basic css functionality is given through the file.
Most of css is used through bootstrap only.
Favicon is downloaded directly through the internet.

## Extras

Feedbacks and Suggestions are much appreciated.

#### delete functionality
I added the delete functionality later in this project.
I added a button next to each password record, you can delete that password by clicking on that button.