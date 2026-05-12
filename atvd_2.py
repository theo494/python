from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Theo Silva</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    padding: 40px 20px;
                }
                .container {
                    background: #fff;
                    max-width: 600px;
                    width: 100%;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                    text-align: center;
                }
                h2 {
                    color: #3498db;
                    font-size: 1.2rem;
                    margin-top: 25px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
                li {
                    margin-bottom: 10px;
                    padding: 8px;
                    background: #f9f9f9;
                    border-left: 4px solid #3498db;
                    border-radius: 4px;
                }
                strong {
                    color: #2c3e50;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Currículo</h1>

                <h2>Informações Pessoais</h2>
                <ul>
                    <li><strong>Nome:</strong> Theo Silva</li>  
                    <li><strong>Email:</strong> 22401130@aluno.cotemig.com.br</li>
                    <li><strong>Telefone:</strong> (31) 1234-1234</li>
                </ul>

                <h2>Experiências Acadêmicas</h2>
                <ul>
                    <li><strong>Colégio:</strong> Cotemig</li>
                    <li><strong>Série:</strong> 3º Ano</li>
                    <li><strong>Período:</strong> Manhã</li>
                </ul>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
