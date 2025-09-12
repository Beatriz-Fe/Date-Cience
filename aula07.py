import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

dados = pd.DataFrame({
    "Orçamento_Campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes_Anuncio": np.random.randint(2000, 20000, size=100),
    "Vendas": np.random.randint(10, 10000, size=100),
    "Cliques": np.random.randint(100, 20000, size=100)
})

#Pairplot: Visualizar todas as relações
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

#jointplot: Explorar a relação entre duas variáveis
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados, kind="reg")
plt.show()
plt.savefig('jointplot7.png') 

#Lmplot: Visualizar a linha de regressão
sns.lmplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados)
plt.show()
plt.savefig('lmplot7.png')