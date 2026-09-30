import os
import cv2
import numpy as np
from PIL import Image

# ASCII Character density ramps
RAMPS = {
    "standard": " .:-=+*#%@",
    "detailed": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "blocks": " ░▒▓█",
    "binary": " 01",
    "minimal": " .#"
}

def image_to_ascii(
    file_bytes: bytes,
    target_width: int = 100,
    style: str = "standard",
    invert: bool = False,
    contrast: float = 1.0,
    color_mode: bool = False
):
    """
    Converts raw image bytes to ASCII art with options for width, style,
    contrast, inverted brightness, and color tags.
    """
    # 1. Decode image from bytes using OpenCV
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise ValueError("Invalid image file.")

    orig_h, orig_w = img_bgr.shape[:2]

    # 2. Aspect Ratio Correction: Monospace characters are roughly 2x taller than wide
    char_aspect_ratio = 0.55
    target_height = int((orig_h / orig_w) * target_width * char_aspect_ratio)
    target_height = max(1, target_height)

    # 3. Resize image to fit ASCII grid
    img_resized = cv2.resize(img_bgr, (target_width, target_height), interpolation=cv2.INTER_AREA)

    # 4. Convert to grayscale & apply contrast adjustment
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    if contrast != 1.0:
        # Scale intensity around midpoint 128
        img_gray = np.clip(128.0 + contrast * (img_gray.astype(np.float32) - 128.0), 0, 255).astype(np.uint8)

    # 5. Invert brightness if dark mode / light characters requested
    if invert:
        img_gray = 255 - img_gray

    # 6. Select ramp and map pixels to characters
    ramp = RAMPS.get(style, RAMPS["standard"])
    num_chars = len(ramp)

    # Vectorized character mapping using NumPy
    indices = (img_gray.astype(np.float32) * (num_chars - 1) / 255.0).astype(int)

    # 7. Output generation
    if not color_mode:
        # Plain text generation (fastest)
        lines = []
        for row in indices:
            lines.append("".join(ramp[idx] for idx in row))
        ascii_text = "\n".join(lines)
        return {"type": "text", "content": ascii_text, "width": target_width, "height": target_height}
    else:
        # Color HTML generation: encode RGB spans
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        html_lines = []
        for y in range(target_height):
            line_parts = []
            for x in range(target_width):
                char = ramp[indices[y, x]]
                if char == " ":
                    char = "&nbsp;"
                r, g, b = img_rgb[y, x]
                line_parts.append(f'<span style="color:rgb({r},{g},{b})">{char}</span>')
            html_lines.append("".join(line_parts))
        html_content = "<br>".join(html_lines)
        return {"type": "html", "content": html_content, "width": target_width, "height": target_height}
