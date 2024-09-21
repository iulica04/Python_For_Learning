# Write a function that receives a variable number of sets and returns a dictionary with the
# following operations from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
#
# Ex: {1,2}, {2, 3} =>
#
# {
#
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#
#     "{1, 2} & {2, 3}":  { 2 },
#
#     "{1, 2} - {2, 3}":  { 1 },
#
#     ...

# }

def pairwise_set_operations(*sets):
    number_of_sets = len(sets)
    dictionary = {}

    for i in range(0, number_of_sets-1):
        for j in range(i+1, number_of_sets):
            string1 = str(sets[i]) + ' | ' + str(sets[j])
            string2 = str(sets[i]) + ' & ' + str(sets[j])
            string3 = str(sets[i]) + ' - ' + str(sets[j])

            dictionary[string1] = sets[i] | sets[j]
            dictionary[string2] = sets[i] & sets[j]
            dictionary[string3] = sets[i] - sets[j]

    return dictionary


if __name__ == "__main__":
    print(pairwise_set_operations({1,2}, {2,3}))