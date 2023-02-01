class Sensor:
    """ Top level class for sensors """
    
    def __init__(self, id):
        """
        Create a sensor 
        :param id: The id of this sensora
        """
        self._id = id
        
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
        
    def calibrate(self):
        """ Calibrates any variables needed 
        :returns: None
        """
        return None
        
    def observe(self):
        """ Observes / senses the world, making observations if it changes 
        :returns: None
        """
        return None
