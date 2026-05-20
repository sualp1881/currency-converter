def get_rates():
    """Static exchange rates based on USD."""
    return {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "TRY": 32.5,
        "JPY": 149.5,
        "CAD": 1.36,
        "AUD": 1.53,
        "CHF": 0.90,
        "CNY": 7.24,
        "INR": 83.1,
    }

def convert(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another."""
    in_usd = amount / rates[from_currency]
    return in_usd * rates[to_currency]

def display_currencies(rates):
    """Display available currencies."""
    print("\n  Available currencies:")
    currencies = list(rates.keys())
    for i in range(0, len(currencies), 5):
        row = currencies[i:i+5]
        print("  " + "  ".join(f"{c}" for c in row))

def get_currency(prompt, rates):
    """Get a valid currency from user."""
    while True:
        currency = input(prompt).upper().strip()
        if currency in rates:
            return currency
        print(f"  ⚠️  Invalid currency! Choose from: {', '.join(rates.keys())}")

def main():
    print("=" * 50)
    print("   💱 CURRENCY CONVERTER")
    print("   Rates based on USD (static)")
    print("=" * 50)

    rates = get_rates()

    while True:
        display_currencies(rates)

        try:
            amount = float(input("\n  Enter amount: "))
        except ValueError:
            print("  ⚠️  Please enter a valid number!")
            continue

        from_currency = get_currency("  From currency: ", rates)
        to_currency = get_currency("  To currency: ", rates)

        result = convert(amount, from_currency, to_currency, rates)

        print("\n" + "=" * 50)
        print(f"  💰 {amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")
        print(f"  📊 Rate: 1 {from_currency} = {rates[to_currency]/rates[from_currency]:.4f} {to_currency}")
        print("=" * 50)

        again = input("\n  🔄 Convert again? (yes/no): ").lower().strip()
        if again not in ["yes", "y"]:
            print("\n  👋 Goodbye!\n")
            break

if __name__ == "__main__":
    main()
