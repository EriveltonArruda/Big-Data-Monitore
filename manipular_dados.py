import pandas as pd

# Carregar a planilha
file_path = 'aluguel_equipamentos_TI_stylized.xlsx'
df = pd.read_excel(file_path, index_col=0)

# Exibir os dados
print("Dados originais:")
print(df)

# Adicionar uma coluna com o total de equipamentos alugados para cada prefeitura
df['Total de Equipamentos'] = df.sum(axis=1)

# Exibir os dados com a nova coluna
print("\nDados com a coluna 'Total de Equipamentos':")
print(df)

# Filtrar prefeituras com mais de 300 equipamentos alugados no total
filtered_df = df[df['Total de Equipamentos'] > 300]

# Exibir as prefeituras filtradas
print("\nPrefeituras com mais de 300 equipamentos alugados no total:")
print(filtered_df)

# Salvar os dados manipulados em um novo arquivo Excel
output_path = 'aluguel_equipamentos_TI_manipulados.xlsx'
df.to_excel(output_path)

print(f"\nDados manipulados foram salvos em: {output_path}")