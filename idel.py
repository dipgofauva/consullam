def color_mapping(input_string):
    color_map = {}
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]
    
    for i, char in enumerate(set(input_string)):
        color_map[char] = colors[i % len(colors)]
    
    return color_map
