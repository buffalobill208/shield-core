#Returns the cylinder surface area depending whether the cylinder is solid or hollow

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    else:
        return side_area

print(cylinder_surface_area(10,5,"has_top_and_bottom"))
print(cylinder_surface_area(10,5,""))
