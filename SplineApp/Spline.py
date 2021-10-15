from beziercurve import *


class Spline:
    def __init__(self, resolution):
        self.beziers = []
        self.resolution = resolution
        self.add_bezier(True)
        self.add_bezier(False)
        self.add_bezier(True)
        
    def add_bezier(self, start):
        if not len(self.beziers):
            self.beziers.append(BezierCurve((np.random.randn(4, 2))*100+400, self.resolution))
        else:
            if start:
                prev = self.beziers[0]
                endpoints = prev.get_endpoints(True)
                other = prev.get_endpoints(False)
                
                new_endpoint = endpoints[0]
                new_control = addtuples(endpoints[0], addtuples(-endpoints[1], endpoints[0]))
                other_endpoint = addtuples(endpoints[0], addtuples(-other[0], endpoints[0]))
                other_control = addtuples(endpoints[0], addtuples(-other[1], endpoints[0]))
                self.beziers = [BezierCurve([other_endpoint, other_control, new_control, new_endpoint], self.resolution)] + self.beziers
                self.beziers[0].next_curve = self.beziers[1]
                self.beziers[1].prev_curve = self.beziers[0]
            
            else:
                prev = self.beziers[-1]
                endpoints = prev.get_endpoints(False)
                other = prev.get_endpoints(True)
                
                new_endpoint = endpoints[0]
                new_control = addtuples(endpoints[0], addtuples(-endpoints[1], endpoints[0]))
                other_endpoint = addtuples(endpoints[0], addtuples(-other[0], endpoints[0]))
                other_control = addtuples(endpoints[0], addtuples(-other[1], endpoints[0]))
                self.beziers.append(BezierCurve([new_endpoint, new_control, other_control, other_endpoint], self.resolution))
                self.beziers[-2].next_curve = self.beziers[-1]
                self.beziers[-1].prev_curve = self.beziers[-2]
                
            
    def edit_bezier_point(self, i, j, d):
        self.beziers[i].edit_point(True, j, d)
    
    def get_beziers(self):
        return self.beziers
            
    