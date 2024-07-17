from flask import Flask, request, send_file, render_template, redirect, url_for
from PIL import Image
import io
import os
import shutil

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    width = int(request.form['width'])
    height = int(request.form['height'])

    image = Image.open(file)
    resized_image = image.resize((width, height))

    img_io = io.BytesIO()
    resized_image.save(img_io, 'JPEG')
    img_io.seek(0)

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resized_image.jpg')
    with open(file_path, 'wb') as f:
        f.write(img_io.getbuffer())

    return redirect(url_for('download'))

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/download_image')
def download_image():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resized_image.jpg')
    response = send_file(file_path, as_attachment=True)

    # Delete the folder after sending the file
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])

    return response

if __name__ == '__main__':
    app.run(debug=True)
