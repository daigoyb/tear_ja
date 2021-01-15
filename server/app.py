from flask import Flask, request
import time, json
import os.path

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {"time": time.time()}

#rotas fluxo JA
@app.route('/cadastro_ja', methods=['POST']) #cadastro jovem aprendiz
def cadastro_ja():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if os.path.isfile('db/cadastro_ja.json'):
            with open('db/cadastro_ja.json', 'a', encoding='utf-8') as ja_file:
                json.dump({data['cpf']: {
                    "name": data['name'],
                    "endereco": data['endereco'],
                    "estado": data['estado'],
                    "area_interesse": data['area_interesse'],
                    "genero": data['identificacao_genero_sex'],
                    "identificacao_comunidade": {
                        "sn": data['identificacao_comunidade']['sn'],
                        "qual_comunidade": data['identificacao_comunidade']['qual']
                    },
                    "etnia": data['etnia'],
                    "habilidades": data['habilidades']
                }},ja_file, ensure_ascii=False, indent=4)
                ja_file.close()
                return 'Cadastrado'
        else:        
            with open('db/cadastro_ja.json', 'w', encoding='utf-8') as ja_file:
                json.dump({data['cpf']: {
                    "name": data['name'],
                    "endereco": data['endereco'],
                    "estado": data['estado'],
                    "area_interesse": data['area_interesse'],
                    "genero": data['identificacao_genero_sex'],
                    "identificacao_comunidade": {
                        "sn": data['identificacao_comunidade']['sn'],
                        "qual_comunidade": data['identificacao_comunidade']['qual']
                    },
                    "etnia": data['etnia'],
                    "habilidades": data['habilidades']
                }}, ja_file, ensure_ascii=False, indent=4)
                ja_file.close()
                return 'Cadastrado'
    return 'nao entrou no post'