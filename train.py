### Importamos Librerias
from datetime import datetime

print('START SCRIPT AT {}\n'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
import numpy as np
import re

# Librerías para paths o sistema
from glob import glob
from time import time
import pickle as pkl
import json
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MaxAbsScaler, FunctionTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
# from sklearn import decomposition, model_selection, metrics, pipeline

# Libreria propia
from utils import read_close
from utils import match_g

# load filenames path
total_files = np.array(glob("{}/*/*".format(sys.argv[1])))
class_files = np.array(glob("{}/*".format(sys.argv[1])))

filename = 'trained_model.pkl'
file_tar_enc = 'target_encoder.json'

## Lectura
print('READ DATA\n')

pat = r'.*\\(.*)\\(.*)$'
total = [(read_close(x,'r'), match_g(pat, x, 1)) for x in total_files]
print('There are {} documents'.format(len(total)))
# Puede ser interesante hacer shuffle cuando entrenamos
np.random.seed(0)
np.random.shuffle(total)
docs = [x[0] for x in total]
labels = [x[1] for x in total]

# Test to ensure that we have all the info labeled
assert((len(docs) == len(labels))&(len(docs) == len(total_files)))

## Prepare training
d_lab_cod = {}
d_cod_lab = {}
for i, label in enumerate(list(set(labels))):
    d_lab_cod[label] = i
    d_cod_lab[i] = label

X_train = docs
y_train = [d_lab_cod[x] for x in labels]

## Train Model
print('START TRAINING...\n')
tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3), use_idf=1,smooth_idf=1,sublinear_tf=1,
            stop_words = 'english')

pipe = Pipeline(steps = [('tfv', tfv),
                        # ('ToArr', FunctionTransformer(lambda x: x.toarray())), # To avoid problems due to sparsity from tfv
                        ('MM', MaxAbsScaler()),
                        ('NB', MultinomialNB())])
t0 = time()
pipe.fit(X_train, y_train)
print('Elapsed time: {:.0f} seconds\n'.format(time() - t0))
print('END TRAINING\n')

print('SAVING MODEL IN {}\n'.format(filename))
pkl.dump(pipe, open(filename, 'wb'))
json.dump(d_cod_lab, open(file_tar_enc, 'w'))

print('END')
# y_train_pipe, d_train_pipe = encode_label(y_train_pipe)
# y_test_pipe, _ = encode_label(y_test_pipe, d_train_pipe)