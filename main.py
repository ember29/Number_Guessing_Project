import art
import random
print(art.logo_1)
num=int(random.randint(1,100))
print("Wwlcome to the Number Guessing Game!")
print("I am thinking number between 1 to 100")
op=input("Choose a difficulti. Type 'easy' or 'hard':")
def fun():
    r=True
    while r:
        global attempts
        print(f"You Have {attempts} remaining to guess a number.")
        guess_num=int(input("make a guess:"))
        if guess_num > num:
            print("Too high")
            attempts-=1
            r=True
        if guess_num < num:
            print("too low")
            attempts-=1
            r=True
        if guess_num == num :
            print(f"You guess correct number! and number computer chooses is {num}")
            r=False


if op=="easy":
    attempts=10
    fun()


if op=="hard":
    attempts=5
    fun()