#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, item, price, quantity = 1):
    self.items.append((item, price, quantity))
    self.total += price * quantity
    return self.total
  
  def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

  def get_total(self):
    return self.total
  
  def get_items(self):
    return self.items

  def subtract_last_item(self):
        if self.items:
            last_item = self.items.pop()
            item_name, price, quantity = last_item
            self.total -= price * quantity
        return self.total

  def clear(self):
    self.total = 0
    self.discount = 0
    self.items = []
  # pass


register = CashRegister(discount=10)
register.add_item("eggs", 1.99, 2)
register.add_item("milk", 2.99, 1)
print("Total:", register.get_total())
# add_item = CashRegister()
# add_item.add_item(1.99)
# add_item.add_item(1.99)