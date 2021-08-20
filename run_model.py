import tensorflow as tf
import time

one_step_model = tf.saved_model.load('models/one_step')

""" start = time.time()
states = None
next_char = tf.constant(['ROMEO:', 'ROMEO:', 'ROMEO:', 'ROMEO:', 'ROMEO:'])
result = [next_char]

for n in range(1000):
    next_char, states = one_step_model.generate_one_step(
        next_char, states=states)
    result.append(next_char)

result = tf.strings.join(result)
end = time.time()
print(result, '\n\n' + '_'*80)
print('\nRun time:', end - start) """

start = time.time()
states = None
next_char = tf.constant(['ROMEO: Juliet is like the'])
result = [next_char]

for n in range(1000):
    next_char, states = one_step_model.generate_one_step(
        next_char, states=states)
    result.append(next_char)

result = tf.strings.join(result)
end = time.time()
print(result[0].numpy().decode('utf-8'), '\n\n' + '_'*80)
print('\nRun time:', end - start)
