from dbfread import DBF

from auto_forms import fill_form

from validator import sale_validator

def load_valid_sales():
    sales = DBF("sales.dbf")

    # creating a empty array to storage valid sales

    valid_sales = []

    # validating each sale and adding to array valid_sales
    for record in sales:
        if sale_validator(record):
            valid_sales.append(record)

    return valid_sales


#loading valid sales on a variable

sales = load_valid_sales()

for sale in sales:
    print("Preenchendo o formulário de ", sale["FULL_NAME"])
    #filling the form
    fill_form(sale)


print("finalizado")
input()

