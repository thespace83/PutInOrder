from analyzer import close_admission_campaign
from parser import parse_university


def main():
    university = parse_university()
    close_admission_campaign(university)


if __name__ == '__main__':
    main()
