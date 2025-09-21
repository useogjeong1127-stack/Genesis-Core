from seed import Seed

def main():
    seed = Seed("Genesis-01")
    print("Before activation:", seed)

    seed.activate()
    print("After activation:", seed)

if __name__ == "__main__":
    main()