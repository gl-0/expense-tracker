format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
underline_start = "\033[4m"
underline_end = "\033[0m"

color_green_start = "\033[102m\033[30m"
color_green_end = "\033[0m"
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
import time 
# * ----------------------------------------------------------------
# * VARIABLES / LISTS

entry = 1
amount = None
category = None
details = None

category_list = ['Food', 'Travel', 'Entertainment', 'Holiday', 'Utilities']

# * DICTIONARY
expenses = {
    '1': {'amount': 100, 'category': 'Food', 'description': 'Weekly shop'},
#     #! 'key': {'value': money} 
    '2': {'amount': 300, 'category': 'Utilities', 'description': 'I eat too much'},
    '3': {'amount': 10, 'category': 'Travel', 'description': 'Train each day'},
    '4': {'amount': 40, 'category': 'Entertainment', 'description': 'Steam'},
    '5': {'amount': 45, 'category': 'Food', 'description': 'Eating out'}
}

# x = expenses['1'].get('category')
# print(x)

# * FUNCTIONS ------------------------------------------------------
# ! Adds (£) to start of string
def prepend(str, list):
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


def show_food():
    food_list = []
    print("\n")
    for i in expenses:
        if expenses[i]['category'] == 'Food':
            print(f"{expenses[i].get('category')}: £{expenses[i]['amount']} - {expenses[i]['description']}")
            food_list.append(expenses[i]['amount'])
    print(f"{color_green_start}{underline_start} Total Food Expenses:{underline_end}{color_green_end} £{sum(food_list)}\n")

# show_food()

def show_util():
    util_list = []
    print("\n")

    for i in expenses:
        if expenses[i]['category'] == 'Utilities':
            print(f"\n{expenses[i].get('category')}: £{expenses[i]['amount']} - {expenses[i]['description']}")
            util_list.append(expenses[i]['amount'])
    print(f"{color_green_start}{underline_start}Total Utility Expenses:{underline_end}{color_green_end} £{sum(util_list)}\n")
# show_util()

def show_travel():
    travel_list = []
    print("\n")

    for i in expenses:
        if expenses[i]['category'] == 'Travel':
            print(f"\n{expenses[i].get('category')}: £{expenses[i]['amount']} - {expenses[i]['description']}")
            travel_list.append(expenses[i]['amount'])
    print(f"{color_green_start}{underline_start}Total Travel Expenses:{underline_end}{color_green_end} £{sum(travel_list)}\n")
# show_travel()

def show_entertainment():
    entertainment_list = []
    print("\n")

    for i in expenses:
        if expenses[i]['category'] == 'Entertainment':
            print(f"\n{expenses[i].get('category')}: £{expenses[i]['amount']} - {expenses[i]['description']}")
            entertainment_list.append(expenses[i]['amount'])
    print(f"{color_green_start}{underline_start}Total Entertainment Expenses:{underline_end}{color_green_end} £{sum(entertainment_list)}\n")
# show_entertainment()

def show_holiday():
    holiday_list = []
    print("\n")

    for i in expenses:
        if expenses[i]['category'] == 'Holiday':
            print(f"\n{expenses[i].get('category')}: £{expenses[i]['amount']} - {expenses[i]['description']}")
            holiday_list.append(expenses[i]['amount'])
    print(f"{color_green_start}{underline_start}Total Holiday Expenses:{underline_end}{color_green_end} £{sum(holiday_list)}\n")
# show_holiday()
# * ----------------------------------------------------------------

# ? 1) welcome message

def message(string):
    for i in string:
        print(i, end="")


# ? 2) log expense

def expense_amount():
    for k, v in expenses.items():
        print("\nEntry ",k, "\n")
        for k2 in v:
            print(k2 + ":", v[k2])
    entry = str(input(f"\nNew Entry #: "))
    if entry == expenses.items():
        print("Entry already exists. Choose a different name. If a number was enetered, pick a number greater than the previous entry")
        entry = str(input("Entry #: "))
    else:
        print(entry)
    amount = int(input("Expense amount: (£)"))
    if not type(amount) is int and amount < 0:
        print("Not a number, try again")
        amount = int(input("Expense amount: (£)"))
    else:
        print(f"£{amount}")
    category = str(input("What is the expense category: \nFood, Travel, Entertainment, Holiday, Utilities: \n").capitalize())
    print(category)
    details = str(input("Description: "))
    print(details)
    expenses.update({entry: {'amount': amount, 'category': category, 'description': details}})
    for key, value in expenses.items():
        print(f"Entry {key}:\n{value}\n")


# ? 3) store data

def total_expenses():
    total = []

    for key, value in expenses.items():
        for value in expenses[key].values():
            if type(value) == int:
                # sum(value)
                # print(value)
                
                total.append(value)     # ! ADDS EXPENSE TO LIST
    print(f"\n\n{color_green_start}Outgoings: £{sum(total)}{color_green_end}")
    print(f"\nExpenses: {prepend("£", total)}\n")


# ? 4) display summary

def category_summary():
    
    category_menu = ["[0] Food", "[1] Utility", "[2] Travel", "[3] Entertainment", "[4] Holiday", "[5] All", "[6] Main Menu"]
    print("\n")
    for i in range(len(category_menu)):
        print(category_menu[i])
    option = int(input("\nWhich category would you like to view?\n"))
    match option:
        case 0:
            show_food()
            category_summary()
        case 1:
            show_util()
            category_summary()
        case 2:
            show_travel()
            category_summary()
        case 3:
            show_entertainment()
            category_summary()
        case 4:
            show_holiday()
            category_summary()
        case 5:
            total_expenses()
            category_summary()
        case 6:
            main_menu()
        # for key, value in expenses.items():
        #     for value in expenses[key].keys():
        #         if value == 'category':
        #             print(expenses[key]['category'])
    
# category_summary()



#! MENU ---------------

def main_menu():
    menu = ["[0] Log Expense", "[1] Total Outgoing", "[2] Total For Category", "[3] Exit"]
    for i in range(len(menu)):
        print(menu[i])
    option = int(input("Please choose an option using the num pad: "))
    match option:
        case 0:
            expense_amount()
            main_menu()
        case 1:
            total_expenses()
            main_menu()
        case 2:
            category_summary()
            main_menu()
        case 3:
            print("Goodbye.")
            exit()

def tracker_start():
    message(f"\n{color_green_start}Let's Get Smarter With Money.{color_green_end}\n\n")
    main_menu()

tracker_start()

# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")