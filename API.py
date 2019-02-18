import json
import csv

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/areamaior')
def areamaior(): # Procura o imóvel com a maior área
    
    with open('Imoveis_3509502.csv', 'r', encoding='utf-8') as csvfile:
        imreader = csv.reader(csvfile, delimiter=';')        

        reader = []

        for row in imreader:
            reader.append(row)

        reader = reader[1:]

        codmaior = 0
        maior = 0

        for row in reader:
            if (float(row[5].replace(',','')) > maior):
                    maior = float(row[5].replace(',',''))
                    codmaior = row[0]
        
    return("A maior área é do imóvel de código " + str(codmaior) + ", que é tem uma área de " + str(maior))

@app.route('/codigo/<cod>') # Digite um código, e você encontrará o nome
def codigo(cod):

    with open('Imoveis_3509502.csv', 'r', encoding='utf-8') as csvfile:
        imreader = csv.reader(csvfile, delimiter=';')

        reader = []

        for row in imreader:
            reader.append(row)

        reader = reader[1:]

        nome = "Teste"        

        for row in reader:
            if cod == row[0]:
                nome = row[1]
                
        return("O imóvel que você procura se chama " + nome)

@app.route('/codigoap/<cod>') # Digite um código, e você encontrará tudo
def codigoap(cod):
    
    with open('Imoveis_3509502.csv', 'r', encoding='utf-8') as csvfile:
        imreader = csv.reader(csvfile, delimiter=';')    

        #mydict = {rows[:7] for rows in imreader}

        #mydict = dict(row[:2] for row in imreader if row)
        
        reader = []
        
        for row in imreader:
            reader.append(row)        
        
        rr = []
        
        for row in reader:
            if cod == row[0]:
                rr = row
                
    return jsonify(CODIGO_DO_IMOVEL=rr[0], DENOMINACAO_DO_IMOVEL=rr[1], CODIGO_MUNICIPIO=rr[2],
                   MUNICIPIO=rr[3], UF=rr[4], AREA_TOTAL=rr[5], TITULAR_CONDICAO_DA_PESSOA=rr[6], PERCENTUAL_DE_DETENCAOO=rr[7])

@app.route('/areamaiorap')
def areamaiorap():
    
    with open('Imoveis_3509502.csv', 'r', encoding='utf-8') as csvfile:
        imreader = csv.reader(csvfile, delimiter=';')        

        reader = []

        for row in imreader:
            reader.append(row)

        reader = reader[1:]

        maior = 0
        rr = []

        for row in reader:
            if (float(row[5].replace(',','')) > maior):
                    maior = float(row[5].replace(',',''))
                    rr = row

    return jsonify(CODIGO_DO_IMOVEL=rr[0], DENOMINACAO_DO_IMOVEL=rr[1], CODIGO_MUNICIPIO=rr[2],
                   MUNICIPIO=rr[3], UF=rr[4], AREA_TOTAL=rr[5], TITULAR_CONDICAO_DA_PESSOA=rr[6], PERCENTUAL_DE_DETENCAOO=rr[7])

if __name__ == '__main__':
    app.run(debug=True)

#Planilha: https://sncr.serpro.gov.br/sncr-web/consultaPublica.jsf;jsessionid=ECqz5EUMnmDbWqTmei+e7v7B.sncr-web2?windowId=f22
