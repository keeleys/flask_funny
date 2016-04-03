from flask import Flask, render_template
from service import funnlService as funnlService

from bean.database_extention import db
from bean.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/funny'
db.init_app(app)




if __name__ == '__main__':
    app.run()
