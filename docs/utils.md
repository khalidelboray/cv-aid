<!-- markdownlint-disable -->

<a href="../cv_aid/utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils`





---

<a href="../cv_aid/utils.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_images`

```python
find_images(path: Path) → Generator
```

Finds all images in a directory. 



**Args:**
 
 - <b>`path`</b> (Path):  path to the directory to search in 
 - <b>`path`</b>:  Path:  



**Returns:**
 generator of all images in the directory 


---

<a href="../cv_aid/utils.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_videos`

```python
find_videos(path: Path) → Generator
```

Finds all videos in a directory. 



**Args:**
 
 - <b>`path`</b> (Path):  path to the directory to search in 
 - <b>`path`</b>:  Path:  



**Returns:**
 generator of all videos in the directory 


---

<a href="../cv_aid/utils.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_fonts`

```python
find_fonts(path: Path) → Generator
```

Finds all fonts in a directory. 



**Args:**
 
 - <b>`path`</b> (Path):  path to the directory to search in 
 - <b>`path`</b>:  Path:  



**Returns:**
 generator of all fonts in the directory 


---

<a href="../cv_aid/utils.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rotate`

```python
rotate(img: ndarray, angle, center=None, scale=1.0, same_dim=True) → ndarray
```

Rotates an image. 



**Args:**
 
 - <b>`img`</b> (np.ndarray):  image to rotate 
 - <b>`angle`</b> (int):  angle to rotate the image by 
 - <b>`center`</b> (tuple, optional):  center of the image to rotate around (Default value = None) 
 - <b>`scale`</b> (float, optional):  scale of the image (Default value = 1.0) 
 - <b>`same_dim`</b> (bool, optional):  if True, the image will be resized to the same dimensions as the original (Default value = True) 
 - <b>`img`</b>:  np.ndarray:  



**Returns:**
 rotated image 


---

<a href="../cv_aid/utils.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `resize`

```python
resize(img: ndarray, width, height, inter=3) → ndarray
```

Resizes an image. 



**Args:**
 
 - <b>`img`</b> (np.ndarray):  image to resize 
 - <b>`width`</b> (int):  width of the resized image 
 - <b>`height`</b> (int):  height of the resized image 
 - <b>`inter`</b> (inter: int, optional):  interpolation method (Default value = cv2.INTER_AREA) 
 - <b>`img`</b>:  np.ndarray:  



**Returns:**
 resized image 


---

<a href="../cv_aid/utils.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `concatenate`

```python
concatenate(image1: ndarray, image2: ndarray, axis=1) → ndarray
```

Concatenates two images. 



**Args:**
 
 - <b>`image1`</b> (np.ndarray):  first image to concatenate 
 - <b>`image2`</b> (np.ndarray):  second image to concatenate 
 - <b>`axis`</b> (int, optional):  axis to concatenate the images on (Default value = 1) 
 - <b>`image1`</b>:  np.ndarray:  
 - <b>`image2`</b>:  np.ndarray:  



**Returns:**
 concatenated image 


---

<a href="../cv_aid/utils.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `batch`

```python
batch(iterable: Iterable, length: int) → Generator
```

Batches an iterable. 



**Args:**
 
 - <b>`iterable`</b> (Iterable):  iterable to batch 
 - <b>`n`</b> (int):  number of items to batch 
 - <b>`iterable`</b>:  Iterable:  
 - <b>`length`</b>:  int:  



**Returns:**
 generator of batches 


---

<a href="../cv_aid/utils.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_type`

```python
is_type(obj, type_name)
```

Checks if an object is of a certain type. 



**Args:**
 
 - <b>`obj`</b> (object):  object to check 
 - <b>`type_name`</b> (str):  name of the type to check 



**Returns:**
 True if the object is of the type, False otherwise 


---

<a href="../cv_aid/utils.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `verify_frame_type`

```python
verify_frame_type(func)
```

Verifies that the frame type is correct. 



**Args:**
 
 - <b>`func`</b> (function):  function to decorate 



**Returns:**
 decorated function 


---

<a href="../cv_aid/utils.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `copy_frame`

```python
copy_frame(func)
```

Copies the frame before applying the function. 



**Args:**
 
 - <b>`func`</b> (function):  function to decorate 



**Returns:**
 decorated function 


---

<a href="../cv_aid/utils.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `verify_deepstack_config`

```python
verify_deepstack_config(func)
```

Verifies that the DeepStack config is correct. 



**Args:**
 
 - <b>`func`</b> (function):  function to decorate 



**Returns:**
 decorated function 


---

<a href="../cv_aid/utils.py#L347"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gray`

```python
gray(frame: ndarray) → ndarray
```

Converts a color image to grayscale. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to convert to grayscale 
 - <b>`frame`</b>:  np.ndarray:  



**Returns:**
 grayscale image 


---

<a href="../cv_aid/utils.py#L361"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `crop`

```python
crop(frame: ndarray, x, y, width, height) → ndarray
```

Crops an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to crop 
 - <b>`x`</b> (int):  x coordinate of the top left corner 
 - <b>`y`</b> (int):  y coordinate of the top left corner 
 - <b>`w`</b> (int):  width of the crop 
 - <b>`h`</b> (int):  height of the crop 
 - <b>`frame`</b>:  np.ndarray:  width:  height:  



**Returns:**
 cropped image 


---

<a href="../cv_aid/utils.py#L381"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `blur`

```python
blur(frame: ndarray, ksize=(5, 5)) → ndarray
```

Blurs an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to blur 
 - <b>`ksize`</b> (tuple, optional):  size of the kernel (Default value = (5) 
 - <b>`frame`</b>:  np.ndarray:  5):  



**Returns:**
 blurred image 


---

<a href="../cv_aid/utils.py#L397"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `flip`

```python
flip(frame: ndarray, flip_code=1) → ndarray
```

Flips an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to flip 
 - <b>`flip_code`</b> (int, optional):  code for flipping the image (Default value = 1) 
 - <b>`frame`</b>:  np.ndarray:  



**Returns:**
 flipped image 


---

<a href="../cv_aid/utils.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `line`

```python
line(
    frame: ndarray,
    start: tuple,
    end: tuple,
    color=(0, 255, 0),
    thickness=2,
    line_type=8
) → ndarray
```

Draws a line on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the line on 
 - <b>`start`</b> (tuple):  start point of the line 
 - <b>`end`</b> (tuple):  end point of the line 
 - <b>`color`</b> (tuple, optional):  color of the line (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  thickness of the line (Default value = 2) 
 - <b>`line_type`</b> (int, optional):  type of the line (Default value = cv2.LINE_8) 
 - <b>`frame`</b>:  np.ndarray:  
 - <b>`start`</b>:  tuple:  
 - <b>`end`</b>:  tuple:  255:  0):  



**Returns:**
 image with the line 


---

<a href="../cv_aid/utils.py#L442"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `lines`

```python
lines(frame, points: list, **kwargs)
```

Draws multiple lines on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the lines on 
 - <b>`points`</b> (list):  list of points to draw lines between 
 - <b>`kwargs`</b> (dict):  keyword arguments for line 
 - <b>`points`</b>:  list:  **kwargs:  



**Returns:**
 image with the lines 


---

<a href="../cv_aid/utils.py#L461"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `box`

```python
box(
    frame: ndarray,
    x,
    y,
    width,
    height,
    color=(0, 255, 0),
    thickness=1,
    line_type=8,
    is_max=False
) → ndarray
```

Draws a box on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the box on 
 - <b>`x`</b> (int):  x coordinate of the top left corner 
 - <b>`y`</b> (int):  y coordinate of the top left corner 
 - <b>`w`</b> (int):  width of the box 
 - <b>`h`</b> (int):  height of the box 
 - <b>`color`</b> (tuple, optional):  color of the box (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  thickness of the box (Default value = 1) 
 - <b>`line_type`</b> (int, optional):  type of the box (Default value = cv2.LINE_8) 
 - <b>`max`</b> (bool):  if True, treat the box as a max box 
 - <b>`frame`</b>:  np.ndarray:  width:  height:  255:  0):  
 - <b>`is_max`</b>:   (Default value = False) 
 - <b>`# pylint`</b>:  disable:  (Default value = redefined-outer-name) 



**Returns:**
 image with the box 


---

<a href="../cv_aid/utils.py#L507"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `boxes`

```python
boxes(frame, cords, **kwargs)
```

Draws multiple boxes on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the boxes on 
 - <b>`cords`</b> (list):  list of coordinates of the boxes 
 - <b>`kwargs`</b> (dict):  keyword arguments for box **kwargs:  



**Returns:**
 image with the boxes 


---

<a href="../cv_aid/utils.py#L525"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `canny`

```python
canny(frame: ndarray, threshold1=100, threshold2=200) → ndarray
```

Applies Canny edge detection to an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to apply Canny edge detection to 
 - <b>`threshold1`</b> (int, optional):  first threshold for Canny edge detection (Default value = 100) 
 - <b>`threshold2`</b> (int, optional):  second threshold for Canny edge detection (Default value = 200) 
 - <b>`frame`</b>:  np.ndarray:  



**Returns:**
 image with the Canny edge detection applied 


---

<a href="../cv_aid/utils.py#L541"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `text`

```python
text(
    frame: ndarray,
    text_: str,
    x: int,
    y: int,
    font=0,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2
) → ndarray
```

Draws text on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the text on 
 - <b>`text_`</b> (str):  text to draw 
 - <b>`x`</b> (int):  x coordinate of the top left corner 
 - <b>`y`</b> (int):  y coordinate of the top left corner 
 - <b>`font`</b> (int, optional):  font to use for the text (Default value = cv2.FONT_HERSHEY_SIMPLEX) 
 - <b>`scale`</b> (float, optional):  scale of the text (Default value = 0.5) 
 - <b>`color`</b> (tuple, optional):  color of the text (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  thickness of the text (Default value = 2) 
 - <b>`frame`</b>:  np.ndarray:  
 - <b>`text_`</b>:  str:  
 - <b>`x`</b>:  int:  
 - <b>`y`</b>:  int:  255:  0):  



**Returns:**
 image with the text 


---

<a href="../cv_aid/utils.py#L576"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `text_above_box`

```python
text_above_box(
    frame: ndarray,
    text_: str,
    cords: tuple,
    font=0,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2
) → ndarray
```

Draws text above a box on an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to draw the text on 
 - <b>`text_`</b> (str):  text to draw 
 - <b>`cords`</b> (tuple):  coordinates of the box 
 - <b>`font`</b> (int, optional):  font to use for the text (Default value = cv2.FONT_HERSHEY_SIMPLEX) 
 - <b>`scale`</b> (float, optional):  scale of the text (Default value = 0.5) 
 - <b>`color`</b> (tuple, optional):  color of the text (Default value = (0) 
 - <b>`thickness`</b> (int, optional):  thickness of the text (Default value = 2) 
 - <b>`frame`</b>:  np.ndarray:  
 - <b>`text_`</b>:  str:  
 - <b>`cords`</b>:  tuple:  255:  0):  



**Returns:**
 image with the text 


---

<a href="../cv_aid/utils.py#L617"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search`

```python
search(frame, template, method=5, threshold=0.8)
```

Searches for a template in an image. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  image to search for the template in 
 - <b>`template`</b> (np.ndarray):  template to search for 
 - <b>`method`</b> (int, optional):  method to use for template matching (Default value = cv2.TM_CCOEFF_NORMED) 
 - <b>`threshold`</b> (float, optional):  threshold for template matching (Default value = 0.8) 



**Returns:**
 coordinates of the template in the image 


---

<a href="../cv_aid/utils.py#L637"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `stack`

```python
stack(frames: list, resize_=None, cols=2) → ndarray
```

Stacks frames into a single image. 



**Args:**
 
 - <b>`frames`</b> (list):  frames to stack 
 - <b>`resize_`</b> (tuple, optional):  resize the frames (Default value = None) 
 - <b>`cols`</b> (int, optional):  number of columns in the stacked image (Default value = 2) 
 - <b>`frames`</b>:  list:  



**Returns:**
 stacked frames 


---

<a href="../cv_aid/utils.py#L691"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_bytes`

```python
to_bytes(frame: ndarray) → bytes
```

Converts a frame to bytes. 



**Args:**
 
 - <b>`frame`</b> (np.ndarray):  frame to convert 
 - <b>`frame`</b>:  np.ndarray:  



**Returns:**
 bytes 


---

<a href="../cv_aid/utils.py#L705"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_frame`

```python
to_frame(bytes_: bytes) → ndarray
```

Converts bytes to a frame. 



**Args:**
 
 - <b>`bytes_`</b> (bytes_: bytes):  bytes to convert 
 - <b>`bytes_`</b>:  bytes:  



**Returns:**
 frame 


---

<a href="../cv_aid/utils.py#L719"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_base64`

```python
to_base64(bytes_: bytes) → str
```

Converts bytes to a base64 string. 



**Args:**
 
 - <b>`bytes_`</b> (bytes_: bytes):  bytes to convert 
 - <b>`bytes_`</b>:  bytes:  



**Returns:**
 base64 string 


---

<a href="../cv_aid/utils.py#L733"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `from_base64`

```python
from_base64(base64_: str) → ndarray
```

Converts a base64 string to bytes. 



**Args:**
 
 - <b>`base64_`</b> (str):  base64 string to convert 
 - <b>`base64_`</b>:  str:  



**Returns:**
 np.ndarray frame 


---

<a href="../cv_aid/utils.py#L279"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TemplateResponse`
TemplateResponse class. 

<a href="../cv_aid/utils.py#L282"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(frame, loc, template)
```

Initializes the TemplateResponse class. 

:param frame: frame to apply the template to :type frame: np.ndarray :param loc: location of the template :type loc: tuple :param template: template to apply :type template: np.ndarray 




---

<a href="../cv_aid/utils.py#L320"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `boxes`

```python
boxes(color=(0, 255, 0)) → Generator
```

Returns the boxes of the template. 



**Args:**
 
 - <b>`color`</b> (tuple, optional):  color of the boxes (Default value = (0) 255:  0):  



**Returns:**
 generator of boxes 

---

<a href="../cv_aid/utils.py#L300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `draw_boxes`

```python
draw_boxes() → TemplateResponse
```

Draws the boxes on the frame. 

:return: The resulting TemplateResponse object 



**Args:**
 



**Returns:**
 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
