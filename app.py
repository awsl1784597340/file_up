import os
from flask import *

import json

app = Flask(__name__)

def getfilelist():
    file_path = './uploads'
    return os.listdir(file_path)


@app.route('/list')
def history():
    return_data = {'code': 200, 'filelist': getfilelist()}
    return json.dumps(return_data)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

history_list = []

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


if __name__ == '__main__':
    app.run()