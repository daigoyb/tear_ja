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
        dct_data = {data['cpf']: {
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
        }}
        if os.path.isfile('db/cadastro_ja.json'): # se o arquivo já existir
            with open('db/cadastro_ja.json', 'r', encoding='utf-8') as ja_file:
                json_data = json.load(ja_file)
                ja_file.close()
            json_data.update(dct_data)
            with open('db/cadastro_ja.json', 'w', encoding='utf-8') as ja_file:
                json.dump(json_data, ja_file, ensure_ascii=False, indent=4)
                ja_file.close()
            return 'Cadastrado - doc atualizado'
        else: # se o arquivo não existir
            with open('db/cadastro_ja.json', 'w', encoding='utf-8') as ja_file:
                json.dump(dct_data, ja_file, ensure_ascii=False, indent=4)
                ja_file.close()
            return 'Cadastrado - Arquivo criado'
    return 'nao entrou no post'

@app.route('/get_empregos', methods=['GET'])
def get_empregos():
    if request.method == 'GET':
        habilidades_empresa = []
        interesses_ja = []
        with open('db/cadastro_emp.json', encoding='utf-8') as emp_file, open('db/cadastro_ja.json') as ja_file:
            # comparar habilidades desejadas da empresa e interesses do JA




# Rotas Fluxo Empresa
@app.route('/cadastro_emp', methods=['POST']) #cadastro empresa
def cadastro_emp():
    if request.method == "POST":
        data = request.get_json()
        dct_data = {data['cnpj']: {
                    "name_emp": data['name_emp'],
                    "endereco": data['endereco'],
                    "estado": data['estado'],
                    "vagas": data['vagas'],
                }}
        print(dct_data)
        if os.path.isfile('db/cadastro_emp.json'): #Arquivo não existe
            with open('db/cadastro_emp.json', 'r', encoding='utf-8') as file_empresa:
                json_data = json.load(file_empresa)
                file_empresa.close()
            json_data.update(dct_data)
            with open('db/cadastro_emp.json', 'w', encoding='utf-8') as emp_file:
                json.dump(json_data, emp_file, ensure_ascii=False, indent=4)
                emp_file.close()
            return 'Cadastrado doc empresas atualizado'
        else: #arquivo Existe
            with open('db/cadastro_emp.json', 'w', encoding='utf-8') as emp_file:
                json.dump(dct_data, emp_file, ensure_ascii=False, indent=4)
                emp_file.close()
            return 'Cadastrado doc empresas criado'
    return 'nao entrou no post'

if __name__ == "__main__":
    app.run()
