def check_even_odd(num):
    try:
        if num % 2 == 0: 
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    except TypeError:
        print("Please enter a valid integer.")

    if num % 2 ==0:  
        print(f"{num} is even")
    else:
        print(f"{num} + is odd") 
    if num % 2 == 0:  
        print(f"{num} is even")
    else:
        print("is odd")
    return None

check_even_odd(7) 
check_even_odd(-4)  
