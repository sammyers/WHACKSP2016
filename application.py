from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
	string = 'Hello World'
	return render_template('index.html', hello=string)

if __name__ == '__main__':
	application.run(debug=True)
