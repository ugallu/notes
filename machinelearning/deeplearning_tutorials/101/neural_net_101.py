import numpy as np

# sigmoid
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

#input in matrix
# training set: 4 input data for 3 input neuron
X = np.array([[0,1,0,1],
              [0,1,1,1],
              [1,1,0,1],
              [0, 0, 1, 1],
              [1, 0, 0, 1],
              [0, 0, 1, 1],
              [1, 0, 0, 1],
              [1,1,1,1]])

# 4 output data
y = np.array([[1],
             [1],
             [1],
             [0],
             [1],
             [0],
             [0],
             [0]])

# to be repeatable, we use deterministic speudorandom nums
np.random.seed(123)

# synapses
# connection between layers
# 3 input maps to 4 hidden maps to 1 output
syn0 = 2*np.random.random((4,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

# train
for j in xrange(60000):

    # layer values after activation function
    layer0 = X
    layer1 = nonlin(np.dot(layer0,syn0))
    layer2 = nonlin(np.dot(layer1, syn1))

    # diff between output and prediction
    layer2_error = y - layer2

    # error mean to debug
    if(j % 10000) == 0:
        print "Error:" + str(np.mean(np.abs(layer2_error)))

    layer2_delta = layer2_error*nonlin(layer2, deriv=True)

    layer1_error = layer2_delta.dot(syn1.T)

    layer1_delta = layer1_error*nonlin(layer1, deriv=True)

    #update weight
    syn1 += layer1.T.dot(layer2_delta)
    syn0 += layer0.T.dot(layer1_delta)

print "Output after training"
print layer2

