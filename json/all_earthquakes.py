import json

# Explore the structure of the data.
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# print(all_eq_data)

all_eq_dicts = all_eq_data['features']
for d in all_eq_dicts:
    print(d['properties'])
# print(all_eq_dicts)
# print(all_eq_dicts)
# for x in all_eq_dicts:
#     print(x)
