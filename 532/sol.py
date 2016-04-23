import math


class Memoize(object):
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


class Point(object):
    """
    A point on the surface of a sphere. Assume the
    sphere has radius 1.

    """
    # 24 18
    # 11 8 seems to work
    TINY_STEP_SIZE = 2**-11
    # The difference in spherical coordinates before two points are the same.
    # Maybe convert to cartesian diff?
    # Should be bigger than TINY_STEP_SIZE so there is no bouncing
    EPSILON = 2**-8

    def __init__(self, lat, lon):
        # self.x1 = x1
        # self.y1 = y1
        # self.z1 = z1
        self.lat = lat
        self.lon = lon
        self.traveled = 0
        self.lat_backup = 0
        self.lon_backup = 0

    def travel(self, p2):
        """
        Move towards p2 along a great circle. Move only TINY_STEP_SIZE
        distance. Return False if we are at p2.

        See http://math.stackexchange.com/questions/383711/
            parametric-equation-for-great-circle

        """
        # self.traveled += d
        # This function returns both the distance and the central angle
        # because our radius is 1.

        d = geodesic_distance(self, p2)
        if d < self.EPSILON:
            return False
        sin_d = memo_sin(d)
        cos_lat = memo_cos(self.lat)
        cos_lon = memo_cos(self.lon)
        cos_p2_lat = memo_cos(p2.lat)
        cos_p2_lon = memo_cos(p2.lon)
        dist_traveled = self.TINY_STEP_SIZE * d
        # print 'distance is still', d
        A = memo_sin((1-self.TINY_STEP_SIZE)*d) / sin_d
        B = memo_sin(dist_traveled) / sin_d
        x = A * cos_lat * cos_lon + B * cos_p2_lat * cos_p2_lon
        y = A * cos_lat * memo_sin(self.lon) + B * cos_p2_lat * memo_sin(
            p2.lon)
        z = A * memo_sin(self.lat) + B * memo_sin(p2.lat)

        # Update distance
        self.lat_backup = memo_atan2(z, memo_sqrt(x**2 + y**2))
        self.lon_backup = memo_atan2(y, x)
        self.traveled += dist_traveled

        return True

    def update_position(self):
        # print 'moved from', self.lat, self.lon, 'to', self.lat_backup, self.lon_backup

        self.lat = self.lat_backup
        self.lon = self.lon_backup
        # print 'updated position to', self.theta, self.phi


def hav(angle):
    return math.sin(angle/2)**2

hav = Memoize(hav)
memo_sin = math.sin
memo_cos = math.cos
memo_atan2 = math.atan2
memo_sqrt = math.sqrt
memo_asin = math.asin


def asin_sqrt(d):
    return memo_asin(memo_sqrt(d))


def geodesic_distance(p1, p2):
    # Use haversine formula, assume radius = 1
    delta_lat = p1.lat - p2.lat
    delta_lon = p1.lon - p2.lon
    d = hav(delta_lat) + memo_cos(p1.lat)*memo_cos(p2.lat)*hav(delta_lon)
    return 2 * asin_sqrt(d)


def small_circle_latitude(radius):
    """
    Return the latitude of the small circle with radius `radius`.
    Assume sphere has radius 1.
    """
    # Use Pythagoras.
    h = memo_sqrt(1 - radius**2)
    # h is the height of the latitude line over the center of the sphere.
    # convert to spherical coordinates:
    # x = 0
    # y = radius
    # z = h
    # Assume theta is elevation from the reference plane.
    theta = memo_asin(h / memo_sqrt(radius**2 + h**2))
    # phi = math.atan2(radius, 0)
    return theta


def place_robots(n):
    # Place n robots on a small circle of R = 0.999 equidistantly
    # Use spherical coordinates; same latitude and equidistant longitudes.
    # Longitude is in [0, 2pi)
    # Latitude is in [0, pi]
    robots = []
    latitude = small_circle_latitude(0.999)
    for i in range(n):
        longitude = i * (2*math.pi/n)
        robots.append(Point(latitude, longitude))
        print 'robot', i, latitude, longitude
    return robots


def get_length_for_robots(n):
    robots = place_robots(n)
    # Iterate.. will this work?
    lon_diff = 2 * math.pi / n
    traveling = True
    iterations = 0
    while traveling:
        iterations += 1
        for i, robot in enumerate(robots):
            if i < len(robots) - 1:
                next_robot = robots[i+1]
            else:
                next_robot = robots[0]
            if i == 0:
                traveling = robot.travel(next_robot)
                robot.update_position()
            else:
                # This is symmetric, dont need to recalculate every time.
                robot.lat = robots[0].lat
                robot.lon = robots[0].lon + (i * lon_diff)
                robot.traveled = robots[0].traveled
        if iterations == 1:
            print robots[0].lat, robots[0].lon
        if iterations % 100000 == 0:
            print 'iterations:', iterations
            print 'memo_lengths: %s' % (
                len(hav.memo)
            )
        #for robot in robots:
        #    robot.update_position()

    return sum([robot.traveled for robot in robots])
    # return robots[0].traveled * n

if __name__ == '__main__':
    n = 2
    while True:
        l = get_length_for_robots(n)
        print 'length for %s robots is %s, per_robot %s' % (n, l, l/n)
        if l / n >= 1000:
            print 'total length is', l, 'num robots', n
            break
        n += 1
