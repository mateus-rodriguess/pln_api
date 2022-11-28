import logging
import os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger('tensorflow').disabled = True


from apps.pln.dm.dcnn import CnnModel
from apps.core.config import get_settings
import tensorflow_datasets as tfds
import numpy as np


def accuracy_predict(text: str):
    """
    Accuracy predict
    """
    settings = get_settings()

    Dcnn = CnnModel()
    Dcnn.built = True
    try:
        # if the error of the file does not exist it returns float 0.0
        Dcnn.load_weights(settings.PATH_MY_WEIGHTS).expect_partial()
        encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(
            settings.VOCAB_FNAME)
        text = encoder.encode(text)
        # feedback prediction
        [[accuracy]] = Dcnn.predict(np.array([text]))
        return accuracy.astype(float)
    except Exception as error:
        print(error)
        return 0.0
