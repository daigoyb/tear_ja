from flask import Flask, request
import pprint, json
import os.path

app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)

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
            "habilidades": data['habilidades'],
            "vaga_preferencia": data['vaga_preferencia']
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
    if request.method == 'GET' and request.args['id']:
        referencias_emprego = {}
        interesses_ja = {}
        ja_id = request.args['id']
        with open('db/cadastro_emp.json', encoding='utf-8') as emp_file, open('db/cadastro_ja.json') as ja_file:
            # comparar habilidades desejadas da empresa e interesses do JA
            empresas = json.load(emp_file)
            list_ja = json.load(ja_file)
            for key in empresas: # pegar o cnpj
                referencias_emprego[key] = empresas[key]["vagas"]
            ja = list_ja[ja_id]
            hab_int = ja['habilidades'] + ja['area_interesse']
            interesses_ja[ja_id] = {
                "interesse": hab_int,
                "vaga_preferencia": ja['vaga_preferencia'],
                "identificacao": ja['identificacao_comunidade'],
                "identificacao_gen_sex": ja['genero'],
                "etnia": ja['etnia']
            }
            emp_file.close()
            ja_file.close()
        ja_ref = interesses_ja[ja_id]
        send_data = {}
        for referencia in referencias_emprego:
            for i in range(len(referencias_emprego[referencia])):
                vaga = referencias_emprego[referencia][i]
                id_vaga = referencia + '_' + str(i)
                send_data[id_vaga] = {
                    'nome_vaga': vaga['nome_vaga'],
                    'desc_vaga': vaga['descricao_vaga'], 
                    'points': 0
                }
                for pub_esp in vaga['publico_especifico']:
                    if pub_esp ==  ja_ref['identificacao_gen_sex'] or pub_esp == ja_ref['identificacao']['qual_comunidade'] or pub_esp == ja_ref['etnia']:
                        send_data[id_vaga]['points'] += 50
                        break
                for interesse in ja_ref['interesse']:
                    for habilidades in vaga['habilidades']:
                        if interesse == habilidades:
                            send_data[id_vaga]['points'] +=25
                            break
                for tipo_vaga in vaga['tipo_vaga']:
                    if ja_ref['vaga_preferencia'] == tipo_vaga:
                        send_data[id_vaga]['points'] += 25
                        break      
        return send_data            



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
