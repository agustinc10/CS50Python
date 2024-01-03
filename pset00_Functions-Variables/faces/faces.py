def main():
    x = convert(input("Write: "))
    print(x)

def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

main()
