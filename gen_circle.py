import re
from PIL import ImageColor


def hex_to_rgb(hex_color):
    return ImageColor.getcolor(hex_color, "RGB")


def create_html(colors):
    html_string = "<html><body>"

    for color_group in colors:
        html_string += "<div style='display: flex; flex-direction: row;'>"
        for color in color_group:
            rgb = hex_to_rgb(color)
            html_string += f"""
            <div style='margin: 10px; padding: 20px; text-align: center;'>
                <div style='background-color: {color}; border-radius: 50%; width: 50px; height: 50px; margin: 0 auto;'></div>
                <p>Hex: {color}</p>
                <p>RGB: {rgb}</p>
            </div>
            """
        html_string += "</div>"

    html_string += "</body></html>"

    with open("colors2.html", "w") as f:
        f.write(html_string)


def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    color_pattern = r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})'
    colors = [re.findall(color_pattern, line) for line in lines]

    colors = [['#' + color for color in color_group] for color_group in colors]

    create_html(colors)


if __name__ == "__main__":
    process_file('colors.txt')  # 请将这里的 'colors.txt' 更改为你的文件路径
