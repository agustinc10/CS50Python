def main():
    twit = input("Input: ")
    twit2 = shorten(twit)
    print("Output:", twit2)


def shorten(word):
    vowels = "AaEeIiOoUu"
    word2 = ""
    for t in word:
        if t not in (vowels):
            word2 += t
    return word2


if __name__ == "__main__":
    main()
