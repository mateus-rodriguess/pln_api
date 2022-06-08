import logging
import os

import numpy as np

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger('tensorflow').disabled = True

import tensorflow_datasets as tfds
from apps.config import get_settings
from apps.pln.dm.dcnn import DCNN

settings = get_settings()

Dcnn = DCNN()
Dcnn.built = True

Dcnn.load_weights(settings.PATH_MY_WEIGHTS).expect_partial()
encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(settings.VOCAB_FNAME)


def accuracy_response(text: str):
    """
    Accuracy predict
    """
    text = encoder.encode(text)
    [[accuracy]] =  Dcnn.predict(np.array([text]))
   
    return accuracy.astype(float)
