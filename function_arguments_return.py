import math

# Define the function to calculate the area of a circle
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * (radius ** 2)
    return area

# Set a specific radius value
radius_value = 5

# Call the function with the radius_value and store the result
area_result = circle_area(radius_value)

# Print the result, formatted to 2 decimal places
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
