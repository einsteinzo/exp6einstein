def calculate_taxable_income(income, deductions):
    return max(income - deductions, 0)

def calculate_tax(taxable_income):
    # Simple progressive tax brackets (for example purposes)
    if taxable_income <= 10275:
        return taxable_income * 0.10
    elif taxable_income <= 41775:
        return 1027.5 + (taxable_income - 10275) * 0.12
    elif taxable_income <= 89075:
        return 4807.5 + (taxable_income - 41775) * 0.22
    else:
        return 15213.5 + (taxable_income - 89075) * 0.24

def main():
    print("Welcome to the Tax Filing System")
    income = float(input("Enter your total annual income: $"))
    deductions = float(input("Enter your total deductions: $"))

    taxable_income = calculate_taxable_income(income, deductions)
    tax_owed = calculate_tax(taxable_income)

    print(f"\n--- Tax Summary ---")
    print(f"Gross Income: ${income:,.2f}")
    print(f"Deductions:   ${deductions:,.2f}")
    print(f"Taxable Income: ${taxable_income:,.2f}")
    print(f"Estimated Tax Owed: ${tax_owed:,.2f}")

if __name__ == "__main__":
    main()
