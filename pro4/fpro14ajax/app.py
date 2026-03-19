from flask import Flask, request, render_template,jsonify
import pymysql

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/legacy")
def legacy():
    pass

@app.get("/async")
def async_func():
    pass

@app.get("/fetch")
def fetch_func():
    return render_template("show2.html")

@app.get("/axios")
def axios_func():
    return render_template("show3.html")

@app.get("/api/sangdata")
def sangdata():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "123",
        database = "test",
        charset = "utf8"
    )
    cur = conn.cursor()
    cur.execute("select * from sangdata")
    columns = [col[0] for col in cur.description] # ??
    rows = cur.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    print(result)
    cur.close()
    conn.close()
    
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)