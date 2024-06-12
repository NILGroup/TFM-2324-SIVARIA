import constants
'''
for e,t in constants.BAYES_NETWORK_STATE_NAMES.items():
    index = 0
    #print(t)
    newStr = e.replace(' ', '_').replace('/','_').replace('-','_')
    print(newStr.upper() + '_DECODE = {')
    for value in t:
        print('\t\'' + value + '\':' + str(index) + ',')
        index += 1
    
    print('}')
    print('\n')
'''
'''
print('BAYES_NETWORK_STATE_NAMES = {')
for e,t in constants.BAYES_NETWORK_STATE_NAMES.items():
    tmp = []
    index = 0
    for values in t:
        tmp.append(str(index))
        index += 1

    my_string = ','.join(tmp)
    print('\t\'' + e + '\':['+ my_string +'],')

print('}')
'''

'''
# In python 3.x cPickle is not available
import pickle
import random

# A custom class to demonstrate pickling 
class ModelTrainer:
	def __init__(self) -> None:
		self.weights = [0,0,0]
	
	def train(self):
		for i in range(len(self.weights)):
			self.weights[i] = random.random()
	
	def get_weights(self):
		return self.weights

# Create an object 
model = ModelTrainer()

# Populate the data
model.train()

print('Weights before pickling', model.get_weights())

# Open a file to write bytes
p_file = open('model.pkl', 'wb')

# Pickle the object
pickle.dump(model, p_file)
p_file.close()

# Deserialization of the file
file = open('model.pkl','rb')
new_model = pickle.load(file)

print('Weights after pickling', new_model.get_weights())
'''
'''
import sklearn.metrics as sm
from sklearn.utils import all_estimators

# Model evaluation
name_m = []
precise = []
estimator = all_estimators(type_filter="classifier")
for name, get_model in estimator:
    try:
        model = get_model()
        model.fit(train_x, train_y)
        predict_y = model.predict(test_x)
        prec = sm.precision_score(test_y, predict_y)
        name_m.append(name)
        precise.append(prec)
    except Exception as e:
        print("Unable to import model", e)
'''