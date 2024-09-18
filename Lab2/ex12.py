# Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
#
# 	Example:
#
# group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]


def group_by_rhyme(words) :
    prefixes = list({word[-2:] for word in words})

    result = []
    for prefix in prefixes:
        rhyming_words = [word for word in words if word.endswith(prefix)]
        result.append(rhyming_words)

    return result

if __name__ == "__main__" :
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))