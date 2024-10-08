import tensorflow as tf

my_tensor = tf.constant([[10, 3],
                         [9, 6]])
print("my_tensor")
print(my_tensor)

print("add 10")
print(tf.add(my_tensor, 10))

print("substract 10")
print(tf.subtract(my_tensor, 10))

print("plus 2")
print(tf.multiply(my_tensor, 2))

print("divide 10")
print(tf.divide(my_tensor, 10))
