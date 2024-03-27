def solution(A, D, N):
    total_income = 0
    total_card_payments = {}

    
    for amount, date in zip(A, D):

        if amount >= 0:
            total_income += amount

        
        if amount < 0:
            month = date[:7]  
            if month not in total_card_payments:
                total_card_payments[month] = 0
            total_card_payments[month] += abs(amount)

    
    balance = total_income
    for month in range(1, 13):
        month_str = f'2020-{month:02d}'
        card_payment_total = total_card_payments.get(month_str, 0)

        
        if card_payment_total < 100 or len(total_card_payments) < 3:
            balance -= 5

    
    balance -= sum(A)

    return balance