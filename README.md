# cv-aid
CV Aid is a set of helpers of computer vision tasks.

## Installation

`pip install cv-aid`

### From source

```
git clone https://github.com/khalidelboray/cv-aid
cd cv-aid
poetry install
poetry run python setup.py install
```

## Tests

`poetry run test`

all tests are in `tests/` directory.

## Examples

- Basic Frame Functions

    ```python
    from cv_aid import Frame

    frame = Frame.load('/path/to/image.jpg')
    # or
    import cv2
    frame = Frame(cv2.imread('/path/to/image.jpg'))

    # Grayscale image
    gray = frame.gray()

    # Resize image
    small = frame.resize(width=100, height=100)

    # Crop image
    cropped = frame.crop(x=100, y=100, width=100, height=100)

    # All methods return a new Frame object, so you can chain them
    new_frame = frame.resize(width=100, height=100).crop(x=100, y=100, width=100, height=100)

    # Save image
    frame.save('/path/to/image.jpg')
    ```

- Basic Video Functions

