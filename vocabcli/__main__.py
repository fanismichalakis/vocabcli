import sys
from .classmodule import MyClass
from .funcmodule import challenge

def main():
    args = sys.argv[1:]

    if args[0] == 'challenge':
        print("Commençons le test sur la liste de vocabulaire " + args[1])
        challenge(args[1])
    else:
        print("Je n'ai pas compris.")

if __name__ == '__main__':
    main()