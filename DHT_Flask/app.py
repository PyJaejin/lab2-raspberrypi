from flask import *
from DHT22 import get_DHT
import sqlite3

app = Flask(__name__)

@app.route('/')
def view():
    con = sqlite3.connect('./test.db')
    cur = con.cursor()
    value = get_DHT()
    t = value[0]
    h = value[1]
    cur.execute("INSERT INTO DHT Values(%f, %f);" % (t, h))
    con.commit()
    datas = []
    params = {}
    cur = con.cursor()
    cur.execute("SELECT * FROM DHT;")
    for row in cur:
        data = {
            "t":row[0],
            "h":row[1]
        }
        datas.append(data)
    print(datas)
    params.update({"datas":datas})
    con.close()
    return render_template("view.html", params=params)


if __name__ == '__main__':
    app.run(debug=True)
