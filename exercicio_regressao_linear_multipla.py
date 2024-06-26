# -*- coding: utf-8 -*-
"""Exercicio_Regressao_Linear_Multipla.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1475G1Sb1H-KFnMNn3TFp3IOr9AdlH63S
"""

import numpy as np
import matplotlib.pyplot as plt

Dados = np.genfromtxt('dados_descarbonizacao.csv', delimiter=',', skip_header=1)

y = Dados[:,[-1]]
x = Dados[:, 0:4]

X = np.hstack((np.ones((len(x), 1)),x))
betas,res,_, _= np.linalg.lstsq(X, y,rcond=None)

