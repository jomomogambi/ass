class temperature():
    def __init__(self,celsius,fahrenheit):
        self.cel=celsius
        self.fahren=fahrenheit
    def convertfahren(self):
        fans=(self.cel*9/5)+32
        print=(self.cel,"celsius=",fans,"fahrenheit")
    def convertcel(self):
        cans=(self.fahren-32)*5/9
        print=(self.fahren,"fahrenheit=",cans,"celsius")
Te=temperature(10,50)
Te.convertfahren
Te.convertcel()