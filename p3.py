def display_first_and_last_colors(color_list):
    if len(color_list) >= 1:
        first_color = color_list[0]
        print("Перший колір:", first_color)

    if len(color_list) >= 2:
        last_color = color_list[-1]
        print("Останній колір:", last_color)

color_list = ["Red", "Green", "White", "Black"]
display_first_and_last_colors(color_list)
