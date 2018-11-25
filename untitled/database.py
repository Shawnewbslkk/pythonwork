import pymysql
import base64

jpg = open(r'E:\pythonwork\timg.jpg', 'rb')
img = base64.b64encode(jpg.read())
jpg.close()


db = pymysql.connect(host='127.0.0.1', user='root', password='mm5201314', database='newone', port=3306,
                         cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("insert into carousemap(id,title,src) value(%s,%s,%s)", (0, 'first', img))


cursor.execute('select * from carousemap')
print (cursor.fetchall())