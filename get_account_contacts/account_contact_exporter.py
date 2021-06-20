import requests
import csv
import sys

API_TOKEN = 'dG9rOjk4ZDNkNzk1XzA4MzBfNDhkYV9hNTdjX2Q3YmEwZDk2M2JmNToxOjA='
HEADERS = {'Authorization': 'Bearer ' + str(API_TOKEN), 'Accept': 'application/json'}
PATH_TO_FILE = sys.argv[1]


def open_csv():
    accounts_list = []

    with open(PATH_TO_FILE + 'company_contacts.csv', 'r',) as output_file:
        csv_reader = csv.reader(output_file)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                accounts_list.append(row[0])
        return accounts_list

ACCOUNT_IDS = open_csv()


class AccountCompanyContact(object):
    def __init__(self, account_id, company_name, customer_success, account_manager):
        self.account_id = account_id
        self.company_name = company_name
        self.customer_success = customer_success
        self.account_manager = account_manager


def get_account_company_contacts(account_ids):
    account_ids = ACCOUNT_IDS
    result_list = []
    for account_id in account_ids:
        cse_json = get_cse_json(account_id)
        company_name = get_company_name(cse_json)
        customer_success = get_account_cse(cse_json)
        account_manager = get_account_manager(get_salesforce_id(cse_json))
        account_management_contact = AccountCompanyContact(account_id,company_name, customer_success, account_manager)
        result_dict = account_management_contact.__dict__
        result_list.append(result_dict)
    return result_list


def get_cse_json(account_id):
    urlCSE = f"https://api.intercom.io/companies?company_id=" + str(account_id)
    cse_json = requests.get(url=urlCSE, headers=HEADERS).json()
    return cse_json

def get_company_name(cse_json):
    return cse_json['name']

def get_account_cse(cse_json):
    return cse_json['custom_attributes']['Customer Success Engineer']


def get_salesforce_id(cse_json):
    salesforce_id = cse_json['id']
    return salesforce_id


def get_account_manager(salesforce_id):
    urlAM = "https://api.intercom.io/companies/" + salesforce_id + "/contacts"
    responseAM = requests.get(url=urlAM, headers=HEADERS).json()
    return responseAM["data"][0]["custom_attributes"]['salesforce_owner_name']

def create_csv():
    account_company_contacts = get_account_company_contacts(ACCOUNT_IDS)
    keys = account_company_contacts[0].keys()
    with open(PATH_TO_FILE + 'company_contacts.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(account_company_contacts)


def main():
    csv_company_contacts = create_csv()
    return csv_company_contacts


if __name__ == '__main__':
    main()
