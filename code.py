class Drinks:
    def __init__(self, sugar_content):
        self.sugar_content = sugar_content


    def get_sugar_content(self):
        return self.sugar_content

    def set_sugar_content (self, sugar_content):
        self.sugar_content = sugar_content 

    def stuff (self, a, b, c)
        print (a, b, c)
    

class Soda(Drinks):
    pass


class Water(Drinks):
    def __init__(self, sugar_content, name):
        super()__init__(sugar_content)
        self.name = name 

    def print_name(self):
        print(self.name)


class Sparkling_Water(Water)
    def __init__(self, sugar_content):
        super().__init__(sugar_content, "sparking water")
    
    
        water.stuff(3,5,7)