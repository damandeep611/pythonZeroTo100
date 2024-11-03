from pathlib import Path
import pandas as pd
import csv
from datetime import datetime


current_dir = Path.cwd()
print(f"current working directory is : {current_dir}")

file_path = current_dir.parent / 'dataset' / 'ADANIPORTS.csv'
df = pd.read_csv(file_path)

def load_stock_prices(csv_file_path):
  try:
    with open(file_path, 'r') as file:
      csv_reader  = csv.DictReader(file)
      # get the first row(most recent date)
      row = next(csv_reader)
      return float(row['Close'])
  except FileNotFoundError:
    print(f"CSV file not found: {csv_file_path}")
    return None
  except StopIteration:
    print("CSV file is empty")
    return None
  except Exception as e:
    print(f"Error reading CSV file: {e}")
    return None

def load_portfolio():
  try:
    with open(file_path, 'r') as file:
      port



