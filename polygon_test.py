import polygons

my_bad_poly = polygons.Polygon([2, 3, 4, 20], tag='Bad Poly')
print('Valid: {}'.format(my_bad_poly.validate_side_lengths()))

my_poly = polygons.Polygon([2, 3, 4, 5], tag='Good Poly')
print('Valid: {}'.format(my_poly.validate_side_lengths()))

my_simply_poly = polygons.SimplePolygon([3, 3, 4, 6], tag='Simple')
print('Simple Ploly Perimeter: {}'.format(my_simply_poly.perimeter))

my_regular_poly = polygons.RegularPolygon(side_length=3, nsides=4,
                                          tag='Regular')
print('Regular Ploly Perimeter: {}'.format(my_regular_poly.perimeter))
print('Regular Ploly Area: {}'.format(my_regular_poly.area()))
