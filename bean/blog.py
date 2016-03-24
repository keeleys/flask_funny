class Blog(object):
    title = ""  # 标题
    content = ""  # 内容
    user = ""  # 创建人

    def __init__(self, title=title, content=content, user=user):
        self.title = title
        self.content = content
        self.user = user
