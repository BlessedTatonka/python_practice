class ComplexNumber:
  
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __add__(self, c1: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.re + c1.re, self.im + c1.im)
  
    def __mul__(self, c1: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.re * c1.re - self.im * c1.im, self.re * c1.im + self.im * c1.re)

    def __sub__(self, c1: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.re - c1.re, self.im - c1.im)

    def __truediv__(self, c1: 'ComplexNumber') -> 'ComplexNumber':
        denominator = c1.re ** 2 + c1.im ** 2
        if denominator == 0:
            return None

        return ComplexNumber((self.re * c1.re + self.im * c1.im) / denominator,
                       (self.im * c1.re - self.re * c1.im) / denominator)
    
    def __str__(self):
        return f'{self.re} + {self.im}i'

    def __eq__(self, c1):
        return self.re == c1.re and self.im == c1.im