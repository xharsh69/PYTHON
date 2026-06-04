marks= {
    "harsh": 100,
    "rahul": 67,
    "khushi": 89,
    "padmini": 76

}

print(marks, type(marks))
print(len(marks)) # lenth os dict
print(marks.items()) # get al items
print(marks.keys()) # get all keys
print(marks.values()) # Get all values
marks.update({"harsh":99,"renuka":80}) # update your veluas
marks.pop("khushi") # remove item

print(marks) 

print(marks.get("harsh")) 
print(marks["harsh"])


print(marks.get("harsh")) # print none
# print(marks["garsh"]) # return error

marks["khushi jha"] = 90
print(marks)

marks_copy = marks.copy() # copy your dict
marks_copy.popitem() # remove last item
marks_copy.clear() # clear  dictionary
print(marks_copy)


