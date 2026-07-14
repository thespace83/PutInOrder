from parser import parse_university
from analyzer import close_admission_campaign


def main():
    close_admission_campaign(parse_university())


if __name__ == '__main__':
    main()
