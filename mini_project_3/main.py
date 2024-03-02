from fpdf import FPDF
import pandas as pd

df = pd.read_csv('articles.csv', dtype={'id': str})

class Product:
    def __init__(self, product_id):
        self.product_id = product_id
        self.product_name = df.loc[df['id'] == self.product_id, 'name'].squeeze()
        self.product_price = df.loc[df['id'] == self.product_id, 'price'].squeeze()

    def available(self):
        in_stock = self.product_stock = df.loc[df['id'] == self.product_id, 'in stock'].squeeze()
        if in_stock > 0:
            return True
        else:
            return False
        
    def adjust_inventory_after_purchase(self):
        df.loc[df['id'] == self.product_id, 'in stock'] -= 1
        df.to_csv('articles.csv', index=False)

    def details_of_purchase(self):
        content = f"""
        Please confirm details of the purchase as follows:
        Product ID: {self.product_id}
        Product Name: {self.product_name}
        product Price: ${self.product_price} per unit
        """
        print(content)

    def create_invoice(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.product_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.product_name.title()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.product_price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
if __name__ == "__main__":
    choice = input("Please choose the id of an article to buy: ")
    product = Product(product_id=choice)
    if product.available():
        product.adjust_inventory_after_purchase()
        product.details_of_purchase()
        product.create_invoice()
    else:
        print("The product you sought was out of stock right now. Please come back later!")

print(df)