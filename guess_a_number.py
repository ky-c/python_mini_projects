from random import randint

def main():
    print("Please enter the range of integers you'd like to guess between.")

    lower = get_number("First integer: ")
    upper = get_number("Second integer: ")

    if lower > upper:
        lower, upper = upper, lower
    
    num = randint(lower, upper)
    tries = guess(lower, upper, num)
    print(f"Congratulations!!! You correctly guessed the number, {num}, in only {tries} tries!")

def get_number(msg):
    while True:
        try:
            ret = int(input(msg))
            return ret
        except ValueError:
            print("Only integers are accepted.")

def guess(lower, upper, num):
    tries = 0
    while True: 
        num_guessed = get_number(f"Guess a number between {lower} and {upper}, inclusive: ")
        tries += 1

        if num_guessed == num:
            return tries

        if num_guessed > upper or num_guessed < lower:
            print(f"Guess was out of the range of {lower} to {upper}. Try again.")
            continue

        if num_guessed < num:
            lower = num_guessed
        else:
            upper = num_guessed


if __name__ == "__main__":
    main()