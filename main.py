import pandas as pd

def load_data():
   data = pd.read_excel('your_file.xlsx')
   return data

def analyze_data(data):
   correlation = data['seling_price'].corr(data['production_price'])
   print(f"Correlation between selling price and production price: {correlation}")

def main():
   data = load_data()
   data = clear_data(data)
   analyze_data(data)

if __name__ == '__main__':
   main()
