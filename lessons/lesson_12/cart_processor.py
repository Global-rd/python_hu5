

def calculate_total(prices:list[int]) -> float:

    total = 0

    for price in prices:

        service_fee = price * (10 / 100)
        total += price + service_fee

    return float(total)

def process_cart_items(customer_name: str, prices: list[int]) -> float:
    total_price = calculate_total(prices)
    print(f"Total price for {customer_name}: ${total_price:.2f}")
    return total_price