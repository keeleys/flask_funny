#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21
from funny.models import Blog
from funny import db

engine = db.engine


def selectHome():
    return engine.execute(" select * from blog order by content_id desc limit 0 ,16")


def select_page(off=1, limit=10):
    return Blog.query.all()


def updateCheck(id):
    return engine.execute("update blog set check_num = ifnull(check_num,0) + 1 where id = %s", id)


def selectBefore(id):
    return engine.execute("select * from blog where id < %s order by id desc limit 0,1", id).first()


def selectRandom():
    sql = """
    SELECT * FROM `blog` AS t1 JOIN (SELECT
        ROUND(RAND() * ((SELECT MAX(id) FROM `blog`)-(SELECT MIN(id) FROM `blog`))+(SELECT MIN(id) FROM `blog`))
        AS id from `blog`  limit 6) AS t2 on t1.id=t2.id ORDER BY t1.id ;
    """
    return engine.execute(sql)


if __name__ == '__main__':
    pass
