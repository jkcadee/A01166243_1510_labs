import random


def main():
    word = random.sample("Index", k=2)

    print(str(2) % "hello")
# Type Error 1
    print("2" + 2)
# Type Error 2
    print(word[1] + word[2] + word[3])
# Index Error 1
    print(word[10])
# Index Error 2
    print(5 / 0)
# Division by 0


if __name__ == "__main__":
    main()