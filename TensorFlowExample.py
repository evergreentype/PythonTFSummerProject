# To compile:
## Open CommandPrompt or PowerShell
## Navigate to the PythonTFSummerProject folder using the "cd" command
## Type to compile: python TensorFlowExample.py

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))