from datetime import datetime
from meteostat import Point, Hourly

class WroclawTemperature:
    def __init__(self):
        # Wrocław coordinates
        self.latitude = 51.1079
        self.longitude = 17.0385
        self.elevation = 120
        self.point = Point(self.latitude, self.longitude, self.elevation)

    def get_current_temperature(self):
        """Get the current temperature in Wrocław"""
        # Get current time
        now = datetime.now()
        
        # Fetch data for the current hour
        data = Hourly(self.point, now, now).fetch()
        
        # Return the temperature if available, None otherwise
        if not data.empty:
            return data.iloc[-1]['temp']
        return None

if __name__ == "__main__":
    reporter = WroclawTemperature()
    temp = reporter.get_current_temperature()
    if temp is not None:
        print(f"Current temperature in Wrocław: {temp}°C")
    else:
        print("Unable to fetch temperature data")