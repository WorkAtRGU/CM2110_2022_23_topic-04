from sensors import DoorWindowSensor

door_sensor = DoorWindowSensor.DoorWindowSensor()
door_sensor.calibrate()
door_sensor.observe()