from flask import Flask, request, redirect
from flask import url_for, render_template
from werkzeug.utils import secure_filename
import os

#import subprocess
import grade_program

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'cc'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/dfile")
def upload_file():
    grade = ''
    grade = grade_program.grade()
    return render_template("graded.html", grade_details=grade)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('saving the filename', filename)
            return redirect(url_for('upload_file', name=filename))
    else:
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Arthur LeBlanc's Autograder</h1>
        <p><b>Please select "walk.cc"</b><p>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''
  
@app.route("/index")
def index():
    return "Hello CSCI 4795/6795. This is index page."
@app.route("/about")
def about():
    return "Hello CSCI 4795/6795. This is about page."
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
