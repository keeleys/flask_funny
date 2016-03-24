from flask import Flask, render_template
from service import funnlService as funnlService

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)