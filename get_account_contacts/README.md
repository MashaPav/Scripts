### Company's contacts at logz.io (customer success engineer and account manager)

This script gets data from Intercom API and accepts 'company_contacts.csv' file as an input with account id's on logz.io as a column.

To Run this script, please do the following:

#### 1. Clone the script from 'Scripts' repo:
```shell
git clone 
```
#### 2. Get into the get_account_contacts directory:
```shell
cd get_account_contacts
```
#### 3. Update the company_contacts.csv file with the account id's you want to get details for.
*Note:* If there is no information for one of the company id's, the script will stop executing with an error.

#### 4. Insert the account id's to the account_id column and run the script:
```shell
python3 account_contact_exporter.py <<path_to_company_contacts.csv>>
```

**Note:** There is no need to pass the file name (path_to_company_contacts.csv) in the above command, just the path. Example: 
```shell
python account_contact_exporter.py /Users/mashap/Desktop/
```
