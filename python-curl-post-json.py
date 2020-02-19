#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #

try:
    import os
    import json
    import pycurl
    from io import BytesIO

except Exception as E:
    print('001 - Erro ao Importar Bibliotecas: ' + str(E))


# - - - - - - - - - - - - - - [ Bloco de Execucao (1o) ] - - - - - - - - - - - - - - #

try:
    # Define as Variaveis
    codigoMailing = '10001'
    nome = 'John Doe'
    origem = 'Teste'
    telefone1 = '11912345678'  # Celular
    userfield1 = '12345678910'  # CPF

    # Monta o JSON do caso atual que sera enviado via CURL
    sendJSON = {
        "codigoMailing": str(codigoMailing),
        "pessoas":
            [
                {
                    "nome": str(nome),
                    "identificacao": "",
                    "origem": str(origem),
                    "agendamento":
                        {
                            "agendamento": "",
                            "intervalo":
                                {
                                    "horarioInicio": "",
                                    "horarioFim": ""
                                },
                            "data":
                                {
                                    "data": "",
                                    "horario": ""
                                }
                        },
                    "dataValidade": "",
                    "telefones":
                        {
                            "telefone1": str(telefone1),
                            "telefone2": "",
                            "telefone3": "",
                            "telefone4": "",
                            "telefone5": "",
                            "telefone6": "",
                            "telefone7": "",
                            "telefone8": "",
                            "telefone9": "",
                            "telefone10": "",
                            "telefone11": "",
                            "telefone12": ""
                        },
                    "userFields":
                        {
                            "userfield1": str(userfield1),
                            "userfield2": "",
                            "userfield3": "",
                            "userfield4": "",
                            "userfield5": "",
                            "userfield6": "",
                            "userfield7": "",
                            "userfield8": "",
                            "userfield9": "",
                            "userfield10": ""
                        }
                }
            ]
    }


    # Converte a Variavel em um Objeto JSON:
    sendJSON = json.dumps(sendJSON)

    buffer = BytesIO()  # Variavel que guardara o Response do CURL

    # Executa o CURL
    c = pycurl.Curl()
    c.setopt(c.URL, "teste.oracle.discador.com.br:8090/api/discador/V2/adicionar/testetoken")  # URL da API para a qual sera feito o Post via CURL
    c.setopt(c.SSL_VERIFYHOST, 0)  # Nao verificara o Host
    c.setopt(c.POST, 1)  # Sera um Post
    c.setopt(c.HTTPHEADER, ["Content-Type: application/json", "Authorization: Bearer testetoken"])  # Define o Tipo de Dado e a Autenticacao do Post
    c.setopt(c.POSTFIELDS, sendJSON)  # JSON que sera enviado
    c.setopt(c.WRITEDATA, buffer)  # Variavel na qual sera escrita o Response do Post via CURL
    c.perform()  # Executa o CURL
    c.close()


    # Verifica se ocorreu Sucesso ou Falha
    if json.loads(buffer.getvalue().decode('UTF-8'))['message'] == 'Sucesso':
        print(json.loads(buffer.getvalue().decode('UTF-8')))

except Exception as E:
    print('\n002 - Erro ao executar o Post via CURL.\nsendJSON: ' + str(sendJSON) + "\nErro: " + str(E))

