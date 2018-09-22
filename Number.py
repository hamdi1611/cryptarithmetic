class Number:
    def __init__(self):
        self.alpha = 'X'
        self.value = -1

    # Getter and Setter
    def getAlpha(self):
        return self.alpha
    def getValue(self):
        return self.value
    def setAlpha(self, alpha):
        self.alpha = alpha
    def setValue(self, value):
        self.value = value
    def setAll(self, alpha, value):
        self.alpha = alpha
        self.value = value
    
    # Check wether this object Number has been set with a value or not
    def isSetByValue(self):
        return not(self.alpha == 'X')
