#great circle better for short distances. see: https://www.section.io/engineering-education/using-geopy-to-calculate-the-distance-between-two-points
from geopy.distance import great_circle as GRC

# Define coordinates
first_coordinate = (51.498172, -0.272888)
second_coordinate = (51.496467, -0.273953)

# Calculate distance
distance_between_points = round(GRC(first_coordinate, second_coordinate).km, 2)

# Display the result
print(f"The distance between the two points is: {distance_between_points} km")
