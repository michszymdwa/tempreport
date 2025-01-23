from datetime import datetime
from meteostat import Point, Hourly
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

class TemperatureReporter:
    def __init__(self, location_name=None, latitude=None, longitude=None, elevation=None):
        """
        Initialize the temperature reporter for any location.
        
        Args:
            location_name (str, optional): Name of the location (e.g., 'Wrocław, Poland')
            latitude (float, optional): Latitude of the location
            longitude (float, optional): Longitude of the location
            elevation (float, optional): Elevation in meters (will be estimated if not provided)
        """
        if location_name:
            self._init_from_location_name(location_name)
        elif all(coord is not None for coord in [latitude, longitude]):
            self.latitude = latitude
            self.longitude = longitude
            self.elevation = elevation or 0
        else:
            raise ValueError("Either location_name or both latitude and longitude must be provided")
        
        self.point = Point(self.latitude, self.longitude, self.elevation)

    def _init_from_location_name(self, location_name):
        """Initialize coordinates using geopy to look up the location."""
        try:
            geolocator = Nominatim(user_agent="tempreport")
            location = geolocator.geocode(location_name)
            if location is None:
                raise ValueError(f"Could not find location: {location_name}")
            
            self.latitude = location.latitude
            self.longitude = location.longitude
            self.elevation = location.altitude if location.altitude else 0
            
        except (GeocoderTimedOut, GeocoderUnavailable) as e:
            raise ConnectionError(f"Could not connect to geocoding service: {e}")

    def get_current_temperature(self):
        """Get the current temperature for the location"""
        now = datetime.now()
        data = Hourly(self.point, now, now).fetch()
        
        if not data.empty:
            return data.iloc[-1]['temp']
        return None


class WroclawTemperature(TemperatureReporter):
    """Legacy class maintained for backward compatibility"""
    def __init__(self):
        super().__init__(latitude=51.1079, longitude=17.0385, elevation=120)


def main():
    # Example usage
    try:
        # Using the new general reporter
        reporter = TemperatureReporter(location_name="Paris, France")
        temp = reporter.get_current_temperature()
        if temp is not None:
            print(f"Current temperature in Paris: {temp}°C")
        
        # Using the legacy Wrocław reporter
        wroclaw = WroclawTemperature()
        temp = wroclaw.get_current_temperature()
        if temp is not None:
            print(f"Current temperature in Wrocław: {temp}°C")
            
    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()