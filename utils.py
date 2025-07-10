def validate(prompt, test, original = None):
    while True:
        value = input(prompt).strip()
        if test(value or original):
            return value or original
        print("Invalid input. Try again.")
        
