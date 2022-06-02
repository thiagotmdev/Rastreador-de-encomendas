from twilio.rest import Client
from flask import Flask, render_template, request, redirect
from rastreamento import rastrear

app = Flask('Api_Flask_Hacker_News')
# autenticacao twilio
# pegue suas credenciais: http://twil.io/secure
account_sid = 'SUA SID'
auth_token = 'SEU TOKEN'
client = Client(account_sid, auth_token)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enviado')
def enviado():
    cod_r = request.args.get('cod_r')
    n_cel = request.args.get('n_cel')
    rastrear(cod_r, n_cel)
    return render_template('enviado.html')


app.run(host='0.0.0.0')
