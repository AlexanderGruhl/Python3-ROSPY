from robot_control_class import RobotControl

robotcontrol = RobotControl()

l = robotcontrol.get_laser_full()
print("Distance from laser 0 ", l[0])
print("Distance from laser 360 ", l[360])
print("Distance from laser 719 ", l[719])


