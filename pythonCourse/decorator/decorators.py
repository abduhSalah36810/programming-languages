# decorator ha ?  : 

# - areya gonna say it's used to decorate 
# the function and enhance its behavior ? 
# - yeah ! and it takes function as a prameter
# it's a high order fucntion thu. and we use it to 
# modify the behavior of any function without
# even changing it's lines of code 
 

# let's see : 


# if we wanted to see the run time of the fuctions
# that we have in our program we can use a decorator

import time 

def timer (func) : 
    def wrapper(*args , **kwargs) : 
        start = time.time()
        rv = func()
        end  = time.time() - start
        print(f"time : {end}") 
        if end > 5 : 
            print("long time to run")
        return rv
    return wrapper

@timer
def somefunc () : 
    for i in range(100000) : 
        print(i)
        
somefunc()