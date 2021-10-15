import numpy as np
from math import factorial


def addtuples(a, b):
    return (a[0]+b[0], a[1]+b[1])

def to_int(arr):
    return [[int(i) for i in j] for j in arr]

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def get_bezier_matrix(n):
    coef = [[comb(n, i) * comb(i, k) * (-1)**(i - k) for k in range(i + 1)] for i in range(n + 1)]
    return [row + [0] * (n + 1 - len(row)) for row in coef]

def evaluate_bezier(points, total):
    n = len(points) - 1
    T = lambda t: [t**i for i in range(n + 1)]
    M = get_bezier_matrix(n)
        
    return to_int(np.array([
        np.dot(np.dot(T(t), M), points)
        for t in np.linspace(0, 1, total)
    ]))
    
    
class BezierCurve:
    def __init__(self, points, resolution):
        self.points = points
        self.resolution = resolution
        
        self.fix_points()
                        
                        
        self.curve = evaluate_bezier(points, resolution)
        
        self.next_curve = None
        self.prev_curve = None
        
        
    def get_curve(self):
        return self.curve
    
    def get_points(self):
        return self.points
    
    def edit_point(self, check, j, d):
        if(check):
            if(j == 0):
                if(self.prev_curve != None):
                    self.prev_curve.edit_point(False, -1, d)
                    self.prev_curve.edit_point(False, -2, d)
                    self.points[j+1] = addtuples(self.points[j+1], d)
            elif (j == len(self.points)-1):
                if(self.next_curve != None):
                    self.next_curve.edit_point(False, 0, d)
                    self.next_curve.edit_point(False, 1, d)
                    self.points[j-1] = addtuples(self.points[j-1], d)
            elif (j == 1):
                if(self.prev_curve != None):
                    self.prev_curve.edit_point(False, -2, (-d[0], -d[1]))
            elif (j == len(self.points)-2):
                if(self.next_curve != None):
                    self.next_curve.edit_point(False, 1, (-d[0], -d[1]))
                    
            
        self.points[j] = addtuples(self.points[j], d)
        self.fix_points()
        self.curve = evaluate_bezier(self.points, self.resolution)
        
        
    def fix_points(self):
        pass
        
    def get_endpoints(self, start):
        if(start):
            return (self.points[0], self.points[1])
        else:
            return (self.points[-1], self.points[-2])
