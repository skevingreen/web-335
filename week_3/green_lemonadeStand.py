""" 
    Title: green_lemonadeStand.py
    Author: Scott Green
    Date: 1238 January 2025
    Description: Lemonade Stand Simulator
"""

""" @method: calculate_cost.
    @description: Method to calculate the cost to operate lemonade stand. 
    @params: lemons_cost, sugar_cost
    @returns: integer value.
"""
def calculate_cost(lemons_cost, sugar_cost):
  total_cost = lemons_cost + sugar_cost   # calculate the total cost

  return total_cost   # return the total cost

""" @method: calculate_profit.
    @description: Method to calculate the profit from operating lemonade stand. 
    @params: lemons_cost, sugar_cost, selling_price
    @returns: integer value.
"""
def calculate_profit(lemons_cost, sugar_cost, selling_price):
  profit = selling_price - calculate_cost(lemons_cost, sugar_cost)  # calculate the profit

  return profit # return the profit

""" Variables for cost and sales """
lemons_cost = 5
sugar_cost = 3
total_sales = 20

""" Variables to hold the values from the above methods. """
total_cost = calculate_cost(lemons_cost, sugar_cost)
total_profit = calculate_profit(lemons_cost, sugar_cost, total_sales)

""" Variable to hold the string output. """
#output = "Total Cost: {0}\nTotal Profits: {1}".format(total_cost, total_profit)  #alternative output
output = "${0} lemons + ${1} sugar = ${2} total cost\n${3} total sales - ${4} total cost = ${5} total profit".format(lemons_cost, sugar_cost, total_cost, total_sales, total_cost, total_profit)

print(output)