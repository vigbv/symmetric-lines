from decimal import Decimal as D # use decimal for accurate calculations
round_digits = D(10) ** -5 # use precision 5 to round the decimals

def calculate_linear_equation(p: set, q: set) -> tuple: 
    """Returns linear equation for a given set of points (coordinates)
       - used to calculate linear equation for line passing through input point and centroid
    """
    
    x1, y1 = D(q[0]).quantize(round_digits), D(q[1]).quantize(round_digits)
    x2, y2 = D(p[0]).quantize(round_digits), D(p[1]).quantize(round_digits)
    
    a = y1 - y2
    b = x2 - x1
    c = D((x1 * y2) - (x2 * y1)).quantize(round_digits)
    
    return a, b, c

def find_midpoints(input: list) -> set:
    """Returns midpoints between all points for a given set of coordinates
       - find midpoints to check if there are lines of symmetry along non-vertex points
    """
    
    input_len = len(input)
    mid_points = set()
    
    for i in range(input_len):
        for j in range(i+1, input_len):
            midpoint = (D((input[i][0] + input[j][0]) / 2).quantize(round_digits) , D((input[i][1] + input[j][1]) / 2).quantize(round_digits))
            mid_points.add(midpoint)
            
    return mid_points

def find_reflection_point(x: set, a: float, b: float, c: float) -> set:
    """Returns reflection point coordinates for a given point (coordinates) and linear equation
       - used to calculate reflection point for a given input point
       - for a line to be symmetric, all reflection points exist in input points
    """
    
    p = D(x[0])
    q = D(x[1])
    
    """
        tried other methods to calculate refelction points, but got errors, need to investigate:
        reflection_coord = (((1-m**2)*p + 2*m*(q-c))/(1+m**2), ((2*m*p)-(1-m**2)*q + 2*c)/(1+m**2))
        reflection_coord = ((p*(a**2-b**2)-2*b*((a*q)+c)/(a**2+b**2)), (q*(b**2-a**2)-2*a*((b*p)+c))/(a**2+b**2))
    """
                
    reflection_eqn = -2*(a*p + b*q + c)/(a**2 + b**2)
    reflection_point_x = (reflection_eqn * a + p).quantize(round_digits)
    reflection_point_y = (reflection_eqn * b + q).quantize(round_digits)
    reflection_point = ((reflection_point_x), (reflection_point_y))
    
    return reflection_point

def find_symmetric_lines(input: list) -> dict:
    """Checks if there are lines of symmetry for a given set of points (coordinates) and returns the coordinates for symmetric lines
    """
    
    master_slope = set()
    symmetric_lines = {}
    
    input_set = set()
    
    for point in input: # convert input points to decimal
        input_set.add((D(point[0]).quantize(round_digits), D(point[1]).quantize(round_digits)))
                
    centroid = tuple(D(x / len(input)).quantize(round_digits) for x in map(sum, zip(*input))) # calculate centroid for all points, all symmetric lines pass through centroid

    mid_points = find_midpoints(input) # find all midpoints

    all_points = set() # merge input points and midpoints
    all_points = input_set
    all_points.update(mid_points)
    
    for point in all_points: # loop through all the points to find symmetryic lines
    
        is_symmetric = 0
        
        if point != centroid:
            
            a, b, c = calculate_linear_equation(point, centroid) # ax+by+c
            
            if b != 0: # skip vertical lines as they have Inf slope 
                slope = -a/b
            else:
                slope = "vertical"

            if slope in master_slope: # check master slope set to ignore duplicate points on same line  
                continue
            
            master_slope.add(slope) 
            
            for input_point in input:    
                if input_point != point:
                    reflection_point = find_reflection_point(input_point, a, b, c)
                                    
                    if reflection_point not in input_set:
                        is_symmetric = 0
                        break
                    else:
                        is_symmetric = 1
            
            if is_symmetric:
                symmetric_lines[point] = [a,b,c]
            
    return symmetric_lines
    

# example inputs
input_examples = {
    'square': [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)], # 4
    'rectangle': [(-2,2), (-2,4), (2,4), (2,2)], # 2
    'rhombus': [(2,-3), (6,5), (-2,1), (-6,-7)], # 2
    'kite': [(2,2), (5,-1), (2,-4), (-4,-1)], # 1
    'isosceles_trapezoid': [(-3,2), (0,2), (2,0), (2,-3)], # 1
    'trapezoid': [(0,0), (17,6), (8,6), (20,0)], # 0
    'parallelogram': [(-5,-4), (5,3), (7,12), (-3,5)], # 0
    'equilateral_triangle': [(-1,0),(0,1.7320508075688772),(1,0)], # 3
    'isosceles_triangle': [(1,-6), (7,5), (-4,-1)], # 1,
    'butterfly': [(13,27), (15,22), (15,7), (17,  11), (15, 22),(14,21), (17,11), (16,15), (14, 21), (13, 18), (16,15), (17, 18), (13, 18), (14, 15), (17, 18), (16,21), (14, 15), (13, 11), (16,21), (15, 22), (13,11), (15,7), (15, 22), (17, 27), (16,15), (21, 24), (21, 24), (28,26), (28,26), (29, 23), (29, 23), (26, 17), (26, 17), (20,15), (20,15), (24, 12), (24, 12), (24,9), (12,9), (9,7), (24,9), (23,8), (9,7),(7,8), (23, 8), (21,7), (7,8), (6,9), (21,7), (18,9), (6,9), (6, 12), (18,9), (17,  11), (6,12), (10,15), (13, 11), (12,9), (10, 15), (4, 17), (4,17), (1,23), (1, 23), (2, 26), (2,26), (9,24), (9,24), (14, 15)] # 1
}

if __name__ == '__main__':
    symmetric_lines = find_symmetric_lines(input_examples['rectangle'])
                        
    print("Total number of symmetric lines: " + str(len(symmetric_lines))) 

    i = 1
    for point, coord in  symmetric_lines.items():
        a, b, c = round(float(coord[0]), 2), round(float(coord[1]), 2), round(float(coord[2]), 2)
        print(f'Linear equation for symmetric line {i}: {a}x{b:+}y{c:+} = 0')
        i += 1