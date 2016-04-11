#!/usr/bin python
# -*- coding: utf-8 -*-
# Created by tianjun 
from admin import db

engine = db.engine


def select_sites():
    return engine.execute("select site from blog GROUP by site")
