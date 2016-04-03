#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from funny import db
from funny.blog_query import *

if __name__ == '__main__':
    #db.create_all()
    print selectHome()

    #for item in selectRandom():
    #    print item

    #print engine.execute("select * from blog").first()