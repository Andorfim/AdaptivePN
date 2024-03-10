import numpy as np

c, d, e = [1, 2, 3]

a = np.random.randint(0, 10, 2)

b = [1, 2, 3]

b[int(2)] = 1
list_indexes = np.random.randint(0, 1)
list_indexes - 2

# for i in range(len(a)):
#     if number in a[i]:
#         print(f'число {number} лежит в {i} спике')


# list_indexes_delete = [[1], [2], [3]]
# list_indexes_delete = sum(list_indexes_delete, [])

original_list = [1, 2, 3, 4, 5, 6]
new_list = [original_list[i:i+3] for i in range(0, len(original_list), 3)]
index = np.random.randint(0, 2)

h = 5
# delete_data_x = list_indexes_delete[::2]
# delete_data_y =