# Few-shot examples:
# Example 1: convert_currency(100, 'USD', 'EUR', {'USD': 1, 'EUR': 0.92}) -> 92.0
# Example 2: convert_currency(50, 'EUR', 'USD', {'USD': 1, 'EUR': 0.92}) -> 54.35
# Example 3: convert_currency(200, 'USD', 'JPY', {'USD': 1, 'JPY': 110}) -> 22000.0

def convert_currency(amount, from_currency, to_currency, rates):
	"""
	Converts an amount from one currency to another using exchange rates stored in a dictionary.
	rates: dictionary with currency codes as keys and their rates relative to a base currency.
	"""
	if from_currency not in rates or to_currency not in rates:
		raise ValueError("Currency not found in rates dictionary.")
	# Convert amount to base currency, then to target currency
	base_amount = amount / rates[from_currency]
	converted = base_amount * rates[to_currency]
	return round(converted, 2)


# Ask user for input
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

# Example rates dictionary (can be expanded or replaced with user input)
rates = {'USD': 1, 'EUR': 0.92, 'JPY': 110}

try:
	result = convert_currency(amount, from_currency, to_currency, rates)
	print(f"{amount} {from_currency} is {result} {to_currency}")
except ValueError as e:
	print(e)
