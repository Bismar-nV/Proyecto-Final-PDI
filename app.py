from flask import Flask, render_template, request, jsonify
import random


app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True)
