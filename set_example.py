set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2
print(union_set)  # 輸出：{1, 2, 3, 4, 5, 6}

intersection_set = set1 & set2
print(intersection_set)  # 輸出：{3, 4}

difference_set = set1 - set2
print(difference_set)  # 輸出：{1, 2}

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # 輸出：{1, 2, 5, 6}
