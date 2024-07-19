tuple1 = 11, [22, 33], 44, 55

tuple2 = list(tuple1)

tuple2[1][0] = 222

tuple2 = tuple(tuple2)

print(tuple2)