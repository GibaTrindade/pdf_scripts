import pdfplumber
import pandas as pd

# Substitua 'caminho/do/seu/arquivo.pdf' pelo caminho do seu arquivo PDF
with pdfplumber.open('lotacaoA7.pdf') as pdf:
    # Acessa a página desejada
    page = pdf.pages[0]
    
    # Extrai todas as tabelas da página
    tables = page.extract_tables()

    # Itera sobre todas as tabelas extraídas
    for i, table in enumerate(tables):
        # A primeira linha é tratada como cabeçalho
        if i == 0:
            header = table[4]
            data = table[5:]
            dataframe = pd.DataFrame(data, columns=header)
        else:
            header = table[0]
            data = table[1:]
            # Converte a tabela em um DataFrame do Pandas
            dataframe = pd.DataFrame(data, columns=header)
            # Remove as linhas onde a coluna 'DISCIPLINA' tem o valor 'DISCIPLINA'
            dataframe = dataframe[dataframe['DISCIPLINA'] != 'DISCIPLINA']
            dataframe.to_csv('estagioA7.csv', index=False)

        

        # Imprime o DataFrame
        print(f"Tabela {i + 1}:")
        print(dataframe)