from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'company':'ABC Corp.',
        'location':'Banglore',
        'salary':'Rs. 15,00,000'
    },
    {
        'id':2,
        'title':'Backend Engineers',
        'company':'ABC Corp.',
        'location':'Pune',
        'salary':'Rs. 12,00,000'
    },
    {
        'id':3,
        'title':'Data Scientist',
        'company':'ABC Corp.',
        'location':'New York',
        'salary':'Rs. 12,00,000'
    },
    {
        'id':4,
        'title':'Data Scientist',
        'company':'ABC Corp.',
        'location':'New York',
    }
]
@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')