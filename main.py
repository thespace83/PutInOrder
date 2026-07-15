from analyzer import close_admission_campaign
from parser import parse_university


def main():
    close_admission_campaign(parse_university())


if __name__ == '__main__':
    main()
