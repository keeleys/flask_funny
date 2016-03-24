from bean.user import User
from bean.blog import Blog


def get_user_list():
    yield User("我", '男')
    yield User("小贤儿", '女')


def get_blog_list():
    for i in range(5):
        yield Blog("文章" + str(i), "内容一" + str(i), "作者"+str(i))
