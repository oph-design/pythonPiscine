def NULL_not_found(object: any) -> int:
    values = {"Nothing": None, "Cheese": float("NaN"), "Zero": 0, "Empty": "", "Fake": False}
    for key, value in values.items():
        if (value == object):
            print(f"{key}: {object} {type(object)}")
            return 0;
    print("Type not Found")
    return 1;


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
