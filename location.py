from geopy.geocoders import Nominatim


# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude
def get_lat_lon(place_name):
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


place_name = input("Enter place name: ")
latitude, longitude = get_lat_lon(place_name)
print(f"The latitude and longitude of {place_name} are {latitude}, {longitude}")







