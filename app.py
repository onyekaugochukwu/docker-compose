from flask import Flask, render_template
import psycopg2

app = Flask(__name__, template_folder='.')

def get_firstname():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT firstname FROM students WHERE id = '1'")
    firstname = cur.fetchone()[0]
    cur.close()
    conn.close()
    return firstname

@app.route('/')
def index():
    firstname = get_firstname()
    return render_template('index.html', firstname=firstname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
