# https://youtu.be/k8asfUbWbI4

import datetime as dt
import calendar

balance = 5_000  # credit card balance you owe the bank
interest_rate_annual = 15 * .01  # 15% on credit card
terms_annual = 12  # 12 terms per year
monthly_pmt = 200  # fixed monthly payment

today = dt.date.today()  # We ONLY want the date this time (⚡️ now())

# 😎 Leverage the built-in calendar module from the standard library
# DO NOT reInvent your wheel

# 🧠 calendar.monthrange()
# Get the number of days in current month automatically!
# 👀 NOTE: this will be the "immutable" tuple! And ONLY grab the [1] element

days_in_curr_month = calendar.monthrange(today.year, today.month)[1]

print(days_in_curr_month)  # (1, 31) -> 1 = Tuesday

# 👀 Remember: all attributes ends with .attribute (E.g. today.day)
days_till_end_month = days_in_curr_month - today.day

print(days_till_end_month)

# 🧠 datetime.timedelta()
# Create time delta Δ for duration difference

start_date = today + dt.timedelta(days=days_till_end_month + 1)
end_date = start_date  # 🏃‍♂️ Will increment the end_date throuhg out the script

# Simulate the 💸 Payment Loop

while balance > 0:
    """1st - add the interest accumulated from the previous month"""
    interest_charge = (interest_rate_annual/terms_annual) * balance
    balance += interest_charge

    """2nd - subtract the monthly payment we contribute"""
    balance -= monthly_pmt

    """3d - round the balance into 2 decimal places, and ALWYS be sure no-negative"""
    balance = 0 if balance < 0 else round(balance, 2)

    # 🎯 How to adjust print output with fixed length (E.g. $ _370.51 $___0.00)
    print(f'{end_date}, $ {balance:,.2f}')

    days_in_curr_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date += dt.timedelta(days=days_in_curr_month)
