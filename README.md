# Wrocław Temperature Reporter

A simple Python class that fetches the current temperature in Wrocław, Poland using the meteostat library.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/michszymdwa/tempreport.git
cd tempreport
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

```python
from temp_reporter import WroclawTemperature

# Create an instance of the temperature reporter
reporter = WroclawTemperature()

# Get the current temperature
temperature = reporter.get_current_temperature()

if temperature is not None:
    print(f"Current temperature in Wrocław: {temperature}°C")
else:
    print("Unable to fetch temperature data")
```

You can also run the script directly:
```bash
python temp_reporter.py
```

## Requirements
- Python 3.6+
- meteostat>=1.6.5
- python-dateutil>=2.8.2