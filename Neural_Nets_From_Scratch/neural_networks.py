# -*- coding: utf-8 -*-
"""Neural_Networks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZSZpiyj9UPigfuFBVmbS6OrWEya5-V6M
"""

import sys
import numpy as np
import matplotlib

print("Python: ", sys.version)
print("Numpy: ", np.__version__)
print("Matplotlib: ", matplotlib.__version__)

#Coding a simple neuron that has inputs, weights, bias
inputs = [1.0, 2.0, 3.0, 2.5]

#Modelling 3 neurons with 3 weights and bias
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output1 = 0
output2 = 0
output3 = 0

for i in range(len(inputs)):
  output1 += inputs[i] * weights1[i]
  output2 += inputs[i] * weights2[i]
  output3 += inputs[i] * weights3[i]

output1 += bias1
output2 += bias2
output3 += bias3

output = output1 + output2 + output3

print([output1, output2, output3])

