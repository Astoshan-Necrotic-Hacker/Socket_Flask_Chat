from flask import Flask, render_template, url_for, request
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
    return render_template('index.html')

    if '__main__' == __name__:
        app.run(debug=True, host='0.0.0.0')
        if request.method == 'POST':
            msg_to_send = request.form['text_box']
            #subprocess.run(f"python3 client.py {msg_to_send}")
            return render_template('index.html', msg_to_send)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
