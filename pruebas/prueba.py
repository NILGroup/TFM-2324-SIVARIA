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

data = pd.read_csv('datos.csv', delimiter=',')
print(data.head())

data['B'] = data['B'].replace(mapeo)
print(data)

G.add_edges_from([('A', 'C'), ('B', 'C')])

t = 'A' in G
print(t)

print(len(G))

print(G.nodes())
print(G.edges())
'''
# Primera posible implementación

A_cpds = TabularCPD(variable='A', evidence=[],
           cardinality={'A': 3, 'B': 3, 'C': 2},
           state_names={'A': ['a1', 'a2', 'a3'],
                        'B': [-1, 0, 1],
                        'C': ['c1', 'c2']})

B_cpds = TabularCPD(variable='B', evidence=[],
           cardinality={'A': 3, 'B': 3, 'C': 2},
           state_names={'A': ['a1', 'a2', 'a3'],
                        'B': [-1, 0, 1],
                        'C': ['c1', 'c2']})

C_cpds = TabularCPD(variable='C', evidence=['A', 'B'],
           cardinality={'A': 2, 'B': 2, 'C': 2},
           state_names={'A': ['a1', 'a2', 'a3'],
                        'B': [-1, 0, 1],
                        'C': ['c1', 'c2']})
'''
'''
# Segunda posible implementación
cpd_A = TabularCPD(variable='A', variable_card=3, values=[])
cpd_B = TabularCPD(variable='B', variable_card=3, values=[])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[],
                   evidence=['A', 'B'], evidence_card=[3, 3])

G.add_cpds(cpd_A, cpd_B, cpd_C)
'''
# Definir los nombres de los estados para cada variable
state_names = {
    'A': ['a1', 'a2', 'a3'],
    'B': ['branch1', 'branch2', 'branch3'],  # Asegúrate de que los nombres de los estados de 'B' coincidan con los datos
    'C': ['c1', 'c2']
}

#print(BayesianEstimator.get_parameters())

print('PRIMER FIT\n')
G.fit(data, state_names=state_names) # default equivalent_sample_size=5
for cpd in G.get_cpds():
    print(cpd)
'''
print('SEGUNDO FIT\n')
G.fit(data, estimator=MaximumLikelihoodEstimator, state_names=state_names) # default equivalent_sample_size=5
for cpd in G.get_cpds():
    print(cpd)
'''

print('TERCER FIT\n')
G.fit(data, estimator=BayesianEstimator, prior_type="BDeu", state_names=state_names) # default equivalent_sample_size=5
for cpd in G.get_cpds():
    print(cpd)


# Verificamos si el modelo es válido
print("El modelo es válido?", G.check_model())

# Dibujamos el modelo
#nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold")
#plt.show()

dataNueva = pd.read_csv('datosNuevos.csv', delimiter=',')
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
res = test_set['C']
predict_data = test_set.copy()
predict_data.drop('C', axis=1, inplace=True)

print(train_set)
print(test_set)
print(predict_data)
print(res)



G.fit_update(train_set)
y_pred=G.predict(predict_data)

print(y_pred)
print(y_pred.values)
print(y_pred.values.ravel())
print(list(y_pred.values.ravel()))
pred = list(y_pred.values.ravel())
'''
G.fit_update(dataNueva)
for cpd in G.get_cpds():
    print(cpd)
'''
model_infer = VariableElimination(G)

# EL INFER ES COMO HACER QUERIES. BUSCAR LA PROBABILIDAD DE QUE OCURRA UNA VARIABLE DADO UNA SERIE DE EVIDENCIAS
# SIN AÑADIR EVIDENCIAS = WHERE CLAUSE
#results = model_infer.query(variables=['C'])
# CON EVIDENCIAS = WHERE CLAUSE
#results = model_infer.query(variables=['C'], evidence={'A':'a1'})
#print(results)

#fscore,accuracy,precision,recall=calscore(res,pred)

fscore = correlation_score(G, test_set, test="chi_square", score=f1_score, significance_level=0.05)
print(fscore)
acc_score = correlation_score(G, test_set, test="chi_square", score=accuracy_score, significance_level=0.05)
print(acc_score)
rec_score = correlation_score(G, test_set, test="chi_square", score=recall_score, significance_level=0.05)
print(rec_score)
prec_score = correlation_score(G, test_set, test="chi_square", score=precision_score, significance_level=0.05)
print(prec_score)

G.save('pruebaDiagrama.bif', filetype='bif')
