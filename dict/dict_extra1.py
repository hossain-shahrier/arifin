color_sequence = input("Enter the color sequence (R for Red, G for Green, B for Blue): ")

red_count = 0
green_count = 0
blue_count = 0

for color in color_sequence:
    if color == "R":
        red_count += 1
    elif color == "G":
        green_count += 1
    elif color == "B":
        blue_count += 1

color_choices = []
if red_count >= 1:
    color_choices.append(("Red", red_count))
if green_count >= 1:
    color_choices.append(("Green", green_count))
if blue_count >= 1:
    color_choices.append(("Blue", blue_count))

# print the result
print(tuple(color_choices))
