# calculating weekly pay 

wage = eval(input("What is your hourly wage: "))
hours = eval(input("How many hours did you work: "))

if hours <= 40:
    weekly_wage = wage*hours
    weekly_wage_after_tax = weekly_wage - (weekly_wage*0.13)
    monthly_wage = (weekly_wage * 4)
    monthly_wage_after_tax = (weekly_wage * 4) - ((weekly_wage*0.13) * 4)

else:
    weekly_wage = (wage*(40)) + ((hours - 40)*(wage*.5))
    weekly_wage_after_tax = weekly_wage - (weekly_wage*0.13)
    monthly_wage = (weekly_wage * 4)
    monthly_wage_after_tax = (weekly_wage * 4) - ((weekly_wage*0.13) * 4)

print("\nWeekly earnings before tax are $", weekly_wage)
print("Weekly earnings after tax are are $", weekly_wage_after_tax)

print("Monthly eanings after tax are $", monthly_wage)
print("Monthly earnings after tax are are $", monthly_wage_after_tax)