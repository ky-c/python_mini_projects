from random import choice

def main():
    input("\n\n\nWhat time should Lucia write her CS final exam? \nOptions are: 9:30am or 12:30pm.")
    print(f"Lucia should write her final at {choice(["9:30am", "12:30pm"])}\n\n")

if __name__ == "__main__":
    main()