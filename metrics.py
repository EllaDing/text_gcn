import tensorflow as tf
import keras

def masked_softmax_cross_entropy(preds, labels, mask):
    """Softmax cross-entropy loss with masking."""
    print(preds)
    class_weights = tf.constant([[17, 1.0]])
    weights = tf.reduce_sum(class_weights * labels, axis=1)
    loss = tf.nn.softmax_cross_entropy_with_logits(logits=preds, labels=labels)
    #loss = keras.losses.binary_crossentropy(labels, preds) 
    loss *= weights
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    loss *= mask
    return tf.reduce_mean(loss)


def masked_accuracy(preds, labels, mask):
    """Accuracy with masking."""
    correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(labels, 1))
    print(tf.contrib.metrics.f1_score(labels, preds))
    accuracy_all = tf.cast(correct_prediction, tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    accuracy_all *= mask
    return tf.reduce_mean(accuracy_all)
