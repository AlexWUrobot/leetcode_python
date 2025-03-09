# 

dict_o = {}
key = "key_input"
dict_o["key_input"] = [6]
dict_o["key_input"].append(7)
print (dict)
print (dict_o["key_input"])


from collections import defaultdict

dict = defaultdict(list)
dict["key_input"].append(7)   # the only difference, we can append immediately 
dict["key_input"].append(8)
print (dict)
print(dict["key_input"])
