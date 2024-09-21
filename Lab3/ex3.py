# Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other
# containers, such as dictionaries, lists, sets, etc.)



def compare_dicts(dict1, dict2) :

    if dict1.keys() != dict2.keys() :
        return False

    # in this case both dictionaries have same keys

    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]


        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        elif isinstance(value1, (list, tuple)) and isinstance(value2, (list, tuple)):
            if len(value1) != len(value2) :
                return False
            elif any(value1[i] != value2[i] for i in range(0, len(value1))):
                return False

        elif isinstance(value1, set) and isinstance(value2, set):
            if value1 != value2:
                return False

        elif value1 != value2:
            return False

    return True

if __name__ == "__main__":
    dict1 = {"a": 1, "b": {"c": 3, "d": 4}, "e": [5, 6, 7], "f": {8, 9}}
    dict2 = {"a": 1, "b": {"c": 3, "d": 4}, "e": [5, 6, 9], "f": {9, 8}}

    print(compare_dicts(dict1, dict2))