import cv2
import numpy as np

def nothing(x):
    pass

# Create a window and trackbars for HSV adjustment
cv2.namedWindow('Adjust HSV')
cv2.createTrackbar('Hue', 'Adjust HSV', 0, 179, nothing)
cv2.createTrackbar('Saturation', 'Adjust HSV', 0, 255, nothing)
cv2.createTrackbar('Value', 'Adjust HSV', 0, 255, nothing)

# Initialize with the approximate HSV values for light brown
hue_init = 25
saturation_init = 100
value_init = 150

cv2.setTrackbarPos('Hue', 'Adjust HSV', hue_init)
cv2.setTrackbarPos('Saturation', 'Adjust HSV', saturation_init)
cv2.setTrackbarPos('Value', 'Adjust HSV', value_init)

# Convert hex to RGB
hex_color = '#C4A484'
rgb_color = np.array([int(hex_color[i:i+2], 16) for i in (1, 3, 5)])

# Reshape the array to match the OpenCV format
rgb_color = rgb_color.reshape(1, 1, 3)

while True:
    # Get trackbar positions
    hue = cv2.getTrackbarPos('Hue', 'Adjust HSV')
    saturation = cv2.getTrackbarPos('Saturation', 'Adjust HSV')
    value = cv2.getTrackbarPos('Value', 'Adjust HSV')

    # Define lower and upper bounds
    lower_brown = np.array([max(0, hue - 10), max(0, saturation - 50), max(0, value - 50)])
    upper_brown = np.array([min(179, hue + 10), min(255, saturation + 50), min(255, value + 50)])

    # Print the HSV range
    print("Lower HSV values:", lower_brown)
    print("Upper HSV values:", upper_brown)

    # Convert RGB to HSV
    hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV)

    # Create a mask using inRange
    mask = cv2.inRange(hsv_color, lower_brown, upper_brown)

    # Display the mask
    cv2.imshow('Mask', mask)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the window
cv2.destroyAllWindows()
