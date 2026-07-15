from parser import parse_university
from analyzer import close_admission_campaign, Referral


def main():
    university: dict[str, Referral] = parse_university()
    for n in university:
        print(university[n])


if __name__ == '__main__':
    main()
