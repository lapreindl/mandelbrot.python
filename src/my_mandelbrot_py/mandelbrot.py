"""Mandelbrot drawing utilities."""

from PIL import Image

     
def draw_mandelbrot(
    output_path: str,
    width: int = 800,
    height: int = 600,
    max_iter: int = 1000,
    x_center: float = -0.5,
    y_center: float = 0.0,
    scale: float = 3.0,
):
    """Render the Mandelbrot set to an image file.

    Parameters
    ----------
    output_path : str
        Path where the image will be saved (e.g. "mandelbrot.png").
    width : int
        Width of the generated image in pixels.
    height : int
        Height of the generated image in pixels.
    max_iter : int
        Maximum number of iterations for the escape time algorithm.
    x_center, y_center : float
        Center of the region in the complex plane.
    scale : float
        Width of the region in the complex plane (height is scaled accordingly).
    """
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for px in range(width):
        for py in range(height):
            # Map pixel position to complex plane
            x0 = x_center + (px - width / 2) * (scale / width)
            y0 = y_center + (py - height / 2) * (scale / width)
            x = 0.0
            y = 0.0
            iteration = 0
            while x * x + y * y <= 4.0 and iteration < max_iter:
                x_temp = x * x - y * y + x0
                y = 2 * x * y + y0
                x = x_temp
                iteration += 1
            color = 255 - int(iteration * 255 / max_iter)
            pixels[px, py] = (color, color, color)

    img.save(output_path)
    return output_path
