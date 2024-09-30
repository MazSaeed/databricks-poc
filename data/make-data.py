import csv
from faker import Faker
import random
import os

# Initialize Faker instance
fake = Faker()

# Generate fake customer data
def generate_customer_data(num_customers=10):
    customers = []
    for _ in range(num_customers):
        customer = {
            'cust_id': fake.uuid4(),
            'cust_first_name': fake.first_name(),
            'cust_last_name': fake.last_name(),
            'cust_address': fake.address().replace("\n", ", ")  # Replace newlines with commas
        }
        customers.append(customer)
    return customers

# Generate fake transaction data
def generate_transaction_data(customers, num_transactions=50):
    transactions = []
    for _ in range(num_transactions):
        transaction = {
            'trans_id': fake.uuid4(),
            'trans_date': fake.date_between(start_date='-1y', end_date='today'),
            'trans_amt': round(random.uniform(10.0, 1000.0), 2),
            'sku_id': fake.ean(length=8),
            'cust_id': random.choice(customers)['cust_id']  # Link transaction to a random customer
        }
        transactions.append(transaction)
    return transactions

# Function to write customers to a CSV file
def write_customers_to_csv(customers, filepath):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['cust_id', 'cust_first_name', 'cust_last_name', 'cust_address'])
        writer.writeheader()
        writer.writerows(customers)

# Function to write transactions to a CSV file
def write_transactions_to_csv(transactions, filepath):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['trans_id', 'trans_date', 'trans_amt', 'sku_id', 'cust_id'])
        writer.writeheader()
        writer.writerows(transactions)

# Generate customers and transactions
customers = generate_customer_data(num_customers=10)
transactions = generate_transaction_data(customers, num_transactions=50)

# Specify the path where you want to save the CSV files
customer_csv_path = 'cust.csv'
transaction_csv_path = 'trans.csv'

# Write to CSV files at specified paths
write_customers_to_csv(customers, customer_csv_path)
write_transactions_to_csv(transactions, transaction_csv_path)

print(f"Customer data written to {customer_csv_path}")
print(f"Transaction data written to {transaction_csv_path}")