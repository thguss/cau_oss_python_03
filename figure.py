"""
figure 모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 이용하여 선의 길이를 설정/참조 수행하며
area_square, area_circle, area_regular_triangle 함수로
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다.
"""

import math

class line:
    """
    line class는 선의 길이에 대해 저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가능한 __length가 있으며,
    해당 변수를 수정하고 접근하기 위해
    set_length와 get_length를 제공합니다.
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def set_length(self, width, height):
        self.__width = width
        self.__height = height
    
    def get_length(self):
        return self.__width, self.__height

def area_rectangle(width, height):
    """
    width와 height를 매개변수로받아, 𝑤𝑖𝑑𝑡ℎ×ℎ𝑒𝑖𝑔ℎ𝑡의 직사각형의 넓이를 반환한다.
    """
    if width <= 0 or height <= 0: return ValueError
    return width * height

def area_ellipse(width, height):
    """
    width와 height를 매개변수로 받아, width × ℎ𝑒𝑖𝑔ℎ𝑡 × 𝜋 의 타원의 넓이를 반환한다.
    𝜋는 math 모듈의 math.pi를 사용한다.
    """
    if width <= 0 or height <= 0: return ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    """
    width와 height를 매개변수로 받아, 𝑤𝑖𝑑𝑡ℎ×ℎ𝑒𝑖𝑔ℎ𝑡/2의 직각삼각형의 넓이를 반환한다.
    """
    if width <= 0 or height <= 0: return ValueError
    return width * height / 2