<!-- markdownlint-disable -->

<a href="../cv_aid/frame.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `cv_aid.frame`






---

<a href="../cv_aid/frame.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Frame`
A class to represent a frame of video. 

<a href="../cv_aid/frame.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(frame)
```

Initialize a Frame object. 

:param frame: The frame to be represented. :type frame: numpy.ndarray 


---

#### <kbd>property</kbd> channels

Get the number of channels in the frame. 

---

#### <kbd>property</kbd> haarcascades

Provides access to the haarcascades. 

---

#### <kbd>property</kbd> height

Get the height of the frame. 

---

#### <kbd>property</kbd> shape

Get the shape of the frame. 

---

#### <kbd>property</kbd> size

Get the size of the frame. 

---

#### <kbd>property</kbd> width

Get the width of the frame. 



---

<a href="../cv_aid/frame.py#L366"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `abs`

```python
abs() → Frame
```

Take the absolute value of the frame. 

:return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `blur`

```python
blur(ksize=5) → Frame
```

Blur the frame. 

:param ksize: The kernel size. :type ksize: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `box`

```python
box(x, y, width, height, color, thickness=1, line_type=8, is_max=False) → Frame
```

Draw a box on the frame. 

:param x: The x coordinate of the top left corner. :type x: int :param y: The y coordinate of the top left corner. :type y: int :param width: The width of the box. :type width: int :param height: The height of the box. :type height: int :param color: The color of the box. :type color: tuple :param thickness: The thickness of the box. :type thickness: int :param line_type: The type of the box. :type line_type: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L267"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `boxes`

```python
boxes(boxes, color, thickness=1, line_type=8, is_max=False) → Frame
```

Draw boxes on the frame. 

:param boxes: The boxes to draw. :type boxes: List[Tuple[int, int, int, int]] :param color: The color of the boxes. :type color: tuple :param thickness: The thickness of the boxes. :type thickness: int :param line_type: The type of the boxes. :type line_type: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `canny`

```python
canny(threshold1, threshold2) → Frame
```

Apply the Canny edge detector. 

:param threshold1: The first threshold. :type threshold1: int :param threshold2: The second threshold. :type threshold2: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop`

```python
crop(x, y, width, height) → Frame
```

Crop the frame. 

:param x: The x coordinate of the top left corner. :type x: int :param y: The y coordinate of the top left corner. :type y: int :param width: The width of the crop. :type width: int :param height: The height of the crop. :type height: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio`

```python
crop_to_ratio(ratio) → Frame
```

Crop the frame to a specific ratio. 

:param ratio: The ratio to crop to. :type ratio: float :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L153"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio_height`

```python
crop_to_ratio_height(ratio) → Frame
```

Crop the frame to a specific ratio. 

:param ratio: The ratio to crop to. :type ratio: float :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio_width`

```python
crop_to_ratio_width(ratio) → Frame
```

Crop the frame to a specific ratio. 

:param ratio: The ratio to crop to. :type ratio: float :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_size`

```python
crop_to_size(width, height) → Frame
```

Crop the frame to a specific size. 

:param width: The width of the frame. :type width: int :param height: The height of the frame. :type height: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `flip`

```python
flip(flip_code) → Frame
```

Flip the frame. 

:param flip_code: The code for the flip. :type flip_code: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `gray`

```python
gray() → Frame
```

Convert the frame to grayscale. 

:return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `line`

```python
line(start, end, color=(0, 255, 0), thickness=1, line_type=8) → Frame
```

Draw a line on the frame. 

:param start: The start of the line. :type start: tuple :param end: The end of the line. :type end: tuple :param color: The color of the line. :type color: tuple :param thickness: The thickness of the line. :type thickness: int :param line_type: The type of the line. :type line_type: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L244"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `lines`

```python
lines(points, color, thickness=1, line_type=8) → Frame
```

Draw lines on the frame. 

:param points: The points to draw. :type points: List[Tuple[int, int]] :param color: The color of the lines. :type color: tuple :param thickness: The thickness of the lines. :type thickness: int :param line_type: The type of the lines. :type line_type: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `load`

```python
load(path) → Frame
```

Load a frame from a file. 

:param path: Path to the file. :type path: str 

---

<a href="../cv_aid/frame.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `resize`

```python
resize(width=None, height=None, inter=3) → Frame
```

Resize the frame. 

:param width: The new width. :type width: int :param height: The new height. :type height: int :param inter: The interpolation method. :type inter: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `rotate`

```python
rotate(angle, center=None, scale=1.0, same_dim=True) → Frame
```

Rotate the frame. 

:param angle: The angle to rotate the frame by. :type angle: float :param center: The center of rotation. :type center: tuple :param scale: The scale to apply. :type scale: float :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L381"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `save`

```python
save(path, name)
```

Save the frame. 

:param path: The path to save the frame. :type path: str :param name: The name of the frame. :type name: str 

---

<a href="../cv_aid/frame.py#L373"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show`

```python
show(title='Frame') → None
```

Show the frame. 

:param title: The title of the frame. :type title: str 

---

<a href="../cv_aid/frame.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `text`

```python
text(
    text,
    position,
    font_face=0,
    font_scale=1.0,
    color=(0, 255, 0),
    thickness=1
) → Frame
```

Draw text on the frame. 

:param text: The text to draw. :type text: str :param position: The position of the text. :type position: tuple :param color: The color of the text. :type color: tuple :param font_face: The font face of the text. :type font_face: int :param font_scale: The font scale of the text. :type font_scale: float :param thickness: The thickness of the text. :type thickness: int :return: The resulting frame. 

---

<a href="../cv_aid/frame.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_bytes`

```python
to_bytes() → bytes
```

Convert the frame to bytes. 

:return: The resulting bytes. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
