import pymysql

class MyDB:
    def connect(self):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='andik12345',
                              database='hrd',
                              )
        cur = con.cursor()
        return con, cur

    def exe_Q(self, tipe, query):

        match tipe:
            case 'select': 
                self.cur.execute(query)
                result = self.cur.fetchall()
            case 'update': 
                self.cur.execute(query)
                result = self.conn.commit()
            case 'insert': 
                self.cur.execute(query)
                result = self.conn.commit()
            case 'delete': 
                self.cur.execute(query)
                result = self.conn.commit()
        return result
    
