import pandas


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

    return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# main routine goes here

# set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# get user data
product_name = not_blank("Product name: "
                         "The product name can't be blank. ")

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: "
                          "The component name can't be blank. ")
    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity: "
                         "The amount must be a whole number more than zero", int)

    price = num_check("How much for a single item? $"
                      "The price must be a whole number more than zero",
                      float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# find sub total
variable_sub = variable_frame['Cost'].sum()

# currency formatting
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# printing area

print(variable_frame)

print()

print("Variable Costs: ${:.2f}".format(variable_sub))
