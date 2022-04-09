from flask import session, redirect, render_template
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def apology(message):
    return render_template("apology.html", message=message)

def myhashing(passw1):
    hpassw1 = ""
    codelist = ["z","a","q","s","w","c","d","e","v","f","r","b","g","t","n","h","y","m","j","u","k","i","l","o","p"]
    for i in range(len(passw1)):
        if passw1[i].isupper():
            hpassw1 += chr(ord(codelist[ord(passw1[i])- 65]) -32)
        elif passw1[i].islower():
            hpassw1 += codelist[ord(passw1[i]) - 97]
        else:
            hpassw1 += passw1[i]
    return hpassw1

def myreversehashing(hpassw2):
    def searching(array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i

    passw2 = ""
    codelist = ["z","a","q","s","w","c","d","e","v","f","r","b","g","t","n","h","y","m","j","u","k","i","l","o","p"]
    for i in range(len(hpassw2)):
        if hpassw2[i].islower():
            index = searching(codelist, hpassw2[i])
            passw2 += chr(97 + index)
        elif hpassw2[i].isupper():
            index = searching(codelist, chr(ord(hpassw2[i]) + 32))
            passw2 += chr(65+ index)
        else:
            passw2 += hpassw2[i]
    return passw2