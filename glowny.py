# %%

import numpy as np
import pandas as pd
import glob
import copy

# %% [Markdown]
# 
# Legenda:
# 1. Data
# 2. X - LONGITUDE - DLUGOSC GEOGRAFICZNA
# 3. Y - LATITUDE - SZEROKOSC GEOGRAFICZNA
# 4. 

# %% Wczytywanie Ramki STARE

# sciezki = glob.glob('plikipdu//*.csv')
# df_list = []
# for sciezka in sciezki:
#     df = pd.read_csv(sciezka)
#     df_list.append(df)

# df = pd.concat(df_list,ignore_index=True)
# %% Ekstrakcja Daty

# rok = (df['timestamp'].str[:4]).astype(int)
# msc = (df['timestamp'].str[5:7]).astype(int)
# dzn = (df['timestamp'].str[8:10]).astype(int)
# czas = (df['timestamp'].str[11:19]).astype(str) 
# tz = (df['timestamp'].str[20:25]).astype(str) 
# df['rok'] = rok
# df['miesiac'] = msc
# df['dzien'] = dzn
# df['czas'] = czas
# df['strefa_czasowa'] = tz
# df[['timestamp','rok','miesiac','dzien','czas','strefa_czasowa']]
# df['data'] = pd.to_datetime(df['timestamp'].str[:19])
# # wygodniej bedzie jak beda oddzielnie kolumny na rok, msc, dzien gdzies z tylu

# # %% Bo czemu nie
# df_kopia_zapasowa = copy.deepcopy(df)

# # %% Usuwanie Brzydkiego Timestamp i zastapienie go data

# df = df.drop(columns='timestamp',errors='ignore')
# df = pd.concat([df['data'],df[df.columns[:22]]],axis=1,copy=False)
# # %% Posortowanie WG. daty

# df = df.sort_values('data').reset_index(drop=True)


# %% Wczytywanie NOWE

df = pd.read_csv('ramka_biegacz.csv')
df