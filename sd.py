from Autofhm.autofhm import Autofhm
import time
from datetime import datetime
from pathlib import Path
import sys
import os
import warnings



def getModel(config = "test/iris/config.json", name = 'model'):
    # print("aaaa")
    if os.path.exists(config):
        model = Autofhm(config=config)
        model.get_features()
        model.fit()
        model.save_model(name,'models/')
        return str(model._model), 'models/'+ name+'.sav'
        
    return 'error'
	

if __name__ == "__main__":
	getModel()

