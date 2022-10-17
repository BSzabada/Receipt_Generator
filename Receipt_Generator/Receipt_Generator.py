
#Designer_T-shirt_Description
designer_t-shirt_description = ("Made of pima cotton. Available Size(s): S, M, M, XL ")

#Designer_T-shirt_Price
designer_t-shirt_price = 75.00

#Running_Shoes_Description
running_shoes_description = ("Lightweight, durable, comfortable. The soles are made of memory foam, they have proper ventilation, and ankle support. Available Size(s): 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12 ")

#Running_Shoes_Price
running_shoes_price = 200.00

#Baseball_Cap_Description
baseball_cap_description = ("Made of cotton. Adjustable velcro strap. Available Size(s): OS.")

#Baseball_Cap_Price
baseball_cap_price = 32.99

#Sales Tax
sales_tax = .088

#Customer Total
customer_one_total = 0

customer_one_total += designer_t-shirt_price

customer_one_total += running_shoes_price

customer_one_total += baseball_cap_price

customer_one_tax = customer_one_total * sales_tax

#Lovely Loveseat Description
customer_one_itemization = (lovely_loveseat_description + luxurious_lamp_description)

#Functions to Print the Receipt
print("Customer One Items: ")

print(customer_one_itemization)

print("Customer One Total: ")

print(customer_one_total)
