import random
from faker import Faker
import pandas as pd

fake = Faker()

# Generate data for 2987 customers
num_customers = 2987

data = {
    'CustomerID': [fake.uuid4() for _ in range(num_customers)],
    'Name': [fake.name() for _ in range(num_customers)],
    'Age': [fake.random_int(min=18, max=80) for _ in range(num_customers)],
    'MonthlyBill': [round(random.uniform(30, 200), 2) for _ in range(num_customers)],
    'DataUsageGB': [round(random.uniform(1, 10), 2) for _ in range(num_customers)],
    'ContractMonths': [random.choice([12, 24, 36]) for _ in range(num_customers)],
    'DevicesOwned': [random.randint(1, 5) for _ in range(num_customers)],
    'Exited': [random.choice([0, 1]) for _ in range(num_customers)],  # 0: Did not exit, 1: Exited
    'PhoneNumber': [fake.phone_number() for _ in range(num_customers)],
    'EmailAddress': [fake.email() for _ in range(num_customers)],
    'City': [fake.city() for _ in range(num_customers)],
    'State': [fake.state() for _ in range(num_customers)],
    'ZipCode': [fake.zipcode() for _ in range(num_customers)],
    'PlanType': [random.choice(['Basic', 'Standard', 'Premium']) for _ in range(num_customers)],
    'TotalSpent': [round(random.uniform(100, 1000), 2) for _ in range(num_customers)],
    'CustomerSince': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_customers)],
    'LastInteraction': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_customers)],
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

print("Complete. Check 'data.csv'")

