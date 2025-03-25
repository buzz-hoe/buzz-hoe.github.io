from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Folder untuk menyimpan foto
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Membuat direktori jika belum ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_nama', methods=['GET', 'POST'])
def form_nama():
    if request.method == 'POST':
        nama = request.form['nama']
        kelas = request.form['kelas']
        return redirect(url_for('form_divisi', nama=nama, kelas=kelas))
    return render_template('form_nama.html')

@app.route('/form_divisi', methods=['GET', 'POST'])
def form_divisi():
    if request.method == 'POST':
        divisi = request.form['divisi']
        nama = request.args.get('nama')
        kelas = request.args.get('kelas')
        return redirect(url_for('form_alasan', nama=nama, kelas=kelas, divisi=divisi))
    return render_template('form_divisi.html')

@app.route('/form_alasan', methods=['GET', 'POST'])
def form_alasan():
    if request.method == 'POST':
        alasan = request.form['alasan']
        file = request.files['foto']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('success.html', nama=request.args.get('nama'), kelas=request.args.get('kelas'), divisi=request.args.get('divisi'), alasan=alasan)
    return render_template('form_alasan.html')

if __name__ == '__main__':
    app.run(debug=True)