#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from funny import app, render_template, request

from funny.blog_query import *

from models import Blog

PAGE_SIZE = 10


# http://127.0.0.1:5000/
@app.route('/')
@app.route('/index.html')
def index():
    page = request.args.get('page', 1, type=int)
    page_blog = Blog.query.order_by(Blog.create_time.desc()).paginate(page, PAGE_SIZE, False)
    random_blog = selectRandom()
    return render_template('index.html', random_blog=random_blog,
                           page=page_blog, title="AliFunny", typeIndex="0")


# http://127.0.0.1:5000/123.html
@app.route('/<int:pro_id>.html')
def detail(pro_id=0):
    blog = Blog.query.filter_by(id=pro_id).first()
    updateCheck(pro_id)
    return render_template('detail.html',
                           random_blog=selectRandom(),
                           pid=pro_id, blog=blog,
                           afterBlog=selectBefore(pro_id))


# http://127.0.0.1:5000/list-123.html
@app.route('/list/<int:type>_<int:page>.html')
def blog_list(type, page):
    if type == 0:
        page_blog = Blog.query.order_by(Blog.create_time.desc()).paginate(page, PAGE_SIZE, False)
    elif type == 1:
        page_blog = Blog.query.order_by(Blog.check_num.desc()).paginate(page, PAGE_SIZE, False)
    else:
        page_blog = Blog.query.filter_by(type=(type - 1)).order_by(Blog.create_time.desc()).paginate(page, PAGE_SIZE, False)

    return render_template('index.html', page=page_blog, typeIndex=type, random_blog=selectRandom(), )


@app.route('/hot-funny.html')
def hot_funny():
    return blog_list(1, 1)


@app.route('/funny-pictures.html')
def funny_pictures():
    return blog_list(2, 1)


@app.route('/funny-gif.html')
def funny_gif():
    return blog_list(3, 1)


@app.route('/funny-video.html')
def funny_video():
    return blog_list(4, 1)


@app.route('/rss.xml')
def rss():
    page = Blog.query.order_by(Blog.create_time.desc()).paginate(1, 1000, False)
    return render_template('rss.xml', blogs=page.items)


