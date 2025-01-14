def f(*args):
    print("Positional", args)

    return args

def y(**kwargs):
    print("Positional:",kwargs)
    return kwargs


f(1,3,4,5,5) # Supporting args

y(numb1=1,numb2=2, numb3=3) # Supporting kwargs