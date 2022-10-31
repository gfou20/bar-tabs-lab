class Tab:

  menu = {
    'wine': 30,
    'beer': 15,
    'Soft_drink': 10,
    'chicken_sandwich': 14,
    'hamburger': 18,
    'veggie_burger': 16,
    'dessert': 12
  }

  def init(self):
    self.total = 0
    self.items = []

  def add(self,item):
    self.items.append(item)
    self.total += self.menu[item]  

  def print_bill(self,tax,service):
    tax = (tax/100) * self.total
    service = (service/100) * self.total
    total = self.total + tax + service

    for item in self.items:
      print(f'{item:10} ${self.menu[item]}')

    print(f"Total: ${total:2f}")  
