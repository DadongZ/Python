import numpy as np
np.random.seed(1)
w0 = 2*np.random.random((3,1)) - 1

print("iter 1's output is: \n", w0)
training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])
training_out = np.array([[0, 1, 1, 0]]).T

def segmoid(x):
    return 1/(1+np.exp(x))

def segmoid_driv(x):
    return x*(1-x)

#iter1
out1 = segmoid(np.dot(training_inputs, w0))


print("iter 1's output is: \n", out1)

error1 = training_out - out1

print("iter 1's error is: \n", error1)

w1 = np.dot(training_inputs.T, error1 * segmoid_driv(out1))

print("iter 1's weight is: \n", w1)

#iter2

out2 = segmoid(np.dot(training_inputs, w1))
print("iter 2's output is: \n", out2)

error2 = training_out - out2

print("iter 2's error is: \n", error2)

w2 = np.dot(training_inputs.T, error2 * segmoid_driv(out2))

print("iter 2's weight is: \n", w2)
