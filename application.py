from flask import render_template

from app import application

@application.route('/')
def index():
	string = 'Hello World'
	return render_template('index.html', hello=string)

if __name__ == '__main__':
	application.run(debug=True)
