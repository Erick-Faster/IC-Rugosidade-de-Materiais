# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:52:24 2019

@author: erick
"""

import pandas as pd
base = pd.read_excel('resultados.xlsx', encoding = 'ISO-8859-1')

contagem = base.iloc[:,0].values
reais = base.iloc[:,1].values
previstos = base.iloc[:,2].values

import matplotlib.pyplot as plt
    
plt.title('ANN')
plt.xlabel('Testes')
plt.ylabel('Rugosidade Superficial Média (Ra)')

plt.plot(contagem, reais, color='black')
plt.plot(contagem, previstos, color='red')

plt.scatter(contagem, reais, color='black')
plt.scatter(contagem, previstos, color='red')

plt.legend(['Dados Reais', 'Dados Previstos'], loc=0)

plt.axis((0,18,0,6))

plt.savefig('ANN_cont.jpeg')

plt.show()