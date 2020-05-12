from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        return render_template('search.html', files=[])


@app.route('/help/')
def help_():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()
