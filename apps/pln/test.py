import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import logging
logging.getLogger('tensorflow').disabled = True

import numpy as np
from dm.dcnn import DCNN
import tensorflow_datasets as tfds


Dcnn = DCNN()
Dcnn.built = True

path = 'apps/pln/weights_folder/my_weights'
Dcnn.load_weights(path).expect_partial()

vocab_fname = "apps/pln/services/ttVocab"


encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(vocab_fname)
text = "Ele não é um Grimorio de verdade com feitiços e etc. É um livro de história e sem dúvidas um dos livros mais completos sobre a Bruxaria."
text = encoder.encode(text)

# 0 =  negativo
# 1 = possitivo

value = Dcnn.predict(np.array([text]))
print(value)
