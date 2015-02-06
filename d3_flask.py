from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def serve():
	return render_template('d3_test.html')

if __name__ == '__main__':
	app.run()