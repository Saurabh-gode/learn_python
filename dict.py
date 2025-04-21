our_dictionary = {
    "name": "Joe",
    "age": 25,
    "value": "This is some text",
    "foo": "bar",
    3: "test",
    (1, 2): "test2",
    "items": ["test", 1, 2, 6, "one"],
    "another_random_value": False,
    "set_1": {0, 1, 2, 4, 4},
    "odd_thing": {"length": 34, "area": 600},
    "nothing": None,
}

t = ("name", "foo", "nothing", "odd_thing", "set_1")

for key in our_dictionary:
    if(key in t):
        print(f"our dictionary has the key {key} \n  the value of the key is: {our_dictionary[key]}")
        print("-------------------------------")


