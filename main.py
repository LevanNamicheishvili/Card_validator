def validate_card_number(card_number):
    # Remove any non-digit characters
    card_number = ''.join(c for c in card_number if c.isdigit())

    # Reverse the card number
    reversed_card_number = card_number[::-1]

    # Calculate the Luhn checksum
    total = 0
    for i, digit in enumerate(reversed_card_number):
        if i % 2 == 1:
            double = int(digit) * 2
            total += double // 10 + double % 10
        else:
            total += int(digit)

    # Check if the total is divisible by 10
    return total % 10 == 0


card_number = "4111111111111111"

if validate_card_number(card_number):
    print("Card number is valid.")
else:
    print("Card number is invalid.")
