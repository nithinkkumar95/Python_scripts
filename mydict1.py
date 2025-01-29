mydict={
"name": "Nithin",
"id": 111,
"domain": ["Devops", "Cloud Engineer", "SRE"],
"tools":{"os": ["Linux", "Cloud"], "cloud": "AWS"}
}
print(mydict)
print(mydict["name"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["tools"])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][1])
mydict["place"]=["Bangalore", "Pune"]
print(mydict)
mydict1={
        "name1": "Chatitha"
        }
mydict.update(mydict1)
print(mydict)
