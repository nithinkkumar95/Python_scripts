my_list = [1, 2, "Nithin", "Devops", 4, 5]

my_dict = {
           "Name": "Nithin",
           "Age": 29,
           "Place": "Bengaluru"
           }

my_list1 = []
if "Nithin" in my_list:
    print("Element Found")
else:
    print("Element is not Found")

if my_list1:
    print("List contains Values")
else:
    print("List doesnot contain Values")

if "Name" in my_dict:
    print("Key found")
else:
    print("Key not found")

if "Name" in my_dict.values():
    print("Value found")
else:
    print("Value not found")

if my_dict["Name"] == "Nithin":
    print("Key contains the value")
else:
    print("Key doesnot contain the value")


found = True

if not found:
    print("True")
else:
    print("False")

if my_dict:
    print("Dictionary is not empty")
else:
    print("Dictionary is empty")

