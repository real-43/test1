import face_rec as fr
from flask import Flask, render_template, Response
from werkzeug.datastructures import ResponseCacheControl

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/exec')
def parse(name=None):
    import face_recognize
    print("done")
    return render_template('index.html',name=name)

@app.route('/exec2')
def parse1(name=None):
	import create_data
	print("done")
	return Response(fr.main("test_images/full.jpg"), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
    app.debug = True
