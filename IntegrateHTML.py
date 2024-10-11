### Integrate HTML with flask
#### HTTP verb Get and Post
##### jinja2 template

'''
(%...%) for statements
{{ }} expressions to print output
{#....#} this is for comments

'''

from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def Welcome() :
    return render_template('index.html')

# Building url Dynamically
@app.route('/results/<int:score>')
def results(score) :
    res = ""
    if(score >= 50) :
        res = "pass"
    else :
        res = "fail"
    exp = {'score' : score, 'res' : res}
    return render_template('results.html', result = exp)

@app.route('/submit', methods = ['POST', 'GET'])
def submit() :
    total_score = 0
    if request.method == 'POST' :
        subject1 = float(request.form['subject1'])
        subject2 = float(request.form['subject2'])
        subject3 = float(request.form['subject3'])
        subject4 = float(request.form['subject4'])
        subject5 = float(request.form['subject5'])
        total_score = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
    
    return redirect(url_for('results', score = total_score))
    
if __name__ == '__main__':
    app.run(debug=True)