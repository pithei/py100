# Add to this file for the sample app lab

from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "You are calling me from "+ request.remote_addr

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)