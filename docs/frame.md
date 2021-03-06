<!-- markdownlint-disable -->

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `frame`






---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Frame`
A class to represent a frame of video. 

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(frame)
```

Initialize a Frame object. 



**Args:**
 
 - <b>`frame`</b> (numpy.ndarray):  The frame to wrap. 


---

#### <kbd>property</kbd> channels

Get the number of channels in the frame. 

---

#### <kbd>property</kbd> dlib

Provides access to the dlib. 

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

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L429"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `abs`

```python
abs() → Frame
```

Take the absolute value of the frame. 

:return: The resulting frame. 



**Args:**
 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `blur`

```python
blur(ksize=5) → Frame
```

Blur the frame. 



**Args:**
 
 - <b>`ksize`</b> (int, optional):  The kernel size. (Default value = 5) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `box`

```python
box(x, y, width, height, color, thickness=1, line_type=8, is_max=False) → Frame
```

Draw a box on the frame. 



**Args:**
 
 - <b>`x`</b> (int):  The x coordinate of the top left corner. 
 - <b>`y`</b> (int):  The y coordinate of the top left corner. 
 - <b>`width`</b> (int):  The width of the box. 
 - <b>`height`</b> (int):  The height of the box. 
 - <b>`color`</b> (tuple):  The color of the box. 
 - <b>`thickness`</b> (int, optional):  The thickness of the box. (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  The type of the box. (Default value = cv2.LINE_8) 
 - <b>`is_max`</b> (bool, optional):  Whether or not to draw the max box. (Default value = False) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `boxes`

```python
boxes(boxes, color, thickness=1, line_type=8, is_max=False) → Frame
```

Draw boxes on the frame. 



**Args:**
 
 - <b>`boxes`</b> (List[Tuple[int, int, int, int]]):  The boxes to draw. 
 - <b>`color`</b> (tuple):  The color of the boxes. 
 - <b>`thickness`</b> (int, optional):  The thickness of the boxes. (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  The type of the boxes. (Default value = cv2.LINE_8) 
 - <b>`is_max`</b>:  Default value = False) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `canny`

```python
canny(threshold1, threshold2) → Frame
```

Apply the Canny edge detector. 



**Args:**
 
 - <b>`threshold1`</b> (int):  The first threshold. 
 - <b>`threshold2`</b> (int):  The second threshold. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L245"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `circle`

```python
circle(center, radius, color=(0, 255, 0), thickness=1, line_type=8) → Frame
```

Draw a circle on the frame. 



**Args:**
 
 - <b>`center`</b> (tuple):  The center of the circle. 
 - <b>`radius`</b> (int):  The radius of the circle. 
 - <b>`color`</b> (tuple, optional):  The color of the circle. (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  The thickness of the circle. (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  The type of the circle. (Default value = cv2.LINE_8) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop`

```python
crop(x, y, width, height) → Frame
```

Crop the frame. 



**Args:**
 
 - <b>`x`</b> (int):  The x coordinate of the top left corner. 
 - <b>`y`</b> (int):  The y coordinate of the top left corner. 
 - <b>`width`</b> (int):  The width of the crop. 
 - <b>`height`</b> (int):  The height of the crop. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio`

```python
crop_to_ratio(ratio) → Frame
```

Crop the frame to a specific ratio. 



**Args:**
 
 - <b>`ratio`</b> (float):  The ratio to crop to. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio_height`

```python
crop_to_ratio_height(ratio) → Frame
```

Crop the frame to a specific ratio. 



**Args:**
 
 - <b>`ratio`</b> (float):  The ratio to crop to. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_ratio_width`

```python
crop_to_ratio_width(ratio) → Frame
```

Crop the frame to a specific ratio. 



**Args:**
 
 - <b>`ratio`</b> (float):  The ratio to crop to. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop_to_size`

```python
crop_to_size(width, height) → Frame
```

Crop the frame to a specific size. 



**Args:**
 
 - <b>`width`</b> (int):  The width of the frame. 
 - <b>`height`</b> (int):  The height of the frame. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `flip`

```python
flip(flip_code) → Frame
```

Flip the frame. 



**Args:**
 
 - <b>`flip_code`</b> (int):  The code for the flip. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `gray`

```python
gray() → Frame
```

Convert the frame to grayscale. 

:return: The resulting frame. 



**Args:**
 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `line`

```python
line(start, end, color=(0, 255, 0), thickness=1, line_type=8) → Frame
```

Draw a line on the frame. 



**Args:**
 
 - <b>`start`</b> (tuple):  The start of the line. 
 - <b>`end`</b> (tuple):  The end of the line. 
 - <b>`color`</b> (tuple, optional):  The color of the line. (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  The thickness of the line. (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  The type of the line. (Default value = cv2.LINE_8) 
 - <b>`255`</b>:  param 0): 0): 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L306"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `lines`

```python
lines(points, color, thickness=1, line_type=8) → Frame
```

Draw lines on the frame. 



**Args:**
 
 - <b>`points`</b> (List[Tuple[int, int]]):  The points to draw. 
 - <b>`color`</b> (tuple):  The color of the lines. 
 - <b>`thickness`</b> (int, optional):  The thickness of the lines. (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  The type of the lines. (Default value = cv2.LINE_8) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `load`

```python
load(path) → Frame
```

Load a frame from a file. 



**Args:**
 
 - <b>`path`</b> (str):  Path to the file. 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `resize`

```python
resize(width=None, height=None, inter=3) → Frame
```

Resize the frame. 



**Args:**
 
 - <b>`width`</b> (int, optional):  The new width. (Default value = None) 
 - <b>`height`</b> (int, optional):  The new height. (Default value = None) 
 - <b>`inter`</b> (inter: inter: int, optional):  The interpolation method. (Default value = cv2.INTER_AREA) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `rotate`

```python
rotate(angle, center=None, scale=1.0, same_dim=True) → Frame
```

Rotate the frame. 



**Args:**
 
 - <b>`angle`</b> (float):  The angle to rotate the frame by. 
 - <b>`center`</b> (tuple, optional):  The center of rotation. (Default value = None) 
 - <b>`scale`</b> (float, optional):  The scale to apply. (Default value = 1.0) 
 - <b>`same_dim`</b>:  Default value = True) 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L452"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `save`

```python
save(name, path='./')
```

Save the frame. 



**Args:**
 
 - <b>`path`</b> (str):  The path to save the frame. 
 - <b>`name`</b> (str):  The name of the frame. 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L441"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show`

```python
show(title='Frame') → None
```

Show the frame. 



**Args:**
 
 - <b>`title`</b> (str, optional):  The title of the frame. (Default value = "Frame") 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L356"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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



**Args:**
 
 - <b>`text`</b> (str):  The text to draw. 
 - <b>`position`</b> (tuple):  The position of the text. 
 - <b>`color`</b> (tuple, optional):  The color of the text. (Default value = (0) 
 - <b>`font_face`</b> (int, optional):  The font face of the text. (Default value = cv2.FONT_HERSHEY_SIMPLEX) 
 - <b>`font_scale`</b> (float, optional):  The font scale of the text. (Default value = 1.0) 
 - <b>`thickness`</b> (int, optional):  The thickness of the text. (Default value = 1) 
 - <b>`255`</b>:  param 0): 0): 



**Returns:**
 The resulting frame. 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/frame.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_bytes`

```python
to_bytes() → bytes
```

Convert the frame to bytes. 



**Returns:**
  The resulting bytes. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
