import random

print("Harsh-Raj-Singh")
computer = random.randint(1, 99)

attempts = 1

while True:
    guess = int(input("Enter your number (1 to 99): "))

    if guess == computer:
        print(f"🎉 You guessed the right number: {computer}")
        print(f"Number of attempts: {attempts}")
        break

    elif guess < computer:
        print("⬆️ Please enter a higher number.")

    else:
        print("⬇️ Please enter a lower number.")

    attempts += 1