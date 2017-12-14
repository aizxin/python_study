#coding:utf8

from flask import render_template, jsonify
from . import admin
from app.models import User,Tag
from app.admin.forms import LoginForm
import json

@admin.route("/")
def index():
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=1, per_page=10)
    print(page_data)
    return render_template("admin/index.html")

# 登录
@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return jsonify( form.selectField )
    return render_template("admin/login.html",form=form)
