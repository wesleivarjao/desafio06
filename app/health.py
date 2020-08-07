from flask import Flask, request, jsonify
from rq import Queue
from flask_sqlalchemy import SQLAlchemy
import redis
import os  

#Variaveis
app= Flask (__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
redis_url = os.getenv('REDISTOGO_URL')


#funcao de teste do sql
def status_db():
    try:
        db.session.query("1").all()
        return 'OK'
    except:
        return 'DOWN'
# teste de conexão do no-sql
try:
    redis_conn = redis.from_url(redis_url)
    nosql='OK'
except:
    nosql='DOWN'
 
#função de teste da fila
def status_fila():
    adic = Queue(0, connection=redis_conn)
    sub = Queue(1, connection=redis_conn)
    resul = adic.count + sub.count
    if resul > 1:
        status = "Fila"
    else:
        status = "OK"
    return status

#rota hello world:
@app.route('/')
def hello_world():
    return 'Vai Corinthians!'

#rota, juntamente com o retorno em json
@app.route('/api')
def status():
    dict_api = {
        'api': 1.2, 
        'dep': { 
        'db-sql': status_db(),
        'no-sql': nosql,
        'fila': status_fila(),
        },
    }
    message ={
        'API': dict_api,
        'Status': 200 
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main___':
    app.run(debug=False)
    print("health run")
