# from decimal import Decimal
# import requests

# def fetch_exchange_rates():
#     response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
#     data = response.json()
#     return {
#         'INR': Decimal(data['rates']['INR']),
#         'NGN': Decimal(data['rates']['NGN'])
#     }

# exchange_rates = fetch_exchange_rates()

# def get_usd_to_inr_rate():
#     return exchange_rates['INR']

# def get_usd_to_ngn_rate():
#     return exchange_rates['NGN']

# def convert_usd_to_inr(usd_amount):
#     inr_rate = get_usd_to_inr_rate()
#     return usd_amount * inr_rate

# def convert_usd_to_kobo(usd_amount):
#     ngn_rate = get_usd_to_ngn_rate()
#     ngn_amount = usd_amount * ngn_rate
#     return int(ngn_amount * 100)  # Convert NGN to Kobo

# def convert_usd_to_ngn(usd_amount):
#     ngn_rate = get_usd_to_ngn_rate()
#     return usd_amount * ngn_rate


from decimal import Decimal
# import requests  # Commented out since we're not using API calls

def fetch_exchange_rates():
    # API call commented out for offline development
    # response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    # data = response.json()
    # return {
    #     'INR': Decimal(data['rates']['INR']),
    #     'NGN': Decimal(data['rates']['NGN'])
    # }
    
    # Static exchange rates for offline use
    return {
        'INR': Decimal('83.25'),  # 1 USD = 83.25 INR (approximate)
        'NGN': Decimal('1570.50')  # 1 USD = 1570.50 NGN (approximate)
    }

exchange_rates = fetch_exchange_rates()

def get_usd_to_inr_rate():
    return exchange_rates['INR']

def get_usd_to_ngn_rate():
    return exchange_rates['NGN']

def convert_usd_to_inr(usd_amount):
    inr_rate = get_usd_to_inr_rate()
    return usd_amount * inr_rate

def convert_usd_to_kobo(usd_amount):
    ngn_rate = get_usd_to_ngn_rate()
    ngn_amount = usd_amount * ngn_rate
    return int(ngn_amount * 100)  # Convert NGN to Kobo

def convert_usd_to_ngn(usd_amount):
    ngn_rate = get_usd_to_ngn_rate()
    return usd_amount * ngn_rate

# Test the functions to make sure everything works
if __name__ == "__main__":
    print("=== OFFLINE CURRENCY CONVERTER ===")
    print(f"USD to INR rate: {get_usd_to_inr_rate()}")
    print(f"USD to NGN rate: {get_usd_to_ngn_rate()}")
    print()
    
    # Test conversions
    test_amount = Decimal('100')
    print(f"${test_amount} USD =")
    print(f"  ₹{convert_usd_to_inr(test_amount)} INR")
    print(f"  ₦{convert_usd_to_ngn(test_amount)} NGN")
    print(f"  {convert_usd_to_kobo(test_amount)} Kobo")
    print()
    print("✓ All functions working offline!")
