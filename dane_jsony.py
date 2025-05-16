import json
import os
import pandas as pd

#%%
# żeby działało, w aktualnym folderze 
# musi być folder pdu-2025L-dane-json z danymi
# inaczej nie zwróci nic lub przypadkowe jsony
if 'pdu-2025L-dane-json' in os.listdir():
    os.chdir('pdu-2025L-dane-json')
    
l = []
for file in os.listdir():
    if file.endswith(".json"):
        file_path = f"{file}"
        with open(file_path) as f:
            a = json.load(f)
            p = pd.DataFrame(data=[list(a.values())], columns = a.keys())
            l.append(p)

x = pd.concat(l).reset_index(drop=True)
x
#%%
