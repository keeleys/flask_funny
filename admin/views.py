#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from admin import app, render_template, request

from models import Blog

from query import *

PAGE_SIZE = 20


# http://127.0.0.1:5000/
@app.route('/')
@app.route('/index.html')
def index():
    site = request.args.get("site")
    return page(1, site)


@app.route('/list/<int:page>.html')
def page(page, site=None):
    sites = select_sites()
    select = Blog.query

    if site is not None and site != "":
        select = select.filter_by(site=site)

    select = select.order_by(Blog.create_time.desc()).order_by(Blog.type)

    page_blog = select.paginate(page, PAGE_SIZE, False)
    return render_template('index.html', page=page_blog, sites=sites, site=site)
