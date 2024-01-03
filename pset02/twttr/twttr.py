twit = input("Input: ")
vowels = "AaEeIiOoUu"
print("Output: ", end="")
for t in twit:
    if t not in (vowels):
        print (t, end="")
print()
