"""Command line interface for the Mandelbrot application."""

import argparse
import sys

from .mandelbrot import draw_mandelbrot


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Mandelbrot set image."
    )
    parser.add_argument(
        "-o", "--output", default="mandelbrot.png",
        help="Output file (PNG).",
    )
    parser.add_argument(
        "--width", type=int, default=400,
        help="Image width in pixels.",
    )
    parser.add_argument(
        "--height", type=int, default=300,
        help="Image height in pixels.",
    )
    parser.add_argument(
        "--max-iter", type=int, default=1000,
        help="Maximum iterations for escape time.",
    )
    args = parser.parse_args()

    try:
        path = draw_mandelbrot(
            output_path=args.output,
            width=args.width,
            height=args.height,
            max_iter=args.max_iter,
        )
        print(f"Saved Mandelbrot image to {path}")
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
