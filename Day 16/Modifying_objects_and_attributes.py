from prettytable import PrettyTable  # Here prettytable is a package and PrettyTable is a class.

table = PrettyTable()  # here x is an object of PrettyTable Class.

table.add_column("Pokemon Name", ["Pikachu", "Squirtel", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table.align)


print(table)


