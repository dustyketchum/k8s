from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    results.append('Pod: {}'.format(os.environ.get('MY_POD_NAME')))
    results.append('Node: {}'.format(os.environ.get('MY_NODE_NAME')))
    results.append('Namespace: {}'.format(os.environ.get('MY_POD_NAMESPACE')))
    results.append('IP: {}'.format(os.environ.get('MY_POD_IP')))
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
