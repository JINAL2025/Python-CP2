#serialise / deserialise a tuple
import json
f = open("SampleData", "w+")
tpl = ("Jinal", "25/05/2008", "B+")
json.dump(tpl, f)
f.seek(0)
intpl = json.load(f)
print(tuple(intpl))
f.close()
