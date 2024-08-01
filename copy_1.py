import copy

original_list = [1, 2, 3]
copied = copy.copy(original_list)
print(copied)


# import copy  # 首先我要匯入copy模組

# original_list = [1, 2, 3]  # 原始的list 1,2,3
# copied_list = copy.copy(original_list)  # 去複製原本的

# print(copied_list)  # 將結果印出來

# """
# 這一小節要製作淺層複製
# 淺層複製意味著它會創建一個新的列表對象，
# 並將 original_list 中的元素複製到這個新列表中。
# 這裡時實作給各位看
# 因此，copied_list 現在包含與 original_list 相同的元素 [1, 2, 3]。
# """
