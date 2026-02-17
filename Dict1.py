dict1 = {"key1/1": "v1/1", "key1/2": "v1/2" }
dict2 = {"key2/1": "v2/1", "key2/2": "v2/2" }
dict3 = {"key3/1": "v3/1", "key3/2": "v3/2" }
dict4 = {**dict1, **dict2, **dict3}
print(dict4)
