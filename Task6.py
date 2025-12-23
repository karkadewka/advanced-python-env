def eqs(lst):
    m = max(len(s) for s in lst)
    return [s.ljust(m, "_") for s in lst]

my_list = ["a333", "abc", "desdfsdf"]
print(eqs(my_list))
