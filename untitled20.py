from prettytable import PrettyTable

receipt= PrettyTable()
receipt.field_names = ['№','продукт','цена','количество','стоимость']

print(receipt)
