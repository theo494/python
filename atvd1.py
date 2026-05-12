from flask import Flask

app = Flask(__name__) 
@app.route('/decorator') 
def explicação():
    return 'É um padrão de projeto estrutural que permite adicionar novas funcionalidades, comportamentos ou responsabilidades a um objeto, função ou classe existente de forma dinâmica, sem modificar seu código-fonte original.' 

if __name__ == '__main__':
    app.run(debug=True)