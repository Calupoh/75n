import functools
import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash
from web75.commands import get_db, get_pwd

bp = Blueprint('admin', __name__, url_prefix='/admin')


def login():
    if request.method == 'POST':
        password = request.form['password']
        pwd = get_pwd()
        error = None
        
        if not check_password_hash(pwd, password):
            error = 'contraseña incorrecta'
        
        if error is None:
            session.clear()
            
