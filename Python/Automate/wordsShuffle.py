from pyexcel_ods3 import get_data
import json, random

data = get_data("words.ods")
print(type(data))
listData = data["Sheet1"]
bigString = ""
bigString = "\n".join(x[0] for x in listData)
bigString = bigString.split('\n')
length = (len(bigString))
counter = 0
print(len(set(bigString)))
for i in range(0, length):
	item = random.choice(bigString)
	# bigString.remove(item)
	print(item)
	counter += 1
print(type(bigString), counter)
dictdata = json.dumps(data)
with open("words.json", "w") as f:
	json.dump(data, f)