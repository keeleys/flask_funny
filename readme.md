## flask 项目

启动方式 gunicorn + supervisord
```python
# Python 2.7

cd youapppath
# gunicorn  -b0.0.0.0:8000 funny:app
supervisord -c supervisor.conf

```


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
关闭和启动貌似都没效果 是因为配置不全,目前我是用kill pid方式来进行关闭的,配置全之后可以用浏览器访问监控程序的运行.

## 参考

[sqlalchemy](http://dormousehole.readthedocs.org/en/latest/patterns/sqlalchemy.html)
[flask](http://dormousehole.readthedocs.org/en/latest/quickstart.html#id7)
[supervisord](http://feilong.me/2011/03/monitor-processes-with-supervisord)