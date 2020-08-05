class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
    def add(self):
        return {'first_name': self.first_name, 'last_name': self.last_name, 'father': self.father}

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a.add())
a = {
    "key1":1,
    "key2":{
        "key3":1,
        "key4":{
            "key5":5,
            'user': person_b.add()
        }
    }
}

person_c = Person('User1', '3', None)
person_d = Person('User2', '4', person_c.add())
b = {
    "key1":1,
    "key2":{
        "key3":1,
        "key4":{
            "key5":5,
            'usertest': person_d.add()
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