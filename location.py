from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude
def get_lat_lon(place_name):
    try:
        print(f"Geocoding place: {place_name}")
        location = geolocator.geocode(place_name, timeout=10)
        if location:
            print(f"Location found: {location}")
            return location.latitude, location.longitude
        else:
            print("Location not found.")
            return None, None
    except GeocoderTimedOut:
        print("Geocoding timed out.")
        return None, None
    except GeocoderServiceError as e:
        print(f"Geocoding service error: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

place_name = input("Enter place name: ")
latitude, longitude = get_lat_lon(place_name)

if latitude is not None and longitude is not None:
    print(f"The latitude and longitude of {place_name} are {latitude}, {longitude}")
else:
    print(f"Could not find the location: {place_name}")
