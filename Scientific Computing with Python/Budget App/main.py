class Category:
  withdraws = 0
  name = ''

  def __init__(self, name):
      self.name = name
      self.ledger = list()

  def __repr__(self):
      display_menu = self.name.center(30, '*') + '\n'
      for element in self.ledger:
          row = f"{element['description'][:23]:23}{element['amount']:7.2f}"
          display_menu += row + '\n'
      display_menu += "Total: " + str(self.get_balance())
      return display_menu

  def deposit(self, amount, description=''):
      deposit_list = {'amount': amount, 'description': description}
      self.ledger.append(deposit_list)

  def check_funds(self, amount):
      total_funds = 0
      for transactions in self.ledger:
          total_funds += transactions['amount']
      if float(total_funds) >= amount:
          return True
      else:
          return False

  def withdraw(self, amount, description=''):
      if self.check_funds(amount) is True:
          withdraw_list = {'amount': float(-amount), 'description': description}
          self.ledger.append(withdraw_list)
          self.withdraws += amount
          return True
      else:
          return False

  def get_balance(self):
      total = 0
      for transactions in self.ledger:
          total += transactions['amount']
      return total

  def transfer(self, amount, category_2):
      if self.check_funds(amount) is True:
          description_1 = f'Transfer to {category_2.name}'
          description_2 = f'Transfer from {self.name}'
          self.ledger.append({'amount': -1 * amount, 'description': description_1})
          self.withdraws += amount
          category_2.ledger.append({'amount': amount, 'description': description_2})
          return True
      else:
          return False


def create_spend_chart(categories):
  chart = 'Percentage spent by category\n'
  category = Category
  expenses = dict()
  total = 0
  percentage = []
  count = 0
  max_len = 0
  for category in categories:
      expenses[category.name] = category.withdraws
      total += category.withdraws
      count += 1

  for k, v in expenses.items():
      percentage.append(v / total * 100)
      if len(k) > max_len:
          max_len = len(k)

  for i in range(100, -1, -10):
      chart += f'{str(i).rjust(3)}|'
      for percent in percentage: 
          if percent > i:
              chart += ' o '  
          else:
              chart += ' ' * 3
      chart += " \n"

  chart += '    ' + ('-' * (count * 3 + 1)) + '\n'
  for i in range(max_len):
      chart += ' ' * 4
      for k in expenses.keys():
          name = 1
          if i < len(k):
              chart += ' ' + k[i] + ' '
          else:
            chart += " " * 3  
      chart += " \n"     
  return chart.rstrip("\n") 















