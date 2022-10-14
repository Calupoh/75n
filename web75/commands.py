import sqlite3
import json
import click
from flask import current_app, g
from werkzeug.security import generate_password_hash


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_pwd():
    r_pwd = current_app.config['PWD']

    return r_pwd


def init_db():
    db = get_db()

    with current_app.open_resource('esquema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """limpia la base actual, si es que existe, y crea una nueva"""
    init_db()
    click.echo('base de datos iniciada')


@click.command('admin-pwd')
@click.argument('pwd', default='admin')
def admin_pwd_command(pwd):
    """asigna una contraseña para el usuario administrador"""
    r_pwd = get_pwd()
    with open(r_pwd, 'w', encoding='utf-8') as f:
        pwd = generate_password_hash(pwd)
        json.dump(pwd, f)
    click.echo('contraseña de administrador restablecida')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(admin_pwd_command)
