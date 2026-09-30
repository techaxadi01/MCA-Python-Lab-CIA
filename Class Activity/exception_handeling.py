while True:
    try:
        print(310 * (1/0))
        break
    except (RuntimeError, TypeError, NameError, ZeroDivisionError) as err:
        print("Opps! an Error occured \n\t Error :",err)
        break

while True:
    try:
        print(4 + prod *3)
        break
    except (RuntimeError, TypeError, NameError, ZeroDivisionError) as err:
        print("Opps! an Error occured \n\t Error :",err)
        break

while True:
    try:
        print('5' + 5)
        break
    except (RuntimeError, TypeError, NameError, ZeroDivisionError) as err:
        print("Opps! an Error occured \n\t Error :",err)
        break


def div(x,y):
    try:
        res = x/y
    except Exception as err:
        print("Error : ", err)
    else:
        print("Result : ",res)
    finally:
        print("Executing finally calause \n")

div(6,2)
div(1,2)
div(6,0)
div('8','4')