'''This module contains classes to model polygons. Note that we have added some
properties and methods to each class. Although, we are not experts in geometery
, so there are probably many more methods and attribute we could add!

Note that we have the validate_side_length method defined in the parent Polygon
class. This is because this must be true for ALL polygons.

We add the perimeter property to the Simple polygon class because this is true
for all Simple polygons, but not true for non-Simple polygons.

We added the area method to the Regular polygon class, because this is the area
formula for Regular polygons, but would not be valid for other polygons.

'''

import math


class Polygon:
    '''A class to model a polygon

    Parameters
    ----------
    sides : list of floats, ints
        the lengths of the polygon sides

    tag : str,
        a name for our polygon

    '''

    def __init__(self, sides, tag):
        self.sides = sides
        self.nsides = len(sides)
        self.tag = tag

    def validate_side_lengths(self):
        '''Validate that the longest side is shorter than the sum of the other
        sides
        '''
        max_ix = self.sides.index(max(self.sides))
        if self.sides[max_ix] <= (sum(self.sides[:max_ix]) +
                                  sum(self.sides[max_ix+1:])):
            return True
        else:
            return False


class SimplePolygon(Polygon):
    '''A class to model a Simple polygon. A Simple polygon is a polygon with
    none of the sides intersecting. If any sides of a polygon intersect, it is
    not a Simple polygon'''

    def __init__(self, sides, tag):
        super().__init__(sides, tag)

    @property
    def perimeter(self):
        '''Return the sum of the lengths of the sides'''
        return sum(self.sides)


class RegularPolygon(SimplePolygon):
    '''A class to model a Regular polygon. All of a Regular polygons must be
    the same length (equilateral), and the angles at each vertex must be the
    same (equiangular).'''

    def __init__(self, side_length, nsides, tag):
        super().__init__([side_length]*nsides, tag)

    def validate_side_lengths(self):
        '''Validate that the sides are equilateral. This overwrites the method
        of the same name from the parent class'''
        if len(set(self.sides)) == 1:
            return True
        else:
            return False

    def area(self):
        '''Return the area of the Regular polygon'''
        n = len(self.sides)
        s = self.sides[0]
        return (1/4)*n*(s**2)*(1/math.tan(math.pi/n))
