from robot_control_class import RobotControl

rc = RobotControl()

def get_three_lasers(a=0, b=360, c=600):
    l1 = rc.get_laser_summit(a)
    l2 = rc.get_laser_summit(b)
    l3 = rc.get_laser_summit(c)
    l = [l1, l2, l3]
    return l

laser = get_three_lasers()
print("Reading 1 ", laser[0])
print("Reading 2 ", laser[1])
print("Reading 3 ", laser[2])