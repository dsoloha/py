# Word Counter
# Dan Soloha
# 10/11/2019

from collections import Counter

def open_file():
    f = input("Please enter the name of the file you would like to use, including the extension. ")
    try:
        f = open(f, "r", encoding="utf-8-sig")
    except:
        print("Sorry, that file could not be found. Please ensure you entered the title correctly and try again. ")
        print("Exiting...")
    else:
        return f

def main():
    _file = open_file()
    count = Counter(_file.read().split())

    for item in count.items():
        print("{}\t{}".format(*item))

if __name__ == "__main__":
    main()