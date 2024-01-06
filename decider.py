from random import choice

def main():
    print("Welcome to the decider, designed to decide for the indecisive.")
    num_options = get_number("How many options are you deciding between? ")

    options = []

    for i in range(num_options):
        options.append(input(f"Please input option #{i + 1}: "))

    input(f"Hit any key to reveal what you should do from your {num_options} option(s)!")
    print(f"You know what you should do? You should: {choice(options)}")
    input("The decider has decided :) Hit any key to exit.")

def get_number(msg):
    while True:
        try:
            ret = int(input(msg))
            if ret < 1:
                print("Must have at least one option.")
                continue
            return ret
        except ValueError:
            print("Only integers are accepted.")

if __name__ == "__main__":
    main()