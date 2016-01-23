


my_str =input("Enter a string: ")

print("before " + my_str)


my_str = my_str.casefold()

print("after " + my_str)


rev_str = reversed(my_str)


if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
