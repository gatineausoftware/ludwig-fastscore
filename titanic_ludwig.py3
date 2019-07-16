#fastscore.action: unused
#fastscore.schema.0: ludwig_titanic_input
#fastscore.schema.1: ludwig_titanic_output
#fastscore.module-attached: ludwig

from fastscore.io import Slot
from ludwig.api import LudwigModel
import pandas as pd
import tarfile

with tarfile.open('titanic_model.tar.gz', 'r:gz') as tar:
    tar.extractall('/tmp/titanic')

model = LudwigModel.load('/tmp/titanic/model')


slot0 = Slot(0)
slot1 = Slot(1)
for df in slot0:
	preds = model.predict(df)
	for j in range(len(preds)):
		slot1.write(preds.iloc[j,:].to_dict())
