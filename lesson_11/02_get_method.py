this_dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}

expected = input("enter your key: ")
print(this_dict.get(expected, f" '{expected}' doesn't exist..."))