import tensorflow as tf

dim_2_tensor = tf.constant([[7, 10],
                            [2, 9]])
print(dim_2_tensor)

print("After expanding")
dim_3_tensor = tf.expand_dims(dim_2_tensor, axis=2)
dim_3_tensor_newaxis = dim_2_tensor[:,:, tf.newaxis]

print("Using tf.expand_dims")
print(dim_3_tensor)

print("Using tf.newaxis")
print(dim_3_tensor_newaxis)

# tf.expand_dims and tf.newaxis as the same result