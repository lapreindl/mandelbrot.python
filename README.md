# my-mandelbrot-py

A small Python application that generates an image of the Mandelbrot set.

## Installation

Install from source (editable mode):

```bash
python -m pip install -e .[dev]
```

You can also publish to PyPI later using `build`/`twine` and install via `pip install my-mandelbrot-py`.

## Usage

Generate a default image:

```bash
mandelbrot
```

Specify output file or dimensions:

```bash
mandelbrot -o output.png --width 1024 --height 768 --max-iter 2000
```

## Development

Run tests with pytest:

```bash
pytest
```

## Contributing

Contributions are welcome! Update the code, add tests, and open a pull request.  
Follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages to make publishing and changelog generation easier.

# Wos moch mer do
siehe Folie Aufgabe 2
