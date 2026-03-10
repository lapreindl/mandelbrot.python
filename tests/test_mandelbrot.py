import os

from my_mandelbrot_py import draw_mandelbrot


def test_draw_creates_file(tmp_path):
    output = tmp_path / "test.png"
    result = draw_mandelbrot(str(output), width=100, height=80, max_iter=10)
    assert os.path.exists(result)
    # check that the file is non-empty
    assert os.path.getsize(result) > 0
    # confirm dimensions are correct
    from PIL import Image
    img = Image.open(result)
    assert img.size == (100, 80)


def test_cli_invocation(tmp_path, capsys):
    from my_mandelbrot_py import cli

    out_file = tmp_path / "cli.png"
    sys_args = ["prog", "-o", str(out_file), "--width", "50", "--height", "40"]
    import sys
    orig = sys.argv
    sys.argv = sys_args
    try:
        cli.main()
    finally:
        sys.argv = orig
    captured = capsys.readouterr()
    assert "Saved Mandelbrot image" in captured.out
    assert out_file.exists()
