from flask import Flask, render_template, request, redirect, url_for
import hashlib
from tinydb import TinyDB, Query

db = TinyDB('db.json')

User = Query()

app = Flask(__name__)

def make_md5_hash(user_entered_password):
    result = hashlib.md5(user_entered_password.encode())
    password_hash = result.hexdigest()
    return password_hash