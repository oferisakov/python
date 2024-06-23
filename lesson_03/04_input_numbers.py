num_1 = int(input("please enter first number: "))
num_2 = int(input("please enter second number: "))

print(f"{num_1} + {num_2} = {num_1 + num_2}")

#-------------------------------------------------------------------

score1, score2 = input("enter your scores: ").split()
score1 = int(score1)
score2 = int(score2)
print(score1 + score2)

# --------------------------------------------------------------

num1, num2, num3 = map(int, input("enter 3 numbers: ").split())
print(num1 + num2 + num3)