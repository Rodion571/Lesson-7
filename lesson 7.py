# Task 1
def count_words(text):
    words = text.lower().split()
    word_count = {word: words.count(word) for word in set(words)}
    return word_count
input_text = "Hello world! Hello everyone. Welcome to the world of Python."
word_count = count_words(input_text)
print(word_count)
# task 2
def simple_translator():
    translation_dict = {
        'hello': 'привіт',
        'world': 'світ',
        'python': 'пітон',
        'programming': 'програмування',
        'translator': 'перекладач'
    }
    while True:
        word = input("Enter word in translation (or 'ext' on close): ").lower()
        if word == 'exit':
            print("Good bye!")
            break
        translation = translation_dict.get(word)
        if translation:
            print(f"Translation word '{word}': {translation}")
        else:
            print(f"Translation word '{word}' not found.")
simple_translator()
# Task 3
def contact_manager():
    contacts = {}
    while True:
        print("\nMenu:")
        print("1. Enter new contact")
        print("2. Delete contact")
        print("3. Get a phone number by name")
        print("4. Exit")
        choice = input("Select the option (1-4): ")
        if choice == '1':
            name = input("Enter name contact: ")
            phone_number = input("Enter number phone: ")
            print(f"Contact '{name}' added.")
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print(f"Contact '{name}' not found.")
        elif choice == '3':
            name = input("Enter a contact name to get a phone number: ")
            phone_number = contacts.get(name)
            if phone_number:
                print(f"Phone number for contact '{name}': {phone_number}")
            else:
                print(f"Contact '{name}' not found.")
        elif choice == '4':
            print("Good bye!")
            break
        else:
            print("Wrong choice. Please try again.")
contact_manager()
# Task 4
def currency_converter():
    exchange_rates = {
        'USD': 1.0,  # Курс для доллара США
        'EUR': 0.85,  # Курс для евро
        'UAH': 41.50,  # Курс для украинской гривны
        'GBP': 0.75  # Курс для британского фунта
    while True:
        print("\nMenu:")
        print("1. Convert currency")
        print("2. Go out")
        choice = input("Select the option (1-2): ").strip()
        if choice == '1':
            amount = float(input("Enter the amount to convert: ").strip())
            from_currency = input("Enter the currency to convert from (USD, EUR, UAH, GBP): ").strip().upper()
            to_currency = input("Enter the currency to convert to (USD, EUR, UAH, GBP): ").strip().upper()
            if from_currency in exchange_rates and to_currency in exchange_rates:
                base_amount = amount / exchange_rates[from_currency]
                converted_amount = base_amount * exchange_rates[to_currency]
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                print("Incorrect currency.")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Wrong choice. Please try again.")
currency_converter()
