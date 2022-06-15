# src/background.py

from random import randint

from js import alert, setInterval, setTimeout, clearInterval
from pyodide import create_once_callable, create_proxy


def callback() -> None:
    """
    Sets the document’s background to a random color.

    Parameters:
        None

    Returns:
        None
    """
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    document.body.style.backgroundColor = f"rgb({r}, {b}, {b})"


interval_id = setInterval(create_proxy(callback), 1000)

_ = setTimeout(
    create_once_callable(
        lambda: clearInterval(interval_id)
    ),
    10000
)
