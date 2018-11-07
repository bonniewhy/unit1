def get_initials(fullname):
    # Given a person's name, returns the person's initials (uppercase)
    name_split = fullname.split()
    initials = ''

    for item in name_split:
        initials = initials + item[0]

    return initials.upper()

def main():
    get_initials(fullname)

if __name__ == "__main__":
    main()
