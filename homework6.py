my_dict = {'SASHA': 34256, 'NIKA': 1242, 'JON': 3357}
print("Dict:",my_dict)
print("Existing value:",my_dict.get('SASHA'))
print("Not existing value:",my_dict.get('SANA'))
my_dict['WELL'] = 9243
my_dict['ANN'] = 3543
a = my_dict.pop('SASHA')
print("Deleted value:",a)
print("Modified dictionary:", my_dict)
my_set = {1, 2, 3, 4, 1.2, 7, 2, "tri", 3.21}
print()
print("Set:", my_set)
my_set.add(12)
my_set.add(19)
my_set.discard(2)
print("Modified set:", my_set)