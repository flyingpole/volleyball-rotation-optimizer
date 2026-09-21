from PIL import Image, ImageDraw
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(OUT_DIR, exist_ok=True)

BG = (47, 102, 144, 255)   # matches --accent-2
FG = (255, 255, 255, 255)


def make_icon(size, filename, padding_ratio):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    radius = size * 0.22
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=BG)

    margin = size * padding_ratio
    ball_box = [margin, margin, size - margin, size - margin]
    draw.ellipse(ball_box, fill=FG)

    line_color = BG
    width = max(2, round(size * 0.022))
    cx, cy = size / 2, size / 2
    r = (size - 2 * margin) / 2

    draw.arc(ball_box, start=205, end=335, fill=line_color, width=width)
    draw.arc(ball_box, start=25, end=155, fill=line_color, width=width)
    draw.line([cx - r * 0.92, cy, cx + r * 0.92, cy], fill=line_color, width=width)

    img.save(os.path.join(OUT_DIR, filename))


# Standard icons (used as-is, little padding)
make_icon(192, "icon-192.png", 0.14)
make_icon(512, "icon-512.png", 0.14)

# Maskable icons need extra padding so the OS can safely crop to a circle/squircle
make_icon(192, "icon-maskable-192.png", 0.24)
make_icon(512, "icon-maskable-512.png", 0.24)

print("done")
