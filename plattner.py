import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


desired_width=500
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 100)

with open('C:/Users/Sri/Desktop/samplejson.json') as f:
    data = json.load(f)

df = json_normalize(data)
print(df['locations'])

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

flat = flatten_json(data)
new_flat = json_normalize(flat)

dfs = pd.DataFrame(new_flat)
print(dfs.head(2))
