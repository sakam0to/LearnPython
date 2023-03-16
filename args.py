# args and kwargs support multiple and flexible inputs without explict definition in function parameters

def func1(*args):
    print(f"args: {args} type: {type(args)}")


func1(1, 2, 3)
func1(1.1, 2, "3")


def func2(**kwargs):
    print(f"kwargs: {kwargs} type: {type(kwargs)}")


#func2(1, 2, 3)
func2(f=1.1, i=2, s="3")


def mix_func(v, *args, **kwargs):
    print(f"v:{v} args:{args}, kwargs:{kwargs}")


mix_func(1.1, 2, "3")


#def not_run(**kwargs, *args):
    #pass
