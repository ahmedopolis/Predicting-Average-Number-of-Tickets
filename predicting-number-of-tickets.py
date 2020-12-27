#Problem: The new client has 732 employees, with a contract value that is worth $825,000, and is in the services industry.
# Your company currently has 23 help desk resources on staff, and each resource has a capacity of 125 tickets per week.
# The current average number of tickets that the help desk has been receiving is 2800 per week.
# Based on the Alteryx output: 

import math

Intercept_B0 = -18.45
No_employees_B1 = 0.116
Value_of_Contract_B2 = 0.0004858
Industry_Manufacturting_B4 = 0
Industry_Retail_B5 = -8.725
Industry_Services_B6 = 12.49

# Predict number of average tickets from new client:

def calculate_number_of_tickets(No_Employees,Value_of_Contract,Industry):
    category_product = 0
    Industry = Industry.lower()
    if(Industry == "retail"):
        category_product = Industry_Retail_B5
    elif(Industry == "services"):
        category_product = Industry_Services_B6
    else:
        category_product = Industry_Manufacturting_B4
    predicted_number_of_tickets = Intercept_B0 + No_employees_B1*No_Employees + Value_of_Contract_B2*Value_of_Contract + category_product
    predicted_number_of_tickets_round = math.ceil(predicted_number_of_tickets)
    print(f"The number of predicted of average tickets for the prescribed hypothetical client is: {predicted_number_of_tickets_round}.")
    return predicted_number_of_tickets

number_of_tickets = calculate_number_of_tickets(732,825000,"Services")

# Predict number of helpdesk needed:

No_helpdesk = 23
Helpdesk_individual_weekly_capacity = 125
Current_average_number_of_tickets = 2800

def calculated_number_of_helpdesk_needed(number_of_tickets):
    number_of_helpdesk_needed = 0
    Helpdesk_weekly_capacity = No_helpdesk*Helpdesk_individual_weekly_capacity
    New_current_number_of_tickets = Current_average_number_of_tickets + number_of_tickets
    Number_of_tickets_difference = Helpdesk_weekly_capacity - New_current_number_of_tickets
    if(Number_of_tickets_difference == 0):
        print("The number of new helpdesk support staff needed is 0.")
    elif(Number_of_tickets_difference < 0):
        number_of_helpdesk_needed = (-1)*(Number_of_tickets_difference/Helpdesk_individual_weekly_capacity)
        number_of_helpdesk_needed = math.ceil(number_of_helpdesk_needed)
        print(f"The number of new helpdesk support staff needed is {number_of_helpdesk_needed}.")
    elif(Number_of_tickets_difference > 0):
        number_of_helpdesk_needed = (Number_of_tickets_difference/Helpdesk_individual_weekly_capacity)
        number_of_helpdesk_needed = math.ceil(number_of_helpdesk_needed)
        print(f"The number of helpdesk support staff in surplus is {number_of_helpdesk_needed}.")

calculated_number_of_helpdesk_needed(number_of_tickets)

