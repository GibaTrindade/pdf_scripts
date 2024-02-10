import pandas as pd

# Ler o arquivo de texto como uma lista de linhas
with open('estagios_contatos.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Remover quebras de linha e linhas em branco
linhas = [linha.strip() for linha in linhas if linha.strip()]

# Criar listas para armazenar os dados
nomes = []
dds = []
telefones = []
horarios = []
# Iterar sobre as linhas para extrair os dados
i = 0
while i < len(linhas):
    # Verificar se a linha atual contém um nome
    if not linhas[i].isdigit():
        nomes.append(linhas[i])
        # Verificar se há uma próxima linha com telefone e horário
        if i + 1 < len(linhas) and not linhas[i + 1].isdigit():
            telefone_horario = linhas[i + 1].split(maxsplit=1)
            ddd = telefone_horario[0][:2]  # Pegar os dois primeiros caracteres como DDD
            dds.append(ddd)
            telefones.append(telefone_horario[0][2:])  # Pegar o restante como número de telefone
            horarios.append(telefone_horario[1])
            i += 1  # Avançar para a próxima linha
        else:
            dds.append(None)
            telefones.append(None)
            horarios.append(None)
    i += 1  # Avançar para a próxima linha

# Criar o DataFrame
df = pd.DataFrame({'Nome': nomes, 'DDD': dds, 'Telefone': telefones, 'Horário de Atendimento': horarios})

# Exibir o DataFrame
print(df)
df.to_csv('estagios_contatos.csv', sep=';', encoding='utf-8')
