# ShadowLoop - Predict Shadow Length using Python
# Author: Sakil Hasan Saikat
# GitHub: https://github.com/0xSaikat/shadowloop

import math

def shadow_length(height, angle_deg):
    """
    Calculate shadow length for a given object height and light angle.
    :param height: Object height
    :param angle_deg: Light angle in degrees (0 < angle < 90)
    :return: Shadow length
    """
    if angle_deg <= 0 or angle_deg >= 90:
        raise ValueError("Angle must be between 0 and 90 degrees (exclusive)")
    angle_rad = math.radians(angle_deg)
    return height / math.tan(angle_rad)


def light_angle(height, shadow):
    """
    Calculate light angle for a given object height and shadow length.
    :param height: Object height
    :param shadow: Shadow length
    :return: Light angle in degrees
    """
    if shadow <= 0:
        raise ValueError("Shadow length must be positive")
    angle_rad = math.atan(height / shadow)
    return math.degrees(angle_rad)


def main():
    print("Welcome to ShadowLoop - Shadow Prediction Tool\n")
    
    while True:
        print("Select an option:")
        print("1. Calculate shadow length from height & light angle")
        print("2. Calculate light angle from height & shadow length")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            try:
                h = float(input("Enter object height: "))
                angle = float(input("Enter light angle (degrees): "))
                s = shadow_length(h, angle)
                print(f"Shadow length: {s:.2f}\n")
            except Exception as e:
                print("Error:", e, "\n")
                
        elif choice == '2':
            try:
                h = float(input("Enter object height: "))
                s = float(input("Enter shadow length: "))
                angle = light_angle(h, s)
                print(f"Light angle: {angle:.2f}°\n")
            except Exception as e:
                print("Error:", e, "\n")
                
        elif choice == '3':
            print("Exiting ShadowLoop. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
