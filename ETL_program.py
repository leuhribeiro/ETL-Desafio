import csv

dados_originais = []

with open(r'C:\Users\leuhr\OneDrive\Área de Trabalho\DIO_Python\ETL-Desafio\dados_originais.csv', 'r') as arquivo_csv:
dados_originais.csv', 'r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        dados_originais.append(linha)


dados_transformados = []

for registro in dados_originais:
    idade_em_meses = int(registro['Idade']) * 12
    registro['Idade_em_Meses'] = idade_em_meses
    dados_transformados.append(registro)

with open('dados_transformados.csv', 'w', newline='') as arquivo_csv:
    cabecalho = ['Nome', 'Idade', 'País', 'Idade_em_Meses']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
    
    escritor_csv.writeheader()
    for registro in dados_transformados:
        escritor_csv.writerow(registro)
