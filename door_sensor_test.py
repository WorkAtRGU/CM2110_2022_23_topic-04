from sensors import DoorWindowSensor

door_sensor = DoorWindowSensor.DoorWindowSensor("door1sensor", "door1")
door_sensor.calibrate()
door_sensor.observe()