from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    students = [
        {"name" : "Alice" ,"score" : 80},
        {"name" : "Bob" ,"score" : 70 },
        {"name": "Charlie","score" : 90}
    ]   
    return render_template('daftar nilai.html',
    students=students
    )
if __name__ == '__main__':
 app.run(debug=True)
