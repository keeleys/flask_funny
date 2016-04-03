## 一个flask小例子

```python
# Python 2.7

gunicorn  -b0.0.0.0:8000 funny:app


```

## controller simple

```python
# http://127.0.0.1:5000/
@app.route('/')
@app.route('/index.html')
def index():
    plist = funnlService.get_user_list()
    title = "hello"
    return render_template('index.html', plist=plist, title=title)


# http://127.0.0.1:5000/123.html
@app.route('/<int:pro_id>.html')
def detail(pro_id=0):
     app.logger.info('product %s' % pro_id)
     return render_template('detail.html', pid=pro_id)


# http://127.0.0.1:5000/list-123.html
@app.route('/list-<ptype>.html')
def blog_list(ptype):
    blist = funnlService.get_blog_list()
    return render_template('list.html', blist=blist)

```

## 参考

[sqlalchemy](http://dormousehole.readthedocs.org/en/latest/patterns/sqlalchemy.html)
[flask](http://dormousehole.readthedocs.org/en/latest/quickstart.html#id7)
## gunicorn + supervisor

supervisor.conf
```
[program:funny]
command=gunicorn -w4 -b0.0.0.0:80 funny:app    ; supervisor启动命令
directory=/root/xxx/                                                                    ; 项目的文件夹路径
startsecs=0                                                                             ; 启动时间
stopwaitsecs=0                                                                          ; 终止等待时间
autostart=true                                                                         ; 是否自动启动
autorestart=true                                                                       ; 是否自动重启
stdout_logfile=/root/log/gunicorn.log                           ; log 日志
stderr_logfile=/root/log/gunicorn.err

[supervisord]

```

supervisord 命令
```
supervisord -c supervisor.conf                             通过配置文件启动supervisor
supervisorctl -c supervisor.conf reload                    重新载入 配置文件
supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程
```