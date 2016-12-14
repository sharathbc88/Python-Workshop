COLORS_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2" : "#eedfcc", "AntiqueWhite3": "#cdc0b0",
                "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

color_name = str(input("Enter the color name for the hexadecimal code: "))
print(color_name)

while color_name != "":
    if color_name in COLORS_CODES:
        print(color_name, "is", COLORS_CODES[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter the color name for the hexadecimal code: ")

