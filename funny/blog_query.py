#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21
from funny import db

engine = db.engine


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


def select_by_month(month):
    sql = "select * from blog  where date_format(create_time,'%%Y-%%m')=%s order by id desc"
    return engine.execute(sql,month)

def select_all_month():
    sql ="select DATE_FORMAT(create_time,'%%Y-%%m') months,max(create_time) as max_date from blog group by months order by months"
    return engine.execute(sql)
