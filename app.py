from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    nama = request.form['nama']
    tugas = float(request.form['tugas'])
    uts = float(request.form['uts'])
    uas = float(request.form['uas'])

    # Perhitungan nilai akhir
    nilai_akhir = (tugas * 0.4) + (uts * 0.3) + (uas * 0.3)

    return render_template('hasil.html', nama=nama, nilai_akhir=round(nilai_akhir, 2))

if __name__ == '__main__':
    app.run(debug=True)




