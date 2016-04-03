#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21


from funny import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    type = db.Column(db.String(200))
    img = db.Column(db.String(200))
    site = db.Column(db.String(100))
    detail = db.Column(db.String(200))
    content_id = db.Column(db.String(100))
    mp4 = db.Column(db.String(200))
    create_time = db.Column(db.DATETIME)
    check_num = db.Column(db.Integer)
    html_keys = db.Column(db.String(300))

    def __repr__(self):
        return '<User id:%s>,title %s' % (self.id,self.title.encode("utf-8"))
