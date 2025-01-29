import tensorflow as tf

# Define TensorFlow operations
x = tf.keras.Input(shape=(), dtype=tf.float32, name='x')
y = tf.keras.Input(shape=(), dtype=tf.float32, name='y')
z = tf.add(x, y, name='z')

# Create a summary writer to write the graph
with tf.summary.create_file_writer('logs').as_default():
    tf.summary.trace_on(graph=True, profiler=True)
    # Initialize TensorFlow session
    func = tf.keras.backend.function([x, y], z)
    result = func([1, 2])
    tf.summary.trace_export(name='graph', step=0, profiler_outdir='logs')
    print("Result:", result)
