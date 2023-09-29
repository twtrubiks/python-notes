"""
https://pypi.org/project/Faker/

pip install Faker

https://faker.readthedocs.io/en/master/locales/zh_TW.html
"""


from faker import Faker
from datetime import datetime
fake = Faker(locale='zh_TW')

for _ in range(10):
    # print(fake.company_prefix())
    print(fake.name())
    # print(fake.first_name())
    # print(fake.last_name())
    # print(fake.language_name())
    # print(fake.email())
    # print(fake.city())
    # print(fake.user_agent())
    # print(fake.date())
    # print(fake.date_between())
    # print(fake.date_between(start_date=datetime(2023,1,1), end_date=datetime(2023,12,31)))
    # print(fake.image_url())
    # print(fake.user_agent())
    # print(fake.ipv4())
    # print(fake.ipv4_public())
    # print(fake.url())
    # print(fake.phone_number())

    # print(fake.address())
    # print(fake.text())