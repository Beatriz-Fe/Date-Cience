import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Faz a leitura do arquivo csv a partir de uma URL ou Arquivo
dados = pd.read_csv ('./aula08/desmatamento_prodes.csv')

#Exibe os dados
print (dados)

print ('-+-' * 50)

#Exibindo a matriz de correlação de pearson
#Fornecendo uma pré-analise dos dados para encontrar
#correlações fortes positivas/negativas ou sem correlação
print(dados.corr().round(2))

sns.pairplot(dados)
plt.show()
plt.savefig('./aula08/pairplot.png')

#Fazendo analise individual para correlação forte positiva
#x -> Variavel dependente: Mato Grosso
#Y -> Variavel descritiva: Rondonia
sns.lmplot(data=dados, x="mato_grosso", y="rondonia")
plt.show()

plt.savefig('./aula08/lmplot-positivo.png')

sns.jointplot(data=dados, x="referencia", y="tocantins", kind='reg')
plt.show()
plt.savefig('./aula08/jointplot-negativo.png')