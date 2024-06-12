from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd

from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import BayesianEstimator


from pgmpy.inference import VariableElimination
from pgmpy.metrics import correlation_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score


G = BayesianNetwork()

mapeo = {-1: 'branch1', 0: 'branch2', 1: 'branch3'}

data = pd.read_csv('datos2.csv', delimiter=',')
print(data.head())

data['B'] = data['B'].replace(mapeo)
print(data)

G.add_edges_from([('A', 'C'), ('B', 'C')])

t = 'A' in G
print(t)

print(len(G))

print(G.nodes())
print(G.edges())
# Definir los nombres de los estados para cada variable
state_names = {
    'A': ['a1', 'a2', 'a3'],
    'B': ['branch1', 'branch2', 'branch3'],  # Asegúrate de que los nombres de los estados de 'B' coincidan con los datos
    'C': ['c1', 'c2']
}

G.fit(data, estimator=BayesianEstimator, prior_type="BDeu", state_names=state_names) # default equivalent_sample_size=5
for cpd in G.get_cpds():
    print(cpd)


# Verificamos si el modelo es válido
print("El modelo es válido?", G.check_model())

# Dibujamos el modelo
#nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold")
#plt.show()

dataNueva = pd.read_csv('datosNuevos2.csv', delimiter=',')
#print(dataNueva.head())

dataNueva['B'] = dataNueva['B'].replace(mapeo)
#print(dataNueva)

#IMPORTANTE. PREPARAR SET DE ENTRENAMIENTO Y SET DE TEST
# HAY 2 FORMAS DE HACERLO
# PRIMERA OPCIÓN
'''
res = dataNueva['C']
train_set = dataNueva[:3]
test_set = dataNueva.loc[3:, :'B']


print(res)
print(res.to_numpy())
print(list(res.to_numpy()))
'''
# SEGUNDA OPCIÓN
train_set = dataNueva[:3]
test_set = dataNueva.loc[3:]
#res = test_set['C']
#predict_data = test_set.copy()
#predict_data.drop('C', axis=1, inplace=True)

#print(train_set)
#print(test_set)
#print(predict_data)
#print(res)

G.fit_update(train_set)

G.save('pruebaDiagrama2.bif', filetype='bif')
