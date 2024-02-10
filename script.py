import pandas as pd

# Ler o arquivo de texto como uma lista de linhas
with open('estagios.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Remover quebras de linha e linhas em branco
linhas = [linha.strip() for linha in linhas if linha.strip()]

# Criar uma lista de dicionários para construir o DataFrame
data = []
for linha in linhas:
    partes = linha.split()
    if partes[0] == 'DISCIPLINA':
        continue
    dicionario = {
        'Disciplina': partes[0],
        'Local': ' '.join(partes[1:-3]),
        'Preceptor': partes[-3],
        'Turno': partes[-2],
        'Data': partes[-1]
    }
    data.append(dicionario)

# Criar o DataFrame
df = pd.DataFrame(data)

# Exibir o DataFrame
print(df)
df.to_csv('estagios.csv', sep=';', encoding='utf-8')
