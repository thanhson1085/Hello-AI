import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from catordog import CatOrDog

from os.path import basename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.catordog = CatOrDog()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            thisis = app.catordog.run(file_path)
            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], thisis + '__' + filename))


            print("--- %s seconds ---" % str (time.time() - start_time))
            return redirect("/")
            return redirect(url_for('uploaded_file',
                                    filename="facedetect-"+filename))

    from os import listdir
    from os.path import isfile, join
    htmlpic=""
    for f in listdir(UPLOAD_FOLDER):
        if isfile(join(UPLOAD_FOLDER,f)) and f != '.gitignore':
            print(f)
            htmlpic += """<span>""" + f.split('__')[0] + """--></span>""" + """
                <img width=200px height=150px src='uploads/"""+f+"""'>&nbsp;  &nbsp;
                """
    return '''
    <!doctype html>
    <head>
    <title>Cat Or Dog</title>
    </head>
    <h1>Upload new File - Cat or Dog</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''+htmlpic

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=3000)
