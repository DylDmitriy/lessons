import argparse
import getpass

def parse_args():
    parser = argparse.ArgumentParser(description="command line client")
    subparser = parser.add_subparsers(dest='command', metavar='command')
    subparser.required = True
    parser.set_defaults(funct=argparser_handler)

    # Login
    sub_parser = subparser.add_parser("login", help="Login with email and password")
    sub_parser.add_argument('-u', dest='user', help='user.  If this argument is not passed it will be requested.')
    sub_parser.add_argument('-p', dest='password', help='password.If this argument is not passed it will be requested.')

    args = parser.parse_args()
    args.funct(args)

def argparser_handler(args):
    if (args.command == 'login'):
        login(args.user, args.password)


def login(user, password):
    if not user:
        user = input("User:")
    if not password:
        password = getpass.getpass()
    print("user:", user)
    print("password:", password)


def main():
    pass

if __name__ == '__main__':
    parse_args()
    main()
