import copy

original_dict = {"a": 1, "b": [2, 3]}
copied_dict = copy.copy(original_dict)
copied_dict["b"].append(4)
print(f"copied_dict : {copied_dict}")
print(f"original_dict : {original_dict}")

"""
相同的範例,接著我要去修改它
類似說我要去append附加4,各位看一下可能會有什麼結果
將它印出來,結果就是b去新增了4
那原始的呢,original_dict,我去印出一下
為什麼原本的會新增一個4.各位可能會想說
阿我不是複製一份出來了,為何原本的還會變?
這邊我解釋一下喔, 剛才進行淺層複製
將原始字典的內容複製到copied_dict
這個時候copied_dict 和 original_dict 都有自己的字典對象，
但是它們中 "a" 鍵對應的值 1 和 "b" 鍵對應的值 [2, 3]
都指向同一個列表對象[2, 3]
所以原始字典 original_dict 中的 "b" 鍵對應的值也會被改變
"""
