#!/usr/bin python
# -*- coding: utf-8 -*-
# Created by tianjun 
from admin import db

engine = db.engine


def select_sites():
    return engine.execute("select site from blog GROUP by site")

def select_total():
    sql="select site,count(site) from blog GROUP by site "
    return list(engine.execute(sql))