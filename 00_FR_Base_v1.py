# import libraries

# functions go here

# checks that input is either a float or and integer that is more than zero.
# takes iin custom error message
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


# checks that user entered either yes or no
def yes_no(question):

    to_check = ['yes', 'no']

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no\n")

# main routine goes here
get_int = num_check("How many do you need? ",
                    "Please enter an amount more than 0\n", int)

get_cost = num_check("How much does it cost? $",
                     "Please enter a number more than 0\n", float)

print("You need: {}".format(get_int))
print("It costs: ${}".format(get_cost))