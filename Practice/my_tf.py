import tensorflow as tf

# Define constants
a = tf.constant(2)
b = tf.constant(3)

# Define operations
add = tf.add(a, b)
mul = tf.multiply(a, b)

# Print the results
print("Addition result:", add.numpy(),add)
print("Multiplication result:", mul.numpy(),mul)
