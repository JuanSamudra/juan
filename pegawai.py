
class Pegawai:
    def __init__(self, conn, cursor):
        self.cur = cursor
        self.conn = conn

    def cari_pegawai(self, id):
        self.cur.execute('SELECT * FROM Pegawai WHERE id_pegawai ='+ id) 
        result = self.cur.fetchall()
        return result

    def tambah (self, id, nama, alamat, email):
        print('Menambahkan data pegawai...')
        query = 'INSERT INTO Pegawai (id_pegawai, nama, alamat, email) VALUES ("' + id +'","'+ nama +'","'+alamat + '","'+email+'")';
        self.cur.execute(query)      
        self.conn.commit()
        # print('Query:', query)
        print('Proses penambahan selesai')

    def hapus(self, id):
        #lanjutkan sendiri
        pass

    def update_alamat(self, id, alamat):
        #lanjutkan sendiri
        pass
