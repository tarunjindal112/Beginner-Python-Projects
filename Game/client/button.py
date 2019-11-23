"""
Stores interface for button and two concrete button classes
to be used in the UI.
"""
import pygame


class Button:
    """
    abstract button class
    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        raise Exception("Not implemented")

    def click(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True  # user clicked button

        return False

