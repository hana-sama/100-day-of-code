from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pokemon", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "l"
print(table)