
import import_data
months = import_data.import_data()

#print((months))
#print(months['mars22']['Type'])

clayettes = {}
for key in months:
    print(key)
    print(months[key].columns.values.tolist())
    print(months[key]['Type'])