# Temperature Reporter

A simple Python application that fetches current temperature data for any location using the Meteostat API.

## Features

- Get current temperature for any location worldwide
- Support for location lookup using city names or coordinates
- Backwards compatibility with Wrocław-specific functionality
- Error handling for location lookup and temperature fetching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/michszymdwa/tempreport.git
cd tempreport
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic usage with location name:

```python
from temp_reporter import TemperatureReporter

# Create a reporter for any city
reporter = TemperatureReporter(location_name="London, UK")
temp = reporter.get_current_temperature()
print(f"Current temperature: {temp}°C")
```

### Using coordinates:

```python
reporter = TemperatureReporter(
    latitude=51.1079,
    longitude=17.0385,
    elevation=120  # optional
)
temp = reporter.get_current_temperature()
```

### Legacy Wrocław usage:

```python
from temp_reporter import WroclawTemperature

reporter = WroclawTemperature()
temp = reporter.get_current_temperature()
```

## Dependencies

- meteostat: For fetching temperature data
- geopy: For location geocoding
- python-dateutil: For date handling

## Error Handling

The application handles various error cases:
- Invalid location names
- Geocoding service unavailability
- Missing temperature data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).