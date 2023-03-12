#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()

# Set the timezone to Cairo
cairo_timezone = datetime.timezone(datetime.timedelta(hours=2))

# Get the current time in Cairo timezone
cairo_time = now.astimezone(cairo_timezone)

# Format the time string with hour, minute, and second
time_str = cairo_time.strftime("%H:%M:%S")

date = datetime.datetime.now().strftime('🗓️%d-%b (%a)')


# Choose the sun or moon emoji based on the current time
if cairo_time.hour >= 5 and cairo_time.hour < 18:
    emoji = "☀️"
else:
    emoji = "🌙"

# Print the time with the emoji
print(f"{date} {emoji} {time_str}")
