import numpy as np
import h5py
from PIL import Image

import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug import secure_filename
app = Flask(__name__)
app.secret_key = 'ku$ol'

os.makedirs(os.path.join('static/uploads'), exist_ok=True)

@app.route('/')
def html():
    return render_template('upload.html')
	
@app.route('/predict', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename.endswith('.jpg') or f.filename.endswith('.png') or f.filename.endswith('.jpeg'):
            f.save(os.path.join('static/uploads', secure_filename(f.filename)))
        else:
            flash('Please select an Image file !')
            return redirect(url_for("html"))

		
if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')
