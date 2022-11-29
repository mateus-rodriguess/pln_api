import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import logging
logging.getLogger('tensorflow').disabled = True

import numpy as np
from apps.pln.cnn.cnn import cnn_model
import tensorflow_datasets as tfds


model = cnn_model()
model.built = True

path = 'apps/pln/weights_folder/my_weights'
model.load_weights(path).expect_partial()

vocab_fname = "apps/pln/services/ttVocab"


encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(vocab_fname)
text = "O produto veio errado . Na descrição está escrito aquarela e veio um giz de cera.Meu filho ficou decepcionado . Péssimo"
text = encoder.encode(text)

# 0 =  negativo
# 1 = possitivo

[[value]] = model.predict(np.array([text]))
print(value)
