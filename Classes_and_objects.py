class fruit():
    def __init__(self,taste,colour,shape):
        self.taste = taste
        self.colour = colour
        self.shape = shape
    def print_fruit_sentence(self):
        print('The taste is', self.taste, 'and is', self.colour, 'in colour.')
grapes = fruit('sour','black','round')
grapes.print_fruit_sentence()

watermelon = fruit('sweet','red','oval')
print(watermelon.taste)

