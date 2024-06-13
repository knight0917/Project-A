import pytz
from datetime import datetime, timedelta

def calculate_lagna(birth_datetime_utc, latitude, longitude, sunrise_time_ist):
    # Convert birth time to IST
    ist = pytz.timezone('Asia/Kolkata')
    birth_datetime_ist = birth_datetime_utc.astimezone(ist)
    
    # Calculate Local Mean Time (LMT)
    ist_offset = 82.5  # IST longitude is 82.5 degrees east
    lmt_offset = (longitude - ist_offset) * 4  # 4 minutes per degree
    birth_datetime_lmt = birth_datetime_ist - timedelta(minutes=lmt_offset)
    
    # Calculate Sidereal Time (ST)
    jd = julian_date(birth_datetime_lmt)
    gst = greenwich_sidereal_time(jd)
    lst = (gst + longitude / 15.0) % 24  # Local Sidereal Time in hours
    
    # Calculate the Lagna
    lagna_degrees = lst * 15  # Convert hours to degrees (15 degrees per hour)
    lagna_sign = int(lagna_degrees // 30) + 1  # 30 degrees per sign
    lagna_degrees %= 30  # Degrees within the sign
    
    return lagna_sign, lagna_degrees

def julian_date(dt):
    # Convert datetime to Julian Date
    year = dt.year
    month = dt.month
    day = dt.day + dt.hour / 24.0 + dt.minute / 1440.0 + dt.second / 86400.0
    
    if month <= 2:
        year -= 1
        month += 12
    
    a = year // 100
    b = 2 - a + a // 4
    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5
    
    return jd

def greenwich_sidereal_time(jd):
    # Calculate Greenwich Sidereal Time (GST) in hours
    t = (jd - 2451545.0) / 36525.0
    gst = 280.46061837 + 360.98564736629 * (jd - 2451545) + t * t * (0.000387933 - t / 38710000)
    gst = gst % 360
    if gst < 0:
        gst += 360
    return gst / 15  # Convert degrees to hours

# Example usage
from datetime import datetime

# Input: Birth time in UTC, latitude and longitude of Chennai, and sunrise time in IST
birth_datetime_utc = datetime(1999, 9, 17, 18, 32, tzinfo=pytz.UTC)  # 7:39 AM IST on 15th January 2024
latitude = 25.4381302  # Chennai latitude
longitude = 81.8338005   # Chennai longitude
sunrise_time_ist = datetime(1999, 9, 17, 18, 32, tzinfo=pytz.timezone('Asia/Kolkata'))

lagna_sign, lagna_degrees = calculate_lagna(birth_datetime_utc, latitude, longitude, sunrise_time_ist)
print(f"The Lagna at the time of birth is {lagna_degrees:.2f} degrees in sign number {lagna_sign}.")
