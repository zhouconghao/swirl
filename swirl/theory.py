def calculate_angle(x, y):
    """
    Calculate the angle from the positive x-axis to the point (x, y)
    in a counterclockwise direction.
    
    Args:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.
    
    Returns:
    float: The angle in degrees.
    """
    angle_radians = np.arctan2(y, x)
    angle_degrees = np.degrees(angle_radians)

    angle_degrees_positive = np.where(angle_degrees < 0, angle_degrees + 360, angle_degrees)

    
    # Ensure the angle is in the range [0, 360)
    # if angle_degrees < 0:
    #     angle_degrees += 360
    
    return angle_degrees_positive