"""Top-level package for the my-mandelbrot-py project."""

__version__ = "0.1.0"

from .mandelbrot import draw_mandelbrot  # expose function


# allow running with `python -m my_mandelbrot_py`


def _run():
    # avoid circular import when package is imported
    from .cli import main

    main()


if __name__ == "__main__":
    _run()
