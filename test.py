# import the Flask library 
from flask import Flask, request 
  
from flask_cors import CORS

# Create the Flask instance and pass the Flask 
# constructor, the path of the correct module 
app = Flask(__name__)

CORS(app)  # Enable CORS for all routes
 

  
  
# Default route added using a decorator, for view function 'welcome' 
# We pass a simple string to the frontend browser 
@app.route('/') 
def welcome(): 
    return "Hello! Let us learn about importance of Exercise!"
  

#post request to get the data from the frontend
@app.route('/summary', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        text = request.form.get('text')
        choice = request.form.get('choice')
        percent = request.form.get('percent')

        print(text)
        print(choice)
        print(percent)

    return "Data received successfully"

# Start with flask web app, with debug as True,# only if this is the starting page 
if(__name__ == "__main__"): 
    app.run(debug=True) 