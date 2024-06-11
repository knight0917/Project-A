class ZodiacSign:
    def __init__(self, name):
        self.name = name
        self.degrees = list(range(30))  # 0 to 29 degrees

    def __repr__(self):
        return f"ZodiacSign(name={self.name}, degrees=0-29)"

class Planet:
    def __init__(self, name):
        self.name = name
        self.position = None  # To be assigned to a zodiac sign and degree

    def assign_position(self, zodiac_sign, degree):
        if degree not in zodiac_sign.degrees:
            raise ValueError(f"Degree {degree} is not valid for {zodiac_sign.name}")
        self.position = (zodiac_sign, degree)

    def __repr__(self):
        if self.position:
            zodiac_sign, degree = self.position
            return f"Planet(name={self.name}, position={zodiac_sign.name} {degree}°)"
        return f"Planet(name={self.name}, position=None)"

# List of Zodiac Signs
zodiac_signs = [
    ZodiacSign("Aries"),
    ZodiacSign("Taurus"),
    ZodiacSign("Gemini"),
    ZodiacSign("Cancer"),
    ZodiacSign("Leo"),
    ZodiacSign("Virgo"),
    ZodiacSign("Libra"),
    ZodiacSign("Scorpio"),
    ZodiacSign("Sagittarius"),
    ZodiacSign("Capricorn"),
    ZodiacSign("Aquarius"),
    ZodiacSign("Pisces")
]

# List of Planets including Rahu and Ketu
planets = [
    Planet("Sun"),
    Planet("Moon"),
    Planet("Mercury"),
    Planet("Venus"),
    Planet("Mars"),
    Planet("Jupiter"),
    Planet("Saturn"),
    Planet("Rahu"),
    Planet("Ketu")
]

# Example of assigning positions to planets
planets[0].assign_position(zodiac_signs[0], 15)  # Sun in Aries at 15 degrees
planets[1].assign_position(zodiac_signs[1], 10)  # Moon in Taurus at 10 degrees

# Print out the planets with their positions
for planet in planets:
    print(planet)
