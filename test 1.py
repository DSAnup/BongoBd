
a = {
    "key1":1,
    "key2":{
        "key3":1,
        "key4":{
            "key5":4
        }
    }
}
b = {
    "test1":1,
    "test2":{
        "test3":1,
        "test4":{
            "test5":5
        }
    }
}
def print_depth(d, indent=1):
    for key, value in d.items():
        print(key, indent)
        if isinstance(value, dict):
            return print_depth(value, indent+1)

print(print_depth(a))
print(print_depth(b))
# Time complexity & space complexity of the above solution is O(n)