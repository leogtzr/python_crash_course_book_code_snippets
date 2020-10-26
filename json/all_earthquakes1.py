import json

# Explore the structure of the data.
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# print(all_eq_data)

mags = []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])
