from cart_processor import process_cart_items

def main():

    payments = {
        "Alice": [10, 5, 6, 7, 8], #36 -> 39.6
        "Bob": [1, 4, 6], # 11 -> 12.1
        "Timmy": [10, 6, 6, 8, 9] #39 -> 42.9
    }

    for customer, prices in payments.items():
        process_cart_items(customer, prices)

if __name__ == "__main__":
    main()