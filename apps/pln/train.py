import logging
import os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger('tensorflow').disabled = True

import ast
from apps.pln.clean.clean_text import clean_text, clean_text2
from apps.pln.dm.CnnModel import CnnModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import tensorflow_datasets as tfds
import tensorflow as tf
import pandas as pd
import numpy as np
import spacy as sp
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

cols = ['sentiment', 'id', 'text']


def train():
    print("--- train ---")
    train_data = pd.read_csv('apps/pln/data/trainingandtestdata/train.csv',
                             header=None, names=cols, engine='python',
                             encoding='utf8')
    return train_data


def test_data():
    print("--- test data ---")
    test_data = pd.read_csv("apps/pln/data/trainingandtestdata/test.csv",
                            header=None, names=cols, engine="python",
                            encoding='utf8')
    return test_data


def data_drop(data):
    print("--- data drop cols ---")
    data.drop(['id'], axis=1, inplace=True)
    return data


def data_label(y):
    print("--- data labels ---")
    data_labels = y
    data_labels[data_labels == 4] = 1
    return data_labels


def save_tt(data_clean):
    print("--- salve tt ---")
    with open('apps/pln/services/save_tt.txt', 'w') as file:
        file.write(str(data_clean))


def data_clean_text(X):
    print("--- data clean tt ---")
    nlp = sp.load('pt_core_news_sm')

    data_clean = [clean_text2(clean_text(tweet), nlp) for tweet in X]
    return data_clean


def token(data_clean):
    print("--- token ---")
    tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(data_clean, target_vocab_size=2**16)
    vocab_fname = "apps/pln/services/ttVocab"
    tokenizer.save_to_file(vocab_fname)
    return tokenizer


def max_len_data_inputs(data_inputs):
    print("--- max len data inputs ---")
    max_len = max([len(sentence) for sentence in data_inputs])
    return max_len


def data_inputs_pad_sequences(data_inputs, max_len):
    print("--- data_inputs pad sequences ---")
    data_inputs = tf.keras.preprocessing.sequence.pad_sequences(
        data_inputs, value=0, padding='post', maxlen=max_len)
    return data_inputs


def data_input(tokenizer, data_clean):
    print("-- data input --")
    data_inputs = [tokenizer.encode(sentence) for sentence in data_clean]
    return data_inputs, tokenizer


def train_test(data):
    print("--- train test ---")
    X = data.iloc[:, 1].values
    y = data.iloc[:, 0].values

    # trabalhando so com 15% da base de 1.6m, (drop 85 da base)
    test_size = 0.05
    # stratify, amostram estratificada, mandento a proporção,
    #  (pagina 43 livro)
    X, _, y, _ = train_test_split(X, y, test_size=test_size, stratify=y)
    return X, y


def list_txt_data_clean():
    print("-- list txt data clean ---")
    with open('apps/pln/services/save_tt.txt', 'r') as data:
        data_list = ast.literal_eval(data.read())
    return data_list


def main():
    print("-- main --")
    data = train()
    data = data_drop(data)
    X, y = train_test(data)

    data_labels = data_label(y)

    data_clean = data_clean_text(X)
    save_tt(data_clean)
    data_clean = list_txt_data_clean()

    tokenizer = token(data_clean)
    vocab_fname = "apps/pln/services/ttVocab"
    tokenizer = tfds.deprecated.text.SubwordTextEncoder.load_from_file(vocab_fname)

    data_inputs, tokenizer = data_input(tokenizer, data_clean)
    max_len = max_len_data_inputs(data_inputs)
    data_inputs = data_inputs_pad_sequences(data_inputs, max_len)

    X_train, X_test, y_train, y_test = train_test_split(data_inputs, data_labels, test_size=0.2, stratify=data_labels)
    print(f"data labels: {data_labels}")
    print(f"len test {len(X_test)} --- {len(y_test)}")

    vocab_size = tokenizer.vocab_size
    emb_dim = 200
    nb_filters = 100
    ffn_units = 256
    batch_size = 124
    nb_classes = len(set(y_train))
    dropout_rate = 0.2
    nb_epochs = 1

    CnnModel = CnnModel(vocab_size=vocab_size, emb_dim=emb_dim, nb_filters=nb_filters, ffn_units=ffn_units, nb_classes=nb_classes, dropout_rate=dropout_rate)

    if nb_classes == 2:
        CnnModel.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    else:
        print("--- mais de 2 classes")
        CnnModel.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    CnnModel.fit(X_train, y_train, batch_size=batch_size, epochs=nb_epochs, verbose=1, validation_split=0.10)

    print("-- evaluate --")
    results = CnnModel.evaluate(X_test, y_test, batch_size=batch_size)
    print(results)

    # print("-- y_pred_test ---")
    y_pred_test = CnnModel.predict(X_test)
    # print(y_pred_test)

    y_pred_test = (y_pred_test > 0.5)
    # print(y_pred_test)

    print("--- matrix de confusão")
    #cm = confusion_matrix(y_test, y_pred_test)
    cm = confusion_matrix(y_test, y_pred_test)
    print(cm)

    print("--- salve ---")
    path = 'apps/pln/weights_folder/my_weights'
    CnnModel.save_weights(path, save_format='tf')
    print('Model Saved!')
    print("-------------------------------------------------------------------------")
    
    print(f"accuracy_score: {accuracy_score(y_pred_test,y_test)}")
    print(f"precision_score: {precision_score(y_pred_test,y_test)}")
    print(f"recall_score: {recall_score(y_pred_test,y_test)}")
    print(f"f1_score: {f1_score(y_pred_test,y_test)}") 
    
    print()
    print("---------- testes -------------------")
    text = 'Não gostei desse produto'

    vocab_fname = "apps/pln/services/ttVocab"
    encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(vocab_fname)
    text = encoder.encode(text)
    value = CnnModel(np.array([text]), training=False).numpy()
    print(value)
