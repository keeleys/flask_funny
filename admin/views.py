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

    return page(1)


@app.route('/list/<int:page>.html')
def page(page):
    site = request.args.get("site",None)

    sites = select_sites()
    select = Blog.query

    if site is not None and site != "":
        select = select.filter_by(site=site)

    select = select.order_by(Blog.create_time.desc()).order_by(Blog.type)

    page_blog = select.paginate(page, PAGE_SIZE, False)

    params = {'site': site}
    return render_template('index.html', page=page_blog, sites=sites, params=params)


@app.route('/total.html')
def total():
    # 根据时间 查询所有站点的数量
    totals = select_total()

    return render_template('total.html',totals =totals)