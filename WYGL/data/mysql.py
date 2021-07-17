# Solar
# handsome
import pymysql

class Mysqls (object) :
    def __init__ (self,ip,us,pw,data) :
        db = pymysql.connect (ip,us,pw,data)
        self.cursor = db.cursor ()

    def select (self,diu) :
        self.cursor.execute (diu)
        result = self.cursor.fetchall ()
        return result