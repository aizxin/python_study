#coding:utf8

from flask import render_template, jsonify, request
from . import admin
from app.models import User,Tag
from app.admin.forms import LoginForm
import json

def errors_first(errors):
    k = ''
    for v in errors:
        k = errors[v][0]
        break
    return k

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
    if request.method == "POST":
        if form.validate_on_submit():
            return jsonify({ 'success': True,
                'message': 'form.message'})
        else:
            return jsonify({'success': False,
                        'message': errors_first(form.errors) })
    return render_template("admin/login.html",form=form)