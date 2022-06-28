import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[0]) * target_output[1] +
         math.log(softmax_output[0]) * target_output[2])


# The same as
loss = math.log(softmax_output[0])
print(loss)