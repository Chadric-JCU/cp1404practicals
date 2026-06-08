'''Takes a password and replaces it with stars'''

MINIMUM_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)

def get_password() -> str:
    password = input("Enter password to censor: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password too short, min length is {MINIMUM_LENGTH}")
        password = input("Enter a password: ")
    return password

def print_stars(password):
    for letter in password:
        print("*", end="")

main()

