import flask

app = flask.Flask(__name__)
app.template_folder = 'templates'

import controllers.index
import controllers.hello
import controllers.subject
import controllers.olympiad

# @app.route('/')
# def index():
#     return 'Hello World!'

# if __name__ == '__main__':
#    app.run()
