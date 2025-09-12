# finance_calculator.py

# Ask the user to enter their monthly income
# input() collects text, so we convert it to float for calculations
monthly_income = float(input("Enter your monthly income: "))

# Ask the user to enter their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings (income minus expenses)
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
# Step 1: monthly_savings * 12 = total savings in one year
# Step 2: (monthly_savings * 12 * 0.05) = interest earned in one year
# Step 3: Add them together for projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Show the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
