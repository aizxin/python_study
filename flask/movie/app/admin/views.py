#coding:utf8

from flask import render_template

from . import admin
from app.models import User,Tag

@admin.route("/")
def index():
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=1, per_page=10)
    print(page_data)
    return render_template("admin/index.html")

@admin.route('/login')
def login():
    return render_template("admin/login.html")
