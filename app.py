import os
import json
from flask import Flask,render_template,abort
file_name = '/home/shiyanlou/files/helloshiyanlou.json'
file_name1 = '/home/shiyanlou/files/helloworld.json'
file_path = os.path.abspath(file_name)
file_path1 = os.path.abspath(file_name1)
with open(file_path) as f:
    result = json.load(f)
with open(file_path1) as f:
    result1 = json.load(f)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
@app.route('/')
def index():
    title_list=[result['title'],result1['title']]
    return render_template('index.html',title_list= title_list)


@app.route('/files/<filename>')
def file(filename):
    file_item = [[result],[result1]]
    if not file_item:
        abort(404)
    return render_template('file.html',file_item = file_item)

if __name__ == '__main__':
    app.run()
