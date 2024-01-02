def main():
    wage = ""
    while (type(wage) is str):
        wage = input("What is your hourly wage? ")
        try:
            wage = float(wage)
        except ValueError:
            print("Only numbers are accepted.")

    print(f"Your annual salary working full time (40 hours a week) before tax is ${round(wage * 52 * 40, 2) }")

    input("Hit any key to exit.")

    

main()