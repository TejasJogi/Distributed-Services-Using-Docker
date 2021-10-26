import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './Upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
        
@app.route('/download/<path:path>', methods=['GET', 'POST'])
def get_files(path):
    try:
        return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)
    except FileNotFoundError:
        print(404))


if __name__ == "__main__":
    app.run()
