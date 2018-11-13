import tensorflow as tf
import keras

def masked_softmax_cross_entropy(preds, labels, mask):
    """Softmax cross-entropy loss with masking."""
    print(preds)
    class_weights = tf.constant([[1, 15.03964]])
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
    accuracy_all = tf.cast(correct_prediction, tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    accuracy_all *= mask
    predicted = tf.cast(tf.argmax(preds, 1), tf.float32)
    actual = tf.cast(tf.argmax(labels, 1), tf.float32)
    TP = tf.count_nonzero(predicted * actual * mask)
    TN = tf.count_nonzero((predicted - 1.0) * (actual - 1.0) * mask)
    FP = tf.count_nonzero(predicted * (actual - 1.0) * mask)
    FN = tf.count_nonzero((predicted - 1.0) * actual * mask)
    precision = tf.divide(TP, TP + FP)
    recall = tf.divide(TP, TP + FN)
    f1_score = f1 = tf.divide(2 * precision * recall, precision + recall)
    return tf.reduce_mean(accuracy_all), precision, recall, f1_score

