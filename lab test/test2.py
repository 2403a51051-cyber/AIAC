import re

def extract_emails(text):
	"""
	Extracts all email addresses from a block of text using regular expressions.
	"""
	pattern = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]+'
	return re.findall(pattern, text)


# Ask user for input
user_text = input("Enter text to extract email addresses from: ")
emails = extract_emails(user_text)
print("Extracted emails:", emails)
