
def all_thing_is_obj(object: any) -> int:
    types: dict = {"List": list, "Tuple": tuple, "Set": set, "Dict": dict, "is in the kitchen": str}
    for key, value in types.items():
        if (isinstance(object, value)):
            if (isinstance(object, str)):
                print(f"{object} {key}: {value}")
            else:
                print(f"{key}: {value}")
            return 42
    print("Type not found")
    return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
print(all_thing_is_obj(10))
