
import import_data
import matplotlib.pyplot as plt
import math
from datetime import datetime
import numpy as np

months = import_data.import_data()

# print((months))
# print(months['mars22']['Type'])

#observedKey = 'Nombre vendu de la clayette' 
observedKey = '% Ventes'

clayettes = {}
for key in months:
    print(key)
    # print(months[key].columns.values.tolist())
    # print(months[key]['Type'])
    df = months[key]
    for index, row in df.iterrows():
        if isinstance(row['Type'], str):
            #print(row['Type'], row['% Ventes'])
            if not (row['Type'] in clayettes):
                clayettes[row['Type']] = {'vente':[], 'time': []}
            
            print(row['Date début'])
            date = datetime.strptime(row['Date début'], '%d/%m/%Y')
            clayettes[row['Type']]['time'].append(date)
            clayettes[row['Type']]['vente'].append(float(row[observedKey].replace(' %', '').replace(',','.')))
            #clayettes[row['Type']]['vente'].append(float(row[observedKey]))


    
#for key in clayettes:
#keys = ['SOLO DUO', 'SOUPE ET POTEE', 'QUI CHANGE', 'MOMENT']
#keys = ['QUI CHANGE']

#ecarts types
stds = []
for key in clayettes:
    stds.append({'key':key, 'std':round(np.std(clayettes[key]['vente']),2), 'nombre_lignes':len(clayettes[key]['vente'])})
    #print(key, )
    #plt.scatter(clayettes[key]['time'], clayettes[key]['vente'], label=key)
for element in sorted(stds, key=lambda std: std['std']):
    print(element)

#graph
keys = ['1,5KG MIRABELLE', '1KG FRAISE', '1KG ASPERGE', '750G CERISE', 'SOUPE ET POTEE']
for key in keys:
    plt.scatter(clayettes[key]['time'], clayettes[key]['vente'], label=key)

plt.title('Pourcentage de clayette vendues au cours du temps')
plt.ylabel('% de clayette vendues')
plt.xlabel('Temps')
plt.legend()
plt.show()
