import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class cnn_model(keras.Model):

    def __init__(self, vocab_size=27091, emb_dim=128, nb_filters=50, ffn_units=512, nb_classes=2,
                 dropout_rate=0.2, training=True, name="cnn_model"):
        super(cnn_model, self).__init__(name=name)

        self.embedding = layers.Embedding(vocab_size, emb_dim)

        self.bigram = layers.Conv1D(filters=nb_filters, kernel_size=2, padding='same', activation='relu')

        self.trigram = layers.Conv1D(filters=nb_filters, kernel_size=3, padding='same', activation='relu')

        self.fourgram = layers.Conv1D(filters=nb_filters, kernel_size=4, padding='same', activation='relu')
        
        self.pool = layers.GlobalMaxPool1D()

        self.dense_1 = layers.Dense(units=ffn_units, activation='relu')
        self.dropout = layers.Dropout(rate=dropout_rate)

        if nb_classes == 2:
            self.last_dense = layers.Dense(units=1, activation='sigmoid')
        else:
            self.last_dense = layers.Dense(units=nb_classes, activation='softmax')

    def call(self, inputs, training):

        x = self.embedding(inputs)
        x_1 = self.bigram(x)
        x_1 = self.pool(x_1)
        x_2 = self.trigram(x)
        x_2 = self.pool(x_2)
        x_3 = self.fourgram(x)
        x_3 = self.pool(x_3)

        merged = tf.concat([x_1, x_2, x_3], axis=-1)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output
