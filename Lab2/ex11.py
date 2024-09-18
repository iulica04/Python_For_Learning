# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sort_tuples_by_third_char(tuples_list):

    def sort_key(tpl) :
        return tpl[1][2] if len(tpl[1]) > 2 else ' '

    sorted_list = sorted(tuples_list, key=sort_key)
    return sorted_list

if __name__ == "__main__":
    tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
    result = sort_tuples_by_third_char(tuples_list)
    print(result)