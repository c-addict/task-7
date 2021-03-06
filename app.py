from flask import Flask, render_template, request, send_from_directory, redirect
from utils.fileutils import search_files
import json


app = Flask(__name__)


@app.route('/')
def main():
    return redirect('/search/')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        file_name = request.form['filename']
        with open('json/dirs.json') as dirs_json:
            dirs = json.load(dirs_json)
        found_files = search_files(file_name, dirs)
        return render_template('search.html', files=found_files)


@app.route('/download/<path:path_to_file>/<file_name>')
def download_file(path_to_file, file_name):
    root = '/'
    path = root + path_to_file
    return send_from_directory(directory=path, filename=file_name)


if __name__ == '__main__':
    app.run()
