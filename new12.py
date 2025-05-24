import requests

class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    def get_rates(self):

        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        data = response.json()

        for item in data:
            self.rates[item['cc']] = item['rate']
        self.rates["UAH"] = 1.0

    def convert(self, amount, from_currency, to_currency):

        if from_currency != "USD":
            amount = amount / self.rates[from_currency]
        return round(amount * self.rates[to_currency], 2)


converter = CurrencyConverter()
converter.get_rates()

while True:
    try:

        amount = float(input("Введіть суму валюти: "))
        from_currency = input("Введіть код валюти (наприклад, UAH, EUR, PLN): ").upper()


        converted_amount = converter.convert(amount, from_currency, "USD")
        print(f"{amount} {from_currency} = {converted_amount} USD")
        break

    except KeyError:
        print(" Неправильний код валюти. Спробуйте ще раз.")
    except ValueError:
        print("❌Введено некоректну суму. Спробуйте ще раз.")
