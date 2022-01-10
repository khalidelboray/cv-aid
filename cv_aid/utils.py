import itertools
from pathlib import Path
from typing import Generator, Iterable

import cv2
import filetype
import numpy as np
from deepstack_sdk import ServerConfig


def find_images(path: Path) -> Generator:
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_image(file):
            yield file


def find_videos(path: Path) -> Generator:
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_video(file):
            yield file


def find_fonts(path: Path) -> Generator:
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_font(file):
            yield file


def width(frame: np.ndarray) -> int:
    return frame.shape[1]


def height(frame: np.ndarray) -> int:
    return frame.shape[0]


def rotate(img: np.ndarray, angle, center=None, scale=1.0) -> np.ndarray:
    # get the dimensions of the image
    (height, width) = img.shape[:2]

    # if the center is None, initialize it as the center of the image
    if center is None:
        center = (width / 2, height / 2)

    # the rotation
    rota_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, rota_matrix, (width, height))

    # return the rotated image
    return rotated_img


def resize(img: np.ndarray, width, height, inter=cv2.INTER_AREA) -> np.ndarray:
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        ratio = height / float(height)
        dim = (int(img.shape[1] * ratio), height)
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        ratio = width / float(width)
        dim = (width, int(height * ratio))

    # resize the image
    resized = cv2.resize(img, dim, interpolation=inter)

    return resized


def concatenate(image1: np.ndarray, image2: np.ndarray, axis=1) -> np.ndarray:
    return np.concatenate((image1, image2), axis=axis)


def batch(iterable: Iterable, n: int) -> Generator:
    it = iter(iterable)
    while item := list(itertools.islice(it, n)):
        yield item


def is_type(obj, type_name):
    return type(obj).__name__ == type_name


def verify_frame_type(func):
    def wrapper(self, frame):
        if is_type(frame, "Frame"):
            raise TypeError("The frame must be a Frame object")
        return func(self, frame)

    return wrapper


def copy_frame(func):
    def wrapper(*args, **kwargs):
        frame = args[0]
        new_frame = type(frame)(frame.frame.copy())
        return func(new_frame, *args[1:], **kwargs)

    return wrapper


def verify_deepstack_config(func):
    def wrapper(self, *args, **kwargs):
        server_config = kwargs.get("config")
        if server_config is None:
            try:
                server_config = args[1]
            except KeyError:
                raise ValueError("The server_config must be a ServerConfig object")

        if server_config is None or not isinstance(server_config, ServerConfig):
            raise ValueError("The server_config must be a ServerConfig object")
        if self.server_config.server_url is None:
            raise ValueError("The server_config must have a server_url")

        return func(self, *args, **kwargs)

    return wrapper


class TemplateResponse(object):
    def __init__(self, frame, loc, template):
        self.frame = frame
        self.loc = loc
        self.template = template
        self.w = template.shape[1]
        self.h = template.shape[0]
        self.orig = frame.copy()

    def draw_boxes(self):
        for x, y, w, h, color in self.boxes():
            self.frame = box(self.frame, x, y, w, h, color)
        return self

    def __len__(self):
        return len(self.boxes())

    def __repr__(self):
        return "TemplateResponse({})".format(self.frame)

    def boxes(self, color=(0, 255, 0)) -> Generator:
        for pt in zip(*self.loc[::-1]):
            yield [pt[0], pt[1], pt[0] + self.w, pt[1] + self.h, color]


# OpenCV functions


def gray(frame: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def crop(frame: np.ndarray, x, y, w, h) -> np.ndarray:
    return frame[y : y + h, x : x + w]


def blur(frame: np.ndarray, ksize=(5, 5)) -> np.ndarray:
    return cv2.GaussianBlur(frame, ksize, 0)


def line(
    frame: np.ndarray, start: tuple, end: tuple, color=(0, 255, 0), thickness=2
) -> np.ndarray:
    return cv2.line(frame, start, end, color, thickness)


def lines(frame, lines: list):
    for line in lines:
        frame = line(frame, *line)
    return frame


def box(frame: np.ndarray, x, y, w, h, color=(0, 255, 0), max=False) -> np.ndarray:
    if max:
        frame = cv2.rectangle(frame, (x, y), (w, h), color, 2)
    else:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    return frame


def text(
    frame: np.ndarray,
    text: str,
    x: int,
    y: int,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2,
) -> np.ndarray:
    frame = cv2.putText(frame, str(text), (x, y), font, scale, color, thickness)
    return frame


def text_above_box(
    frame: np.ndarray,
    text_: str,
    box: tuple,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2,
) -> np.ndarray:
    x, y, w, h = box
    frame = text(
        frame=frame,
        text=text_,
        x=x - 10,
        y=y - 10,
        font=font,
        scale=scale,
        color=color,
        thickness=thickness,
    )
    return frame


def search(frame, template, method=cv2.TM_CCOEFF_NORMED, threshold=0.8):
    if is_type(template, "Frame"):
        template = template.frame
    result = cv2.matchTemplate(frame, template, method)
    loc = np.where(result >= threshold)
    return TemplateResponse(frame, loc, template)


def stack(frames: list, resize_=None, cols=2) -> np.ndarray:

    # The minimum width and height of the stack is the width and height of the smallest frame
    min_width = min([width(frame) for frame in frames])
    min_height = min([height(frame) for frame in frames])

    if resize_ is not None:
        min_width = resize_[0]
        min_height = resize_[1]
    # Resize each frame to the minimum width and height
    frames = [resize(frame, min_width, min_height) for frame in frames]

    # Calculate the width and height of the stack by summing the width and height of each frame
    _width = sum([width(frame) for frame in frames])
    _height = sum([height(frame) for frame in frames])
    if cols is not None:
        _width = min_width * cols
        rows_count = int((len(frames) / cols))
        if len(frames) % cols != 0:
            rows_count += 1
        _height = rows_count * min_height

    stacked = np.zeros((_height, _width, 3), np.uint8)

    frames_as_rows = batch(frames, cols)
    for row_index, row in enumerate(frames_as_rows):
        for col_index, frame in enumerate(row):
            x = col_index * min_width
            y = row_index * min_height
            stacked[y : y + height(frame), x : x + width(frame)] = frame
        if len(row) < cols:
            # Fill the remaining space with white
            x = (col_index * min_width) + (cols - len(row)) * min_width
            y = row_index * min_height

            stacked[
                y : y + min_height,
                x - (min_width * ((cols - len(row)) - 1)) : x + min_width,
            ] = 255

    return stacked
