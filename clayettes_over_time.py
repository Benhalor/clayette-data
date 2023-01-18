
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
        if isinstance(row['Type'], str) and isinstance(row['Prix'], str):
            #print(row['Type'], row['% Ventes'])
            if not (row['Type'] in clayettes):
                clayettes[row['Type']] = {
                    'vente': [], 'time': [], 'ingredients': [],
                    'prix': [],
                    }

            print(row['Date début'])
            date = datetime.strptime(row['Date début'], '%d/%m/%Y')
            clayettes[row['Type']]['time'].append(date)
            clayettes[row['Type']]['vente'].append(
                float(row[observedKey].replace(' %', '').replace(',', '.'))) #
            ingredients = []
            for i in range(1, 11):
                if isinstance(row['Ingrédient '+str(i)], str) and len(row['Ingrédient '+str(i)]) > 0:
                    ingredients.append(row['Ingrédient '+str(i)])
            clayettes[row['Type']]['ingredients'].append(ingredients)
            clayettes[row['Type']]['prix'].append(float(row['Prix'].replace(',','.')))
            # clayettes[row['Type']]['vente'].append(float(row[observedKey]))


# for key in clayettes:
#keys = ['SOLO DUO', 'SOUPE ET POTEE', 'QUI CHANGE', 'MOMENT']
"""keys = ['POMMEE']

# ecarts types
stds = []
for key in keys:
    stds.append({'key': key, 'std': round(np.std(
        clayettes[key]['vente']), 2), 'nombre_lignes': len(clayettes[key]['vente'])})
    #print(key, )
    plt.scatter(clayettes[key]['time'], clayettes[key]['vente'], label=key)
for element in sorted(stds, key=lambda std: std['std']):
    print(element)
plt.show()
"""
# graph evolution clayette
"""keys = ['1,5KG MIRABELLE', '1KG FRAISE',
        '1KG ASPERGE', '750G CERISE', 'SOUPE ET POTEE']
for key in keys:
    plt.scatter(clayettes[key]['time'], clayettes[key]['vente'], label=key)

plt.title('Pourcentage de clayette vendues au cours du temps')
plt.ylabel('% de clayette vendues')
plt.xlabel('Temps')
plt.legend()
plt.show()"""


# graph ingrédients clayette
key = 'FRUITS DE SAISON'
listOfIngredients = [['Clémentine']]
for ingredients in listOfIngredients:
    #ingredients = ['PdT']
    ventes = []
    dates = []
    notventes = []
    notdates = []
    for i in range(len(clayettes[key]['time'])):
        # print(week)
        if (all(item in clayettes[key]['ingredients'][i] for item in ingredients)):
            ventes.append(clayettes[key]['vente'][i])
            dates.append(clayettes[key]['time'][i])
        else:
            notventes.append(clayettes[key]['vente'][i])
            notdates.append(clayettes[key]['time'][i])
    plt.scatter(dates, ventes, label=' & '.join(ingredients))
    plt.scatter(notdates, notventes, label='not '+' & '.join(ingredients))

plt.title('Ventes de la ' + key)
plt.xlabel('Temps (en jours)')
plt.ylabel('Ventes en %')
plt.legend()
plt.plot()
plt.show()




"""
# ventes en fonction du prix
keys = ['FRUITS DE SAISON']
for key in keys:
    plt.scatter(clayettes[key]['prix'], clayettes[key]['vente'], label=key)
    

plt.title('Ventes de la ' + key)
plt.xlabel('Prix (€)')
plt.ylabel('Ventes en nombre de clayette')
plt.legend()
plt.plot()
plt.show()"""
