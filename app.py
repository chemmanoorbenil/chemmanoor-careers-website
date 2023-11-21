from flask import Flask, render_template

app = Flask(__name__)



JOBS = [
    {
        'Id': 1,
        'title': 'Data Analyst',
        'Location': 'Kochi',
        'Salary': 'RS 15,00,000'
    },
    {
        'Id': 2,
        'title': 'Developer',
        'Location': 'Thrissur',
        
    },
    {
        'Id': 1,
        'title': 'Data Sciientity',
        'Location': 'kannur',
        'Salary': 'RS 99,00,000'
    },
    {
        'Id': 1,
        'title': 'Data Analyst',
        'Location': 'USA',
        'Salary': '$ 15,00,000'
    },
]    
@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)