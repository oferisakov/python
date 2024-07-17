str1 = "HALLO WORLD"
str2 = "hello world"
str3 = "hello ofer isakov"
str4 = "hello;ofer;isakov"
str5 = "ofer isakov"

print("lower_method ->", str1, "->", str1.lower())
print("upper_method ->", str2, "->", str2.upper())
print("capitalize_method ->", str2, "->", str2.capitalize())
print("capitalize_method ->", str3, "->", str3.capitalize())

print("title_method ->", str3, "->", str3.title())

print("split_method ->", str3, "->", str3.split())
print("split_method ->", str4, "->", str4.split())
print("split_method ->", str4, "->", str4.split(";"))

print("find_method_o ->", str3, "->", str3.find('o'))
print("find_method_m ->", str3, "->", str3.find('m'))

print("count_method_o ->", str3, "->", str3.count('o'))
print("count_method_m ->", str3, "->", str3.count('m'))

print("replace_method ->", str3, "->", str3.replace('ofer','world'))

print("join_method ->", "-".join(str2))