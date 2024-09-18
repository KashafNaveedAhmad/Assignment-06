# ASSIGNMENT NO 06
# Let's start the assignment-0
import array

# QUESTION NO 1:
# array starts from '0'.

print("\nLet's start the assignment!")
print("\n -> PART NO 1:")
print("I've created an intial array to make the insertion more visible.\nHaving the values:\n'arr=[1,2,3,4,5]'\n")
def value_adding(arr,arr_index:int,value_add:int):
    arr.insert(arr_index,value_add)
    return arr

arr=array.array('i',[1,2,3,4,5])
arr_index=int(input(("ENTER THE 'INDEX' TO INSERT VALUE:")))
value_add=int(input("ENTER THE 'VALUE' TO INSERT AT INDEX:"))
modified_array=value_adding(arr,arr_index,value_add)
print(modified_array.tolist())
# the '.tolist()' will simply convert it into int.(simpler display)
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION NO 2:

print("\n -> PART NO 2:\n")
def item_add(user):
    items=str(input("ENTER THE ITEMS YOU WANT TO ADD BELOW!\n(NOTE: USE COMMA) :"))
    item_list = [item.strip() for item in items.split(',')] 
    user.extend(item_list) 
    print(f"YOUR CART HAS ITEMS:{user}")
def item_remove(user):
    print("YOUR CART HAS ITEMS:",user)
    print("Note: THE ITEM NUMBER STARTS FROM '0'(left side).")
    item_remove_index=int(input("\nENTER THE ITEM NUMBER YOU WANT TO REMOVE:"))
    if 0 <= item_remove_index < len(user):
            removed_item = user.pop(item_remove_index)
            print(f"THE ITEM '{removed_item}' IS REMOVED FROM YOUR CART")
    else:
        ("\nYOUR LIST IS EMPTY\n")
    print(f"YOUR CART HAS ITEMS:{user}")
def item_update(user):
    print("YOUR CART HAS ITEMS:",user)
    items=input("\nENTER THE ITEMS YOU WANT TO ADD TO YOUR ALREADY MADE CART BELOW:")
    print("\n(NOTE: USE COMMA) :")
    item_list = [item.strip() for item in items.split(',')]
    user.extend(item_list)
    print(f"THE ITEM {items} IS ADDED TO YOUR CART.")
    print(f"YOUR CART HAS ITEMS:{user}")

user:list=[]
print("\nWELCOME TO 'YOUR SHOPPING CART' PROGRAM!")
choice=None
while True:
    try:
        print("\n You can perform the following operations:\n 1.ADD ITEMS\n 2.REMOVE ITEMS\n 3.UPDATE / ADD ITEMS\n 4.PRINT THE CONTENTS OF CART.\n 5.EXIT")
        choice=int(input("\nEnter your choice number:"))
        if choice==1:
            item_add(user)
        elif choice==2:
            item_remove(user)
        elif choice==3:
            item_update(user)
        elif choice==4:
            print(f"YOUR CART HAS ITEMS:{user}")
        else:
            print("THANK YOU FOR USING 'YOUR SHOPPING CART' PROGRAM.")
            print(f"YOUR CART HAS ITEMS:{user}")
            break
    except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!") 
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION NO 3:

print("\n->  PART NO 3:\n")
print("THIS PROGRAM WILL PRINT FIRST 25.\n")
i=0
while i <=25:
    print(i)
    i+=1
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION # 4:

print("\n->  PART NO 4:\n")
print("THIS PROGRAM WILL PRINT FIRST TEN EVEN NUMBERS.\n")
i =0
count=0
while count<10:
        print(i)
        i+=2
        count+=1
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

#QUESTION #5:

def fac_positive(positive_value:int):
    product=1
    for i in range(positive_value):
        product=product*(i+1)
    return product
print("\n -> PART NO 5:\n")
print("-------- CALCULATE FACTORAL --------\n")
try:
    positive_value=int(input("ENTER A POSITIVE VALUE TO CALCULATE FACTORIAL:"))
except ValueError:
    print("ENTER A VALID RESPONSE")
print(f"THE FACTORIAL OF NUMBER ENTERED '{positive_value}' IS:",fac_positive(positive_value))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

#QUESTION NO 6:

print(" \n-> PART NO 6:\n")
print(" Note :THE PROGRAM WILL TAKE LIST OF VALUES AND WILL RETURN THE POSITIVE NUMBERS EXCLUDING THE NEGATIVE VALUES.")
try:
    input_list=(input("ENTER THE NUMBERS BELOW.\n(NOTE: USE COMMA): "))
    numbers = [int(num.strip()) for num in input_list.split(',')]
    positive_list=[]
    for num in numbers:
        if num>=0:
            positive_list.append(num)
except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!")
print("THE RESULTED POSITIVE LIST IS: ",positive_list)
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION NO 7:

print("-> PART NO 7:")
print("-------  SUM  -------")
try:
    i = input("ENTER THE LIST (comma-separated values): ")
    i_list = [int(num) for num in i.split(',')]
except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!")

print("THE LIST ENTERED IS::", i_list)
print("THE RESULTED SUM IS", sum(i_list))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION NO 8:

print("-> PART NO 8:")

print("----------  CONVERT TEMPERATURE  --------- ")
print("--------FROM CELSIUS TO FAHRENHEIT --------")
try:
    temp_cel = input("\n -> ENTER THE TEMPERATURE IN 'Celsius' BELOW.\n(NOTE:USE COMMA) :")
    temperature_input = [float(num) for num in temp_cel.split(',')]
    temp_output = []
    for temp in temperature_input:
        temp_fahren = (temp * 9/5) + 32
        temp_output.append(temp_fahren)
except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!")

print("\n-> CONVERTED TEMPERATURE IN FAHRENHEIT IS:", temp_output)
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# QUESTION NO 9:

print("-> PART NO 9:")
print("----- ODD NUMBERS REMOVAL -----")
try:
    userr_input = input("\n-> ENTER THE LIST NUMBERS BELOW.\n (NOTE:USE COMMA): ")
    numbers = [int(num) for num in userr_input.split(',')]
    even_numbers = [num for num in numbers if num % 2 == 0]
except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!")
print("\n->LIST AFTER REMOVING THE ODD NUMBER:", even_numbers)
print("\nTHANK YOU!!!\n")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


