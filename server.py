import os
import res.setup as setup
import json

#This may not be installed hence setup is run
setup.setup()
import requests
from flask import Flask, request, render_template, send_from_directory

# Create an instance of a Flask class
app = Flask(__name__)
# Auto-reload the server when HTML files are changed
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data",  methods=('GET', 'POST'))
def data():
    jsonstring = request.args.get('id')
    # Parse the JSON string into a JSON object
    JsonConfig = json.loads(jsonstring)
    print("received data: " + str(JsonConfig))
    

    '''
    # Save the JSON object as a JSON file
    with open('JsonConfig.json', 'w') as outfile:
        json.dump(JsonConfig, outfile) 
    
    '''

    return ('All OK!', 200)

@app.route("/datatest")
def datatest():
    test_data = {'testKey': 'testValue',"testKey2": "testValue2"}
    test_data = json.dumps(test_data)
    r = requests.post("http://localhost:5000/data?id="+test_data, data={'number': 12524, 'type': 'issue', 'action': 'show'})
    print(r.status_code, r.reason)
    return ('', 204)

#404
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404,page_not_found)
    app.run()
