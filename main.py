from analyzer import close_admission_campaign
from parser import parse_university


def main():
    university = parse_university()

    university = close_admission_campaign(university)

    for referral in university.referrals:
        print(f'R: {referral.name} // {referral.number_of_places}')
        for applicant in university.result[referral.name]:
            print(f'{applicant.uuid} // {applicant.amount_of_points}')


if __name__ == '__main__':
    main()
