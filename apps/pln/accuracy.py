import logging
import os
from typing import Dict

import numpy as np
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger('tensorflow').disabled = True
import tensorflow_datasets as tfds

from apps.pln.dm.dcnn import DCNN

from apps.config import get_settings

settings = get_settings()

Dcnn = DCNN()
Dcnn.built = True

Dcnn.load_weights(settings.path_my_weights).expect_partial()
encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(settings.vocab_fname)


def accuracy_response(text: str) -> Dict:

    text = encoder.encode(text)
    [[accuracy]] =  Dcnn.predict(np.array([text]))
    
   
    return accuracy
