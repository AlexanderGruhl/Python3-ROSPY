from robot_control_class import RobotControl

rc = RobotControl()

num = int(input("Enter a number between 0 and 719 "))

laser = rc.get_laser(num)

print("Laser distance is %d meters" % laser)
