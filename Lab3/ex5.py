# . The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end)
# and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
#
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} =>
# False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

def validate_dict(rules, dictionary):
    # More details:
    #   1. multiples values from dictionary can respect same rule
    #   2. can exist more rules that values in dictionary

    for key in dictionary.keys():
        rules_for_element= [r for r in rules for element in r if element==key]
        text = dictionary[key]

        if rules_for_element:
           for rule in rules_for_element:
               prefix= rule[1]
               middle = rule[2]
               suffix = rule[3]
               if not (text.endswith(suffix) and text.startswith(prefix) and text.find(middle) != -1):
                   return False # The element with key %s does not meet the rule

        else:
            return False # For the element with this key, there is no rule in the list of rules.

    return True


if __name__  == "__main__":
    s = {("key1", "", "inside", ""), ("key2", "this", "not", "valid")}
    d = {"key1": "come inside, it's too cold out", "key2": "this is not valid"}
    print(validate_dict(s, d))