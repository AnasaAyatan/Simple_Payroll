# These rates are fictional (only loosely based on actual rates of 2013)
INCOME_TAX_RATE = 0.21
WEEKLY_EI_DEDUCTION = 120.00
WEEKLY_CP_DEDUCTION = 155.00

# Input
salaryString = input("Enter the employee's yearly salary: ")

# Determine salary for a two-week period
salary = float(salaryString) / 26  # Combine the calculation with the assignment

# Processing
incomeTax = salary * INCOME_TAX_RATE
eiDeduction = WEEKLY_EI_DEDUCTION * 2
cpDeduction = WEEKLY_CP_DEDUCTION * 2

# Output
print(f"Bi-Weekly Income Tax Deduction: ${incomeTax:.2f}")
print(f"Bi-Weekly EI Deduction: ${eiDeduction:.2f}")
print(f"Bi-Weekly CP Deduction: ${cpDeduction:.2f}")

totalWithholding = incomeTax + eiDeduction + cpDeduction
takeHomePay = salary - totalWithholding

print(f"Bi-Weekly Total money withholding: ${totalWithholding:.2f}")
print(f"Bi-Weekly Take-Home Pay: ${takeHomePay:.2f}")