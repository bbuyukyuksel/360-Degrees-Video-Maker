class CPrint:
        
    @classmethod
    def cprint(cls, attribute, color, *args,series=3 , **kwargs):
        print('\033[0{};{}{}m'.format(attribute,series ,color), end='')
        print(*args,'\033[00m', **kwargs)
    
    @classmethod
    def tutorial(cls):
        print("Series of 3.")
        for attribute in range(10):
            for color in range(9):
                cls.cprint( attribute, 
                            color,
                            '{:2}:{:2} Hello World!'.format(attribute, color), 
                            end='')
            print()
    
        print("Series of 4.")
        for attribute in range(10):
            for color in range(9):
                cls.cprint( attribute, 
                            color,
                            '{:2}:{:2} Hello World!'.format(attribute, color),
                            series=4,
                            end='')
            print()
