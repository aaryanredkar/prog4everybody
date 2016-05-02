while True:
    try:
        number = int(input("Enter a number..."))
        print("The number you entered was: ", number)
        break
    except ValueError:
        print("wow Sid, go back to preschool and suck eggs")
