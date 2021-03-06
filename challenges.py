from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Task 2 : Dynamic URLS
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return "Welcome to " + course_name

#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using POST method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form') #the url you type in localhost:5000/form
def formView():
    html_form = '''
    <html>
    <body>
    <form method = "GET" action ="http://localhost:5000/result">
    Ingredient :
    <input type= "text" name="ingredient" ></input>
    <input type = "submit" name= "submit"></input>
    </form>
    </body>
    </html>
    '''
    return html_form

#Task 3.2 : Processing Form Data
#run program again and enter localhost:5000/form
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    if request.method == "GET":
        ingg = request.args.get("ingredient")
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results
    params = {}
    params["i"] = ingg
    response = requests.get("http://www.recipepuppy.com/api/", params = params)
    response_json = json.loads(response.text)
    #convert to a string
    response_str = str(response_json)
    return response_str


if __name__ == '__main__':
    app.run(debug=True)
