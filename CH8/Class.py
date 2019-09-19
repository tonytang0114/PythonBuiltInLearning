class Demo:
    # Change the way method is called, so it receives 
    # the class itself as the first argument
    @classmethod
    def klassmeth(*args):
        return args
    
    # changes a method so that it receives no special first
    # argument.
    @staticmethod
    def statmeth(*args):
        return args
    
print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('spam'))