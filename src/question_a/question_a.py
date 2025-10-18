def get_assessment_value(value):
    return value *0.06

def get_tax_assessed(assessment_value):
    return (assessment_value/100) *0.72

#Main program
def main():
    actual_value = float(input("enter the actual value of the property: $"))

    assessment_value = get_assessment_value(actual_value)

    tax = get_tax_assessed(assessment_value)

    #Display results
    print(f"assessment value:  ${assessment_value:.2f}")
    print(f"property tax: ${tax:.2f}")

#Run the program
main()