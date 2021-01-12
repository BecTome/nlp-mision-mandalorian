import sys
import json
import pickle as pkl
from utils import read_close

## Read model from arguments
modelpath = sys.argv[1]
if (len(sys.argv) == 2):
    raise Exception('Introduce Model path and FilesPath')
else:
    predictions = sys.argv[2:]

model = pkl.load(open(modelpath, 'rb'))
d_map = json.load(open('target_encoder.json', 'r'))

## Read predictions from arguments
X_test = [read_close(x) for x in predictions]
y_test = model.predict(X_test)
ls_test = [d_map[str(x)] for x in list(y_test)]

## Print predictions
for path, pred in zip(predictions, ls_test):
    print('{}\t{}'.format(path, pred))