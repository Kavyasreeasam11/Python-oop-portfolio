class Product:
      def __init__(self,product_id : str,name : str,price :float,stock :int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock =stock
      def reduce_stock(self,qty):
         if qty>self.stock:
            raise ValueError("Stock not enough")
         else:
            self.stock -=qty
            print(f"Stock updated for {self.name} new stock is {self.stock}")
      def __str__(self):
         return f"{self.name} - ${self.price} (In stock : {self.stock})"
class ShoppingCart:
   def __init__(self,customer_name:str):
      self.customer_name = customer_name
      self.items = {}
   def add_item(self,product_obj,qty):
      if qty <= 0:
        raise ValueError("Enough Stock not available")
        return
      if qty>product_obj.stock:
         print(f"Cannot add {qty} x {product_obj.name}. Only {product_obj.stock} left in stock.")
         return
      if product_obj in self.items:
         self.items[product_obj] += qty
      else:
         self.items[product_obj] = qty
            
      print(f" Added {qty} x {product_obj.name} to {self.customer_name}'s cart.")
            
   
   def calculate_total(self):
      total = 0
      for product_obj,quantity in self.items.items():
         total+=product_obj.price * quantity
      return total
   def apply_coupon(self,coupon_code):
      current_total = self.calculate_total()
      if coupon_code == "SAVE10":
         discount = current_total*0.10
         return current_total-discount
      else:
         print(f"Invalid Coupon")
         return current_total
def main():
    p1 = Product("L1", "Laptop", 1000.00, 2)
    p2 = Product("M1", "Mouse", 50.00, 10)
    p3 = Product("E1", "Headphones", 100.00, 0)

    c1 = ShoppingCart("Kavya")

    print("\n--- Test Scenario 1: Adding Out of Stock Item ---")
    c1.add_item(p3, 1) 

    print("\n--- Test Scenario 2: Adding Valid Items ---")
    c1.add_item(p1, 1)  
    c1.add_item(p2, 2) 

    print("\n--- Test Scenario 3: Exceeding Available Stock ---")
    c1.add_item(p1, 5)  

    print("\n--- Test Scenario 4: Calculations & Coupons ---")
    subtotal = c1.calculate_total()
    print(f" Cart Subtotal: ${subtotal}")
    
    final_price = c1.apply_coupon("SAVE10")
    print(f" Final Price with 'SAVE10' Coupon: ${final_price}")


if __name__ == "__main__":
    main()
