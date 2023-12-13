from flask import Flask, render_template, redirect, url_for, request
from mysql import connector

app = Flask(__name__)

db = connector.connect(
    host       = 'localhost',
    user       = 'root',
    passwd     = '',
    database   = 'perpus'
)

@app.route('/', methods=['GET', 'POST'])
def masuk():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('daftar_buku'))
    return render_template('masuk.html', error=error)

@app.route('/daftar_buku/', methods=['GET'])
def daftar_buku():
    cur = db.cursor()
    cur.execute("select * from buku")
    res = cur.fetchall()
    cur.close()
    return render_template('list_buku.html', hasil=res)

@app.route('/tambah_buku/')
def tambah_data():
    return render_template('tambah_buku.html')

@app.route('/proses_tambah_buku/', methods=['POST'])
def proses_tambah():
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    pengarang = request.form['pengarang']
    penerbit = request.form['penerbit']
    cur = db.cursor()
    cur.execute('INSERT INTO buku (id_buku, judul_buku, pengarang, penerbit) VALUES (%s, %s, %s, %s)', (id_buku, judul_buku, pengarang, penerbit))
    db.commit()
    return redirect(url_for('daftar_buku'))

@app.route('/ubah/<id_buku>', methods=['GET'])
def ubah_buku(id_buku):
    cur = db.cursor()
    cur.execute('select * from buku where id_buku=%s', (id_buku,))
    res = cur.fetchall()
    cur.close()
    return render_template('ubah_buku.html', hasil=res)

@app.route('/proses_ubah_buku/', methods=['POST'])
def proses_ubah_buku():
    no_id_buku = request.form['id_buku_ori']
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    pengarang = request.form['pengarang']
    penerbit = request.form['penerbit']
    cur = db.cursor()
    sql = "UPDATE buku SET id_buku=%s, judul_buku=%s, pengarang=%s, penerbit=%s WHERE id_buku=%s" 
    value = (id_buku, judul_buku, pengarang, penerbit, no_id_buku)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('daftar_buku'))

@app.route('/hapus_buku/<id_buku>', methods=['GET'])
def hapus_buku(id_buku):
    cur = db.cursor()
    cur.execute(f'DELETE from buku where id_buku="{id_buku}"')
    db.commit()
    return redirect(url_for('daftar_buku'))


@app.route('/peminjaman', methods=['GET'])
def pinjam_buku():
    cur = db.cursor()
    cur.execute("SELECT * FROM peminjaman")
    res = cur.fetchall()
    cur.close()
    return render_template('peminjaman.html', hasil=res)

@app.route('/pinjam_buku/')
def pinjam_data():
    return render_template('tambah_peminjaman.html')

@app.route('/proses_pinjam_buku/', methods=['POST'])
def proses_pinjam():
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    peminjam = request.form['peminjam']
    tanggal_pinjam = request.form['tanggal_pinjam']
    cur = db.cursor()
    cur.execute('INSERT INTO peminjaman (id_buku, judul_buku, peminjam, tanggal_pinjam) VALUES (%s, %s, %s, %s)', (id_buku, judul_buku, peminjam, tanggal_pinjam))
    db.commit()
    return redirect(url_for('pinjam_buku'))

@app.route('/ubah_peminjam/<id_buku>', methods=['GET'])
def ubah_peminjam(id_buku):
    cur = db.cursor()
    cur.execute('select * from peminjaman where id_buku=%s', (id_buku,))
    res = cur.fetchall()
    cur.close()
    return render_template('ubah_peminjam.html', hasil=res)

@app.route('/proses_ubah_peminjam/', methods=['POST'])
def proses_ubah_peminjam():
    no_id_buku = request.form['id_buku_ori']
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    peminjam = request.form['peminjam']
    tanggal_pinjam = request.form['tanggal_pinjam']
    cur = db.cursor()
    sql = "UPDATE peminjaman SET id_buku=%s, judul_buku=%s, peminjam=%s, tanggal_pinjam=%s WHERE id_buku=%s" 
    value = (id_buku, judul_buku, peminjam, tanggal_pinjam, no_id_buku)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('pinjam_buku'))

@app.route('/hapus_pinjam_buku/<id_buku>', methods=['GET'])
def hapus_pinjam_buku(id_buku):
    cur = db.cursor()
    cur.execute(f'DELETE from peminjaman where id_buku="{id_buku}"')
    db.commit()
    return redirect(url_for('pinjam_buku'))


@app.route('/pengembalian', methods=['GET'])
def kembali_buku():
    cur = db.cursor()
    cur.execute("SELECT * FROM pengembalian")
    res = cur.fetchall()
    cur.close()
    return render_template('pengembalian.html', hasil=res)

@app.route('/pengembalian_buku/')
def pengembalian_data():
    return render_template('tambah_pengembalian.html')

@app.route('/proses_pengembalian_buku/', methods=['POST'])
def proses_pengembalian():
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    peminjam = request.form['peminjam']
    tanggal_kembali = request.form['tanggal_kembali']
    cur = db.cursor()
    cur.execute('INSERT INTO pengembalian (id_buku, judul_buku, peminjam, tanggal_kembali) VALUES (%s, %s, %s, %s)', (id_buku, judul_buku, peminjam, tanggal_kembali))
    db.commit()
    return redirect(url_for('kembali_buku'))

@app.route('/ubah_pengembalian/<id_buku>', methods=['GET'])
def ubah_pengembalian(id_buku):
    cur = db.cursor()
    cur.execute('select * from pengembalian where id_buku=%s', (id_buku,))
    res = cur.fetchall()
    cur.close()
    return render_template('ubah_pengembalian.html', hasil=res)

@app.route('/proses_ubah_pengembalian/', methods=['POST'])
def proses_ubah_pengembalian():
    no_id_buku = request.form['id_buku_ori']
    id_buku = request.form['id_buku']
    judul_buku = request.form['judul_buku']
    peminjam = request.form['peminjam']
    tanggal_kembali = request.form['tanggal_kembali']
    cur = db.cursor()
    sql = "UPDATE pengembalian SET id_buku=%s, judul_buku=%s, peminjam=%s, tanggal_kembali=%s WHERE id_buku=%s" 
    value = (id_buku, judul_buku, peminjam, tanggal_kembali, no_id_buku)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('kembali_buku'))

@app.route('/hapus_kembali_buku/<id_buku>', methods=['GET'])
def hapus_kembali_buku(id_buku):
    cur = db.cursor()
    cur.execute(f'DELETE from pengembalian where id_buku="{id_buku}"')
    db.commit()
    return redirect(url_for('kembali_buku'))

if __name__ == '__main__':
    app.run(debug=True)