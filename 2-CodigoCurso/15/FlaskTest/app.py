from flask import Flask, render_template, request
import subprocess
import re


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def code():
    if request.method == 'POST':
        code = request.form['pycode']
        f = open("onlinecode.py", "w")
        f.write(code)
        f.close()
        pipe = subprocess.run(["python", "onlinecode.py"], capture_output=True)

        if pipe.returncode == 0:
            codeoutput = re.sub('[^A-Za-z0-9().,\n\t ]+-:;#$%=_', '',pipe.stdout.decode('utf-8'))
            result={"code":code,"codeoutput":codeoutput, "env":"/"}
            return render_template('code.html',result=result)
        else:
            codeoutput = re.sub('[^A-Za-z0-9().,\n\t ]+-:;#$%=_', '',pipe.stderr.decode('utf-8'))
            result={"code":code,"codeoutput":codeoutput, "env":"/"}
            return render_template('code.html',result=result)

    if request.method == 'GET':
        result={"code":"print('Hello World')","codeoutput":"", "env":"/"}
        return render_template('code.html',result=result) 

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
