# These rates are fictional (only loosely based on actual rates of 2013)
INCOME_TAX_RATE = 0.21
WEEKLY_EI_DEDUCTION = 120.00
WEEKLY_CP_DEDUCTION = 155.00

# input
salaryString = input("Enter the employee's yearly salary: ")  # Corrected the input string

# Convert the input to a floating-point number
salary = float(salaryString)

# Determine salary for a two-week period
salary /= 26  # Using shorthand for dividing by 26

# Processing
incomeTax = salary * INCOME_TAX_RATE

# Corrected the case of the print function (use lowercase 'print' instead of 'Print')
print("Bi-Weekly Income Tax Deduction: $" + str(incomeTax))

eiDeduction = WEEKLY_EI_DEDUCTION * 2

print("Bi-Weekly EI Deduction: $" + str(eiDeduction))

cpDeduction = WEEKLY_CP_DEDUCTION * 2

print("Bi-Weekly CP Deduction: $" + str(cpDeduction))

totalWithholding = incomeTax + eiDeduction + cpDeduction
takeHomePay = salary - totalWithholding

# Corrected the case of the print function (use lowercase 'print' instead of 'Print')
print("Bi-Weekly Total money withholding: $" + str(totalWithholding))
print("Bi-Weekly Take-Home Pay: $" + str(takeHomePay))