"""
sudo apt update
sudo apt -y install python python-pip
sudo pip install flask

sudo ufw allow 8080
Rules updated
Rules updated (v6)

sudo python sample-app.py

http://0.0.0.0:8080



# Sample app web site walk-through
Now create a file in the templates directory called index.html and add the following code:

<html>
<head>
    <title>Sample app</title>
    <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
    <h1>You are calling me from {{request.remote_addr}}</h1>
</body>
</html>


We also need to create the static/style.css file:

We also need to create the static/style.css file:

Now we need to adjust the sample-app.py script so that it renders the template. 
To do that, open sample-app.py and make the following changes:

Now we need to adjust the sample-app.py script so that it renders the template.
 To do that, open sample-app.py and make the following changes:
 
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)

"""


# Add to this file for the sample app lab

from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "You are calling me from "+ request.remote_addr

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)