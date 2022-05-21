def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    valor_dollar = d.replace("$", "")
    return valor_dollar

def percent_to_float(p):
    p_percent = p.replace("%", "")
    valor_percent = float(p_percent) / 100
    return valor_percent


main()