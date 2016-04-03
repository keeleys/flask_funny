#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21


from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/funny'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import funny.views
import funny.blog_query