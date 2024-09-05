#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, item, price, quantity = 0):
    self.items.append(item)
    self.total += price * quantity
    return self.total

  def get_total(self):
    return self.total

  def clear(self):
    self.total = 0
    self.discount = 0
    self.items = []


# add_item = CashRegister()
# add_item.add_item(1.99)
# add_item.add_item(1.99)
  # pass
