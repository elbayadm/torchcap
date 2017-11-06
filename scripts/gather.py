
# coding: utf-8

# In[70]:


import glob
import operator
import pickle
from math import exp
from prettytable import PrettyTable


# In[92]:


def get_results(model, split='val'):
    model_dir = model
    val_results = sorted(glob.glob('%s/val_*.res' % model_dir))
    compiled = []
    for res in val_results:
        params = res.split('/')[-1].split('_')
        beam = int(params[1][2:])
        sample_max = 1 if params[3] == "max" else 0
        temp = 0
        if not sample_max:
            temp = float(params[4])
            index = 5
        else:
            index = 4
        flip = int(params[index][4])
        params = {'beam_size': beam, 'sample_max': sample_max,
                 'temperature': temp, 'flip': flip}
        # Load results:
        out = pickle.load(open(res, 'rb'))
        compiled.append([params, out])
    return compiled


# In[93]:


fields = ['Beam', 'Temperature', 'CIDEr', 'Bleu4', 'Spice', 'Perplexity']
def gather_results(model):
    outputs = get_results(model)
    tab = PrettyTable()
    tab.field_names = ['Sorter'] + fields
    for (p, res) in outputs:
        tab.add_row([p['beam_size'] + p['temperature'],
                     p['beam_size'], p['temperature'],
                     round(res['CIDEr'] * 100, 2), round(res['Bleu_4'] * 100, 2),
                     round(res['SPICE'] * 100, 2), round(exp(res['ml_loss']), 2)])
    return tab


# In[94]:


tab = gather_results("../save/baseline")
print(tab.get_string(fields=fields, sortby="Sorter"))
print(tab.get_html_string(fields=fields, sortby="Sorter"))


# In[98]:


def parse_name(model):
    if '/' in model:
        model = model.split('/')[-1]
    return model


# In[99]:


def crawl_results():
    models = glob.glob('../save/*')
    print("Found:", models)
    fields = ["Model", 'Beam', 'CIDEr', 'Bleu4', 'Spice', 'Perplexity']
    tab = PrettyTable()
    tab.field_names = fields
    for model in models:
        modelname = parse_name(model)
        outputs = get_results(model)
        for (p, res) in outputs:
            if p['beam_size'] > 1:
                tab.add_row([modelname,
                             p['beam_size'],
                             round(res['CIDEr'] * 100, 2), round(res['Bleu_4'] * 100, 2),
                             round(res['SPICE'] * 100, 2), round(exp(res['ml_loss']), 2)])
    return tab
        


# In[100]:


tab = crawl_results()
print(tab)
