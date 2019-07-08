import os


def main():
    email = os.environ['FACEBOOK_EMAIL']
    password = os.environ['FACEBOOK_PASS']
    print(email, password)


if __name__ == '__main__':
    main()