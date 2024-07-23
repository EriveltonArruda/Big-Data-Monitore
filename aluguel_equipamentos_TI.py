from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum
import matplotlib.pyplot as plt

# Iniciar uma sessão Spark
spark = SparkSession.builder.appName("EquipamentosTI").getOrCreate()

# Carregar os dados do Excel usando pandas e convertê-los para um DataFrame Spark
import pandas as pd

file_path = 'aluguel_equipamentos_TI_stylized.xlsx'
pdf = pd.read_excel(file_path, index_col=0)

df = spark.createDataFrame(pdf.reset_index())

# Adicionar uma coluna com o total de equipamentos alugados para cada prefeitura
df = df.withColumn("Total de Equipamentos", 
                   col("Monitores") + col("Computadores") + col("Mouse") + 
                   col("Teclado") + col("Câmeras") + col("Impressoras") + 
                   col("TVs") + col("DVR"))

# Coletar os dados manipulados de volta para um DataFrame pandas para visualização
pdf_result = df.toPandas()

# Gerar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(pdf_result['index'], pdf_result['Total de Equipamentos'], color='skyblue')
plt.xlabel('Prefeituras')
plt.ylabel('Total de Equipamentos Alugados')
plt.title('Total de Equipamentos de TI Alugados por Prefeitura')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico
plt.savefig('aluguel_equipamentos_TI_grafico.png')

# Mostrar o gráfico
plt.show()

# Parar a sessão Spark
spark.stop()