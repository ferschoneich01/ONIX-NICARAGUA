from flask import redirect, render_template, request, session
from functools import wraps
from cs50 import SQL
import os
import urllib.request

db = SQL("sqlite:///Data.db")

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

