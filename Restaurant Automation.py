#This is Eugene's Restaurant automation with python programming

print("Hello, welcome to Eugene's Restaurant !!!!!\n")

name = input("Kindly Enter Your Name\n")

#Using logical operators and If Else Statements

if name == "Ben" or name== "Gladys" or name== "Loki":

    bad_customer = input("Are you a bad customer? Enter Yes/No\n")
    good_ratings = int(input("What is your rating out of 10?\n"))

    if bad_customer == "Yes" and int(good_ratings) < 5:
        print("\nYou're not welcome here "+ name +". Get out!!!")
        exit()
    else:
        print("You're a good customer. Come in!!!")

else:
    print("\n Hello " + name + ", thank you so much for coming in today")

#Restaurant Menu
Menu = ("What would you like to order today " + name +
        ". Here is a list of what we have available \n"
        "\nBanku \n"
        "Rice\n"
        "Omotuo\n"
        "Fried Rice\n"
        "Khebab\n")


print(Menu)

#Order input
order = input()

#Set the price for Food
if order == "Banku":
    price = 15
elif order == "Rice":
    price = 20
elif order == "Fried Rice":
    price = 25
elif order=="Omotuo":
    price= 30
elif order== "Khebab":
    price= 5

else:
    print("Sorry, Product not available")
    price = 0
    exit()


#Ask customer the number of orders preferred
quantity= input("Quantity of " + order + "?\n")

total = price * int(quantity)

print("Thank you. Your total is: " + str(total) + " Ghs")

print (name + ". You ordered for " + quantity + " " + order + ". We will have it sent to you!! " )

