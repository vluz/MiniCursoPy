#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import subprocess
import re


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def code():
    """
    Trata as solicitações de código recebidas.
    Se o método da solicitação for POST, executa o código fornecido e retorna a saída.
    Se o método da solicitação for GET, fornece um código padrão a ser executado.
    """
    if request.method == 'POST':
        # Obtém o código do formulário da solicitação
        code = request.form['pycode']
        
        # Escreve o código em um arquivo
        f = open("onlinecode.py", "w")
        f.write(code)
        f.close()
        
        # Executa o código usando subprocess
        pipe = subprocess.run(["python", "onlinecode.py"], capture_output=True)

        # Processa a saída com base no código de retorno
        if pipe.returncode == 0:
            # Processa a saída padrão
            codeoutput = re.sub('[^A-Za-z0-9().,\n\t ]+-:;#$%=_', '',pipe.stdout.decode('utf-8'))
            result={"code":code,"codeoutput":codeoutput, "env":"/"}
            return render_template('code.html',result=result)
        else:
            # Processa o erro padrão
            codeoutput = re.sub('[^A-Za-z0-9().,\n\t ]+-:;#$%=_', '',pipe.stderr.decode('utf-8'))
            result={"code":code,"codeoutput":codeoutput, "env":"/"}
            return render_template('code.html',result=result)

    if request.method == 'GET':
        # Fornece um código padrão a ser executado
        result={"code":"print('Hello World')","codeoutput":"", "env":"/"}
        return render_template('code.html',result=result) 

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
