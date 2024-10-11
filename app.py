from flask import Flask

### create a WSGI application - > need to communicate beetwen web server and web page
app = Flask(__name__) # 

# decorator - > arguments :  1. rule 2. options
# rule is the url where i have to go (web page) 
@app.route('/')
# whenever I go into the page (inside the rule) this functions is triggered automatically.
def welcome():
    return "Welcome to my youtube channel"




# starting point of program
if __name__ == '__main__': 
    app.run(debuge=True)
    # Here you can pass debug = True for automatically restart the web page.
    
    