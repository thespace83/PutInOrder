from analyzer import University
from parser import parse_university


def main():
    university: University = parse_university()
    for applicant in university.applicants:
        print(applicant)


if __name__ == '__main__':
    main()
