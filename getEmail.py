from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from time import sleep
import getContactUrl
from bs4 import BeautifulSoup
import re
import clearEmail
import requests

def extract_company_contact_info(url):

    def remove_duplicates(string_array):
        unique_strings = set(string_array)
        return list(unique_strings)
    
    def extract_contact_info(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())

        email_links = soup.find_all(href=re.compile(r'mailto:'))
        href_email = [re.sub(r'mailto:', '', link.get('href')) for link in email_links]

        email_addresses.extend(href_email)
        
        email_addresses = remove_duplicates(email_addresses)

        return email_addresses

    def remove_email_duplicates(array):
        unique_strings = set()

        # Iterate over the array
        for email in array:
            # Convert the email to lowercase
            lowercase_email = email.lower()

            # Check if the lowercase email is already in the set
            if lowercase_email not in unique_strings:
                # Add the lowercase email to the set
                unique_strings.add(lowercase_email)

        # Convert the set back to a list
        unique_array = list(unique_strings)

        return unique_array

    emailAddresses_result = []
    emailAddresses_result_1 = []
    emailAddresses_result_2 = []
    emailAddresses_result_3 = []

    available_urls = getContactUrl.available_urls(url)
    for u in available_urls:
        try:
            email_addresses = extract_contact_info(u)
            if len(email_addresses) != 0:
                emailAddresses_result.extend(email_addresses)
        except:
            pass
   
    emailAddresses_result_1 = remove_duplicates(emailAddresses_result)
    emailAddresses_result_2 = clearEmail.clear_emails(emailAddresses_result_1)
    emailAddresses_result_3 = remove_email_duplicates(emailAddresses_result_2)

    if len(emailAddresses_result_3) == 0:
        print("No email address")
    if len(emailAddresses_result_3) != 0:
        print("Email Addresses:", emailAddresses_result_3)

    return emailAddresses_result_3

# email = extract_company_contact_info("https://www.specialistfence.net/")

# print(email)
