import random
def check(a, name, cnt):
    m = int(input())
    cnt += 1
    if m == a:
        print("Good job,", end = " ")
        print(name, end = "")
        print("! You guessed my number in", cnt, "guesses!")
    if m < a:
        print("Your guess is too low.")
        check(a,name,cnt)
    if m > a:
        print("Your guess is too high.")
        check(a,name,cnt)
print("Hello! What is your name?")
name = str(input())
print("Well,", end = " ")
print(name, end = ",")
print(" I am thinking of a number between 1 and 20.")
print("Take a guess.")
cnt = 0
a = random.randrange(1,20)
check(a,name,cnt)