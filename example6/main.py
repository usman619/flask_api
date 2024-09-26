import os
from flask import Flask, request, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
app.secret_key = 'usman007'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'txt', 'sh', 'py'])

def allow_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_files', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return abort(400, description="No file part in request")
    
    file = request.files['file']
    if file.filename == '':
        return abort(400, description="No file selected")
    
    if file and allow_files(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File successfully uploaded", 200
    else:
        return abort(400, description="File type not allowed")

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)