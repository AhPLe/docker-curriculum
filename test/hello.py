from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/dfile")
def download_file():
    return render_template("uploaded.html", name=request.args.get('filename'))

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        submission='filename not set'
        return redirect(url_for('download_file', filename=submission))
    else:
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''