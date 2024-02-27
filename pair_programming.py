import math     # Overall Looks good, straightforward

def pol_to_cartesian(r, theta): # Where r (float)=radial distance from the origin 
                                # and theta (float)=angle in radians measured counterclockwise from the positive x-axis.
    x = r*math.cos(theta)    
    y = r*math.sin(theta)
    
    return x, y


def test_pol_to_cartesian():
    x, y = pol_to_cartesian(1, 0)      # Test Case 1: r = 1, theta = 0
    expected_x = 1
    expected_y = 0
    if x != expected_x:  # Check if values match
        print("Test Case 1 Failed: x-coordinate incorrect. Expected:", expected_x, "Actual:", x)
        return False
    if y != expected_y:
        print("Test Case 1 Failed: y-coordinate incorrect. Expected:", expected_y, "Actual:", y)
        return False

    x, y = pol_to_cartesian(2, math.pi/4)  # Test Case 2: r = 2, theta = pi/4
    expected_x = math.sqrt(2)
    expected_y = math.sqrt(2)
    if x != expected_x:
        print("Test Case 2 Failed: x-coordinate incorrect. Expected:", expected_x, "Actual:", x)
        return False
    if y != expected_y:
        print("Test Case 2 Failed: y-coordinate incorrect. Expected:", expected_y, "Actual:", y)
        return False

    print("All test cases passed.")     # All test cases passed
    return True

test_pol_to_cartesian()  # Call the function to test
