### Building url Dynamically
##### FLask variable Rules and URL Building


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Welcome() :
    return "Welcome to my channel"

# Building url Dynamically
@app.route('/success/<int:score>')
def success(score) :
    return "The person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score) :
    return "The person has failed and the marks is " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    results = ""
    if marks < 50 :
        results = 'fail'
    else:
        results = 'success'
    return redirect(url_for(results, score=marks))
        
        
if __name__ == '__main__':
    app.run(debug=True)