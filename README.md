# Luxembourg Time & Unix Epoch Display

A Python desktop application that displays real-time information including Unix epoch time, Luxembourg local time, and the current date in an elegant GUI interface.

## Features

- **Real-time Unix Epoch Time**: Displays the current Unix timestamp (seconds since January 1, 1970)
- **Luxembourg Time Zone**: Shows the current time in Luxembourg/Europe timezone with timezone indicator
- **Date Display**: Shows the full date in a readable format (Day, Month DD, YYYY)
- **Auto-updating**: Refreshes every second to maintain accuracy
- **Clean GUI**: Modern interface built with tkinter and ttk widgets

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- pytz library for timezone handling

## Installation

1. Ensure Python 3.x is installed on your system
2. Install the required pytz library:
   ```bash
   pip install pytz
   ```

## Usage

Run the application by executing:
```bash
python epoch.py
```

The application window will open displaying:
- **Unix Epoch Time**: Current timestamp in blue
- **Luxembourg Time**: Local time with timezone in orange  
- **Date**: Full date information in green

## Technical Details

### Architecture
- **Main Class**: `TimeDisplay` - Handles GUI creation and time updates
- **GUI Framework**: tkinter with ttk for modern widget styling
- **Timezone Handling**: Uses pytz library for accurate Luxembourg timezone conversion
- **Update Mechanism**: Tkinter's `after()` method for non-blocking periodic updates

### Window Specifications
- **Size**: 600x300 pixels
- **Background**: Light gray (#f0f0f0)
- **Layout**: Grid-based with centered alignment
- **Fonts**: Arial for labels, Courier for time displays

### Time Sources
- Unix epoch time from `time.time()`
- Luxembourg time from `datetime.now()` with Europe/Luxembourg timezone
- Automatic handling of daylight saving time transitions

## Code Structure

The application follows a clean object-oriented design:
- Constructor sets up the GUI layout and timezone configuration
- `update_time()` method refreshes all time displays and schedules the next update
- `main()` function initializes the tkinter root window and starts the application loop

## Hardware Considerations

Given your hardware background, this application is lightweight and suitable for:
- Embedded systems with Python support
- Raspberry Pi deployments
- Low-power computing environments
- Systems requiring accurate time synchronization displays

The application uses minimal system resources and can run continuously without performance degradation.
