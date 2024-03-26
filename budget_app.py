class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, cantidad, description=""):
        self.ledger.append({"cantidad": cantidad, "description": description})

    def ver_cuenta(self):
        return sum(item["cantidad"] for item in self.ledger)
    
    def check_funds(self, cantidad):
        return cantidad <= self.ver_cuenta()

    def transfer(self, cantidad, categoria_budget):
        if self.check_funds(cantidad):
            self.withdraw(cantidad, f"Transfer to {categoria_budget.category}")
            categoria_budget.deposit(cantidad, f"Transfer from {self.category}")
            return True
        return False

    def withdraw(self, cantidad, description=""):
        if self.check_funds(cantidad):
            self.ledger.append({"cantidad": -cantidad, "description": description})
            return True
        return False

    def display(self):
        articulos = ""
        encabezado = f"{self.category:*^30}\n"
        for articulo in self.ledger:
            articulos += f"{articulo['description'][:23]:23}{articulo['cantidad']:>7.2f}\n"
        total = f"Total: {self.ver_cuenta():.2f}"
        resultado_final = encabezado + articulos + total

        print(resultado_final)


def create_spend_chart(categorias):
    chart = "Percentage spent by category\n"
    
    
    gastos = []
    for i in categorias:
        gasto_toal = 0
        for j in category.cuenta:
            if j['cantidad'] < 0:
                gasto_total += j['cantidad']
        gastos.append((gasto_total, i.category))

    for gasto in gastos:
        gasto_total = sum(gastos[0] )
    gastos_avg = [int(gastos[0] / gasto_total * 100) for gasto in gastos]

    #chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for j in gastos_avg:
            bar = "o" if j >= i else " "
            chart += bar + "  "
        chart += "\n"

    chart += "    -" + "---" * len(categorias) + "\n"

 
    tamaño_max = max(len(n.category) for n in categorias)

    # Build the category name lines
    for i in range(max_name_length):
        chart += "     "
        for j in categories:
            if i < len(j.category):
                name_char = j.category[i] 
            else:
                name_char = " " 
            chart += name_char + "  "
        chart += "\n"
    chart = chart.rstrip("\n")

    return chart


def review_budget():
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    food.display()


def main():
    review_budget()


if __name__ == '__main__':
    main()