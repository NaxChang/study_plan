import copy

original_tuple = (1, 2, [3, 4])
copied_tuple = copy.copy(original_tuple)
deep_copied_tuple = copy.deepcopy(original_tuple)

original_tuple[2].append(5)

print(original_tuple)
print(copied_tuple)
print(deep_copied_tuple)

# import copy

# original_tuple = (1, 2, [3, 4])
# copied_tuple = copy.copy(original_tuple)
# deep_copied_tuple = copy.deepcopy(original_tuple)

# print(copied_tuple)  # Output: (1, 2, [3, 4])
# print(deep_copied_tuple)  # Output: (1, 2, [3, 4])

# # 修改原始元組中的列表對象
# original_tuple[2].append(5)

# print(original_tuple)  # Output: (1, 2, [3, 4, 5])
# print(copied_tuple)  # Output: (1, 2, [3, 4, 5])  (影響到了)
# print(deep_copied_tuple)  # Output: (1, 2, [3, 4])  (未影響到)
