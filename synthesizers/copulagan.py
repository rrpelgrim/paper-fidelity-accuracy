
# conda create -y -n sdv python==3.7.7
# conda activate sdv
# pip install sdv==0.7.0

import pandas as pd
import numpy as np
import torch
from sdv.tabular import CopulaGAN

datasets = ['adult', 'credit-default', 'marketing', 'online-shoppers']

for dataset in datasets:
    print('CopulaGAN ' + dataset)
    np.random.seed(0)
    torch.manual_seed(0)
    data = pd.read_csv('~/data/paper05/data/' + dataset + '_trn.csv')
    if dataset == 'credit-default':
        data = data.astype({'SEX': 'object', 'EDUCATION': 'object', 'MARRIAGE': 'object'})
    model = CopulaGAN(verbose=True)
    model.fit(data)
    samples = model.sample(50000)
    samples.to_csv('~/data/paper05/data/' + dataset + '_copulagan.csv', index=False)
