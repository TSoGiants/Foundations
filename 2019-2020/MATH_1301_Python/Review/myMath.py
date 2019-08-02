import string

def avg(*n):
    if n:
        sum = 0
        total = len(n)
        for number in n:
            sum += number
        average = sum / total
        return average
    return 0
    
class abstractInt():
    
    def __init__(self, value="0", base=10):
        self.value = str(value).upper()
        self.base = int(base)
        self.baseDigits = self.getDigits(self.base)
        
    def __str__(self):
        return f"{self.value}, base {self.base}"
        
    def __repr__(self):
        return f"abstractInt(value={self.value}, base={self.base})"
        
    def int(self): # Retrieve the value (in decimal) for this number.
        x = 0
        for i in range(len(self.value)):
            place = len(self.value) - 1 - i
            x += self.baseDigits.find(self.value[place])*(self.base**i)
            
        return x
        
    def getDigits(self, b):
        return (string.digits + string.ascii_uppercase)[0:b]
        
    def changeBase(self, newBase):
        tempVal = self.int()
        self.base = newBase
        self.baseDigits = self.getDigits(newBase)
        
        self.value = "" # Re-initialize self.value
        while tempVal > 0:
            digit = tempVal % newBase
            self.value = self.baseDigits[digit] + self.value
            tempVal //= newBase
            
            
            