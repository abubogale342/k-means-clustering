def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
               b.add_point(point)
        if a_old == a.points:
            continue
        
        a_old = list(a.points)
        a.update()
        b.update()
        # Reassing/clear lists 
        a_old = null
       
    # Return values ordered ny greatest x
    if a.center.x > b.center.x:
        return [(a.center.x, a.center.y),(b.center.x,b.center.y)]
    return [(b.center.x, b.center.y),(a.center.x,a.center.y)]
=====================================