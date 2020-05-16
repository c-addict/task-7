from flask import Flask, render_template, request, send_from_directory
<<<<<<< HEAD
=======
import os
>>>>>>> e504aea8b39f015feaae3d65c98770087ee2d6ac
from utils.fileutils import search_files
import json


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


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
<<<<<<< HEAD
    root = '/'
    path = root + path_to_file
    return send_from_directory(directory=path, filename=file_name)
=======
    print(path_to_file, file_name)
    return send_from_directory(directory='/' + path_to_file, filename=file_name)
>>>>>>> e504aea8b39f015feaae3d65c98770087ee2d6ac


@app.route('/help/')
def help_():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()
