class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return ''.join([self.width * '*' + '\n' for i in range(self.height)])
    
    def get_amount_inside(self, shape):
        return self.get_area() // (shape.width * shape.height)


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side