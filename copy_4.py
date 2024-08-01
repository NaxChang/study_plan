import copy

original_dict = {"a": 1, "b": [2, 3]}
copied_dict = copy.deepcopy(original_dict)
copied_dict["b"].append(4)
print(f"copied_dict : {copied_dict}")
print(f"original_dict : {original_dict}")


"""
那我要如何解決剛才的問題,
這個時候我可以用進行深層複製（deep copy）
那我們列印來看一下結果喔複製的新增4,原始的不變
為什麼呢?因為原始字典 original_dict 中的 "b" 鍵所對應的值
並沒有因為 複製字典copied_dict 中的 "b" 鍵所對應的列表被修改而受到影響。
這是因為深層複製創建了 copied_dict 的完全獨立副本，
包括內部的可變物件列表 [2, 3]，而不是僅僅複製它的引用。
"""
