import cv2
import numpy as np

from cv_aid import utils


class Frame:  # pylint: disable=too-many-public-methods
    """A class to represent a frame of video."""

    def __init__(self, frame):
        """Initialize a Frame object.
        :param frame: The frame to be represented.
        """
        self.frame = frame
        self.original_frame = frame.copy()

    @classmethod
    def load(cls, path) -> "Frame":
        """Load a frame from a file.
        :param path: Path to the file.
        """
        return cls(cv2.imread(str(path)))

    @property
    def shape(self) -> tuple:
        """Get the shape of the frame."""
        return self.frame.shape

    @property
    def width(self) -> int:
        """Get the width of the frame."""
        return self.shape[1]

    @property
    def height(self) -> int:
        """Get the height of the frame."""
        return self.shape[0]

    @property
    def size(self) -> int:
        """Get the size of the frame."""
        return self.shape[:2]

    @property
    def channels(self) -> int:
        """Get the number of channels in the frame."""
        return self.shape[2]

    def save(self, path) -> None:
        """Save the frame to a file.
        :param path: Path to the file.
        """
        cv2.imwrite(str(path), self.frame)

    def to_bytes(self) -> bytes:
        """Convert the frame to bytes.
        :return: The resulting bytes.
        """
        return self.frame.tobytes()

    def gray(self) -> "Frame":
        """Convert the frame to grayscale.
        :return: The resulting frame.
        """
        return Frame(utils.gray(self.frame))

    def resize(self, width=None, height=None, inter=cv2.INTER_AREA) -> "Frame":
        """Resize the frame.
        :param width: The new width.
        :param height: The new height.
        :param inter: The interpolation method.
        :return: The resulting frame.
        """
        return Frame(utils.resize(self.frame, width, height, inter))

    def rotate(self, angle, center=None, scale=1.0) -> "Frame":
        """Rotate the frame.
        :param angle: The angle to rotate the frame by.
        :param center: The center of rotation.
        :param scale: The scale to apply.
        :return: The resulting frame.
        """
        return Frame(utils.rotate(self.frame, angle, center, scale))

    def flip(self, flip_code) -> "Frame":
        """Flip the frame.
        :param flip_code: The code for the flip.
        :return: The resulting frame.
        """
        return Frame(utils.flip(self.frame, flip_code))

    def crop(self, x, y, width, height) -> "Frame":  # pylint: disable=invalid-name
        """Crop the frame.
        :param x: The x coordinate of the top left corner.
        :param y: The y coordinate of the top left corner.
        :param width: The width of the crop.
        :param height: The height of the crop.
        :return: The resulting frame.
        """
        return Frame(utils.crop(self.frame, x, y, width, height))

    def crop_to_size(self, width, height) -> "Frame":
        """Crop the frame to a specific size.
        :param width: The width of the frame.
        :param height: The height of the frame.
        :return: The resulting frame.
        """
        return self.crop(0, 0, width, height)

    def crop_to_ratio(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.
        :param ratio: The ratio to crop to.
        :return: The resulting frame.
        """
        return self.crop_to_size(int(self.width / ratio), int(self.height / ratio))

    def crop_to_ratio_width(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.
        :param ratio: The ratio to crop to.
        :return: The resulting frame.
        """
        return self.crop_to_size(int(self.width / ratio), self.height)

    def crop_to_ratio_height(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.
        :param ratio: The ratio to crop to.
        :return: The resulting frame.
        """
        return self.crop_to_size(self.width, int(self.height / ratio))

    def blur(self, ksize=5) -> "Frame":
        """Blur the frame.
        :param ksize: The kernel size.
        :return: The resulting frame.
        """
        return Frame(utils.blur(self.frame, ksize))

    def canny(self, threshold1, threshold2) -> "Frame":
        """Apply the Canny edge detector.
        :param threshold1: The first threshold.
        :param threshold2: The second threshold.
        :return: The resulting frame.
        """
        return Frame(utils.canny(self.frame, threshold1, threshold2))

    def line(self, start, end, color, thickness=1, line_type=cv2.LINE_8) -> "Frame":
        """Draw a line on the frame.
        :param start: The start of the line.
        :param end: The end of the line.
        :param color: The color of the line.
        :param thickness: The thickness of the line.
        :param line_type: The type of the line.
        :return: The resulting frame.
        """
        return Frame(utils.line(self.frame, start, end, color, thickness, line_type))

    def box(
        self,
        x,
        y,
        width,
        height,
        color,
        thickness=1,
        line_type=cv2.LINE_8,  # pylint: disable=invalid-name
    ) -> "Frame":
        """Draw a box on the frame.
        :param x: The x coordinate of the top left corner.
        :param y: The y coordinate of the top left corner.
        :param width: The width of the box.
        :param height: The height of the box.
        :param color: The color of the box.
        :param thickness: The thickness of the box.
        :param line_type: The type of the box.
        :return: The resulting frame.
        """
        return Frame(
            utils.box(self.frame, x, y, width, height, color, thickness, line_type)
        )

    def lines(self, points, color, thickness=1, line_type=cv2.LINE_8) -> "Frame":
        """Draw lines on the frame.
        :param points: The points to draw.
        :param color: The color of the lines.
        :param thickness: The thickness of the lines.
        :param line_type: The type of the lines.
        :return: The resulting frame.
        """
        return Frame(
            utils.lines(
                self.frame,
                points,
                color=color,
                thickness=thickness,
                line_type=line_type,
            )
        )

    def boxes(self, boxes, color, thickness=1, line_type=cv2.LINE_8) -> "Frame":
        """Draw boxes on the frame.
        :param boxes: The boxes to draw.
        :param color: The color of the boxes.
        :param thickness: The thickness of the boxes.
        :param line_type: The type of the boxes.
        :return: The resulting frame.
        """
        return Frame(
            utils.boxes(
                self.frame, boxes, color=color, thickness=thickness, line_type=line_type
            )
        )

    def text(
        self,
        text,
        position,
        font_face=cv2.FONT_HERSHEY_SIMPLEX,
        font_scale=1.0,
        color=(0, 255, 0),
        thickness=1,
    ) -> "Frame":
        """Draw text on the frame.
        :param text: The text to draw.
        :param position: The position of the text.
        :param color: The color of the text.
        :param font_face: The font face of the text.
        :param font_scale: The font scale of the text.
        :return: The resulting frame.
        """
        return Frame(
            utils.text(
                self.frame,
                text,
                *position,
                font_face,
                font_scale,
                color,
                thickness,
            )
        )

    def __add__(self, other) -> "Frame":
        """Add two frames together.
        :param other: The other frame to be added.
        :return: The resulting frame.
        """
        return Frame(self.frame + other.frame)

    def __sub__(self, other) -> "Frame":
        """Subtract two frames.
        :param other: The other frame to be subtracted.
        :return: The resulting frame.
        """
        return Frame(self.frame - other.frame)

    def __mul__(self, other) -> "Frame":
        """Multiply two frames.
        :param other: The other frame to be multiplied.
        :return: The resulting frame.
        """
        return Frame(self.frame * other.frame)

    def __truediv__(self, other) -> "Frame":
        """Divide two frames.
        :param other: The other frame to be divided.
        :return: The resulting frame.
        """
        return Frame(self.frame / other.frame)

    def abs(self) -> "Frame":
        """Take the absolute value of the frame.
        :return: The resulting frame.
        """
        return Frame(np.abs(self.frame))
