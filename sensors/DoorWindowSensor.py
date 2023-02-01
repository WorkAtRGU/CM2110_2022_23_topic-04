from sense_hat import SenseHat
import time
import math
import datetime
from sensors import Sensor


class DoorWindowSensor(Sensor.Sensor):
    """ Class for sensor that monitors for a door/window opening or closing """
    
    def __init__(self, id, foi_name):
        """
        Create a sensor 
        :param id: The id of this sensora
        """
        super().__init__(id)
        # details of the thing being observed
        self._foi = {
          "name":foi_name,
        }
        self._sense = SenseHat()
        
    def get_id(self):
        """ Returns the id of this sensor
        
        :returns: the id of this sensor
        :rtype: int
        """
        return self._id
    
    def get_reading(self):
        """ Returns a reading from this sensor
        :returns: None or see subclass documentation
        """
        return None
        
    def _calc_mag_field(self):
        """ Calculates the strength of magnetic field sensed by the compass 
        :returns: a float indicating the magnetic field strength
        """
        raw = self._sense.get_compass_raw()
        x = raw["x"]
        y = raw["y"]
        z = raw["z"]
        sum_squares = x*x + y*y + z*z
        force = math.sqrt(sum_squares)
        return force
    
    def calibrate(self):
        """ Calibrates any variables needed 
        :returns: True
        """
        # get the current reading, assuming the door is open
        self._baseline = self._calc_mag_field()
        
        # current state
        self._current_state = "OPEN"

        # threshold for required change to baseline
        self._mag_change_threshold = 60
        return True

    def observe(self):
        """ Observes / senses the world, making observations if it changes 
        
        """
        # lets start making the observations
        while True:
          try:
              # get the current mag field value
              field_strength = self._calc_mag_field()

              # if the current value is greater than the (baseline + a threashold) and the current_state is "OPEN"
              # (experiment with values for threshold - start with 5000 and see if thats enough or if it needs to be larger)
              #  then change current_state to "CLOSED"
              if field_strength > (self._baseline + self._mag_change_threshold) and self._current_state == "OPEN":
                  self._current_state = "CLOSED"
            
                  # complete the template for the observations action and the result and add to
                  observation = {
                      # when the observation action finished - to be set when making observations
                      "resultTime" : datetime.datetime.now().isoformat(),
                      # the thing we're monitoring - i.e. the door / window
                      "featureOfInterest" : self._foi,
                      # change to something more relevant to what we're recording about the door / window
                      "observedProperty" : "State",
                      # what was recorded
                      "hasResult" :  {
                          "value" : self._current_state
                      }
                  }
                  print(observation)
              # else if current_value is less than (baseline + threshold0 current_state is "CLOSED" 
              # then change the current_state to "OPEN" and append and observation to sensor["madeObservation"] list
              elif field_strength < (self._baseline + self._mag_change_threshold) and self._current_state == "CLOSED":
                 self._current_state = "OPEN"
                 # complete the template for the observations action and the result and add to
                 observation = {
                     # when the observation action finished - to be set when making observations
                     "resultTime" : datetime.datetime.now().isoformat(),
                     # the thing we're monitoring - i.e. the door / window
                     "featureOfInterest" : self._foi,
                     # change to something more relevant to what we're recording about the door / window
                     "observedProperty" : "State",
                     # what was recorded
                     "hasResult" :  {
                         "value" : self._current_state
                     }
                 }
                 print(observation)
            
             
          except KeyboardInterrupt:
            # exist the while loop, but before that, print sensor to see what it looks like
            exit()

