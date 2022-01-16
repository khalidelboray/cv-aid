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

:param path: path to the directory to search in :type path: Path :return: generator of all images in the directory 


---

<a href="../cv_aid/utils.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_videos`

```python
find_videos(path: Path) → Generator
```

Finds all videos in a directory. 

:param path: path to the directory to search in :type path: Path :return: generator of all videos in the directory 


---

<a href="../cv_aid/utils.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_fonts`

```python
find_fonts(path: Path) → Generator
```

Finds all fonts in a directory. 

:param path: path to the directory to search in :type path: Path :return: generator of all fonts in the directory 


---

<a href="../cv_aid/utils.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rotate`

```python
rotate(img: ndarray, angle, center=None, scale=1.0, same_dim=True) → ndarray
```

Rotates an image. 

:param img: image to rotate :type img: np.ndarray :param angle: angle to rotate the image by :type angle: int :param center: center of the image to rotate around :type center: tuple :param scale: scale of the image :type scale: float :param same_dim: if True, the image will be resized to the same dimensions as the original :type same_dim: bool :return: rotated image 


---

<a href="../cv_aid/utils.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `resize`

```python
resize(img: ndarray, width, height, inter=3) → ndarray
```

Resizes an image. 

:param img: image to resize :type img: np.ndarray :param width: width of the resized image :type width: int :param height: height of the resized image :type height: int :param inter: interpolation method :type inter: int :return: resized image 


---

<a href="../cv_aid/utils.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `concatenate`

```python
concatenate(image1: ndarray, image2: ndarray, axis=1) → ndarray
```

Concatenates two images. 

:param image1: first image to concatenate :type image1: np.ndarray :param image2: second image to concatenate :type image2: np.ndarray :param axis: axis to concatenate the images on :type axis: int :return: concatenated image 


---

<a href="../cv_aid/utils.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `batch`

```python
batch(iterable: Iterable, length: int) → Generator
```

Batches an iterable. 

:param iterable: iterable to batch :type iterable: Iterable :param n: number of items to batch :type n: int :return: generator of batches 


---

<a href="../cv_aid/utils.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_type`

```python
is_type(obj, type_name)
```

Checks if an object is of a certain type. 

:param obj: object to check :type obj: object :param type_name: name of the type to check :type type_name: str :return: True if the object is of the type, False otherwise 


---

<a href="../cv_aid/utils.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `verify_frame_type`

```python
verify_frame_type(func)
```

Verifies that the frame type is correct. 

:param func: function to decorate :type func: function :return: decorated function 


---

<a href="../cv_aid/utils.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `copy_frame`

```python
copy_frame(func)
```

Copies the frame before applying the function. 

:param func: function to decorate :type func: function :return: decorated function 


---

<a href="../cv_aid/utils.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `verify_deepstack_config`

```python
verify_deepstack_config(func)
```

Verifies that the DeepStack config is correct. 

:param func: function to decorate :type func: function :return: decorated function 


---

<a href="../cv_aid/utils.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gray`

```python
gray(frame: ndarray) → ndarray
```

Converts a color image to grayscale. 

:param frame: image to convert to grayscale :type frame: np.ndarray :return: grayscale image 


---

<a href="../cv_aid/utils.py#L304"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `crop`

```python
crop(frame: ndarray, x, y, width, height) → ndarray
```

Crops an image. 

:param frame: image to crop :type frame: np.ndarray :param x: x coordinate of the top left corner :type x: int :param y: y coordinate of the top left corner :type y: int :param w: width of the crop :type w: int :param h: height of the crop :type h: int :return: cropped image 


---

<a href="../cv_aid/utils.py#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `blur`

```python
blur(frame: ndarray, ksize=(5, 5)) → ndarray
```

Blurs an image. 

:param frame: image to blur :type frame: np.ndarray :param ksize: size of the kernel :type ksize: tuple :return: blurred image 


---

<a href="../cv_aid/utils.py#L336"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `flip`

```python
flip(frame: ndarray, flip_code=1) → ndarray
```

Flips an image. 

:param frame: image to flip :type frame: np.ndarray :param flip_code: code for flipping the image :type flip_code: int :return: flipped image 


---

<a href="../cv_aid/utils.py#L349"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

:param frame: image to draw the line on :type frame: np.ndarray :param start: start point of the line :type start: tuple :param end: end point of the line :type end: tuple :param color: color of the line :type color: tuple :param thickness: thickness of the line :type thickness: int :param line_type: type of the line :type line_type: int :return: image with the line 


---

<a href="../cv_aid/utils.py#L377"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `lines`

```python
lines(frame, points: list, **kwargs)
```

Draws multiple lines on an image. 

:param frame: image to draw the lines on :type frame: np.ndarray :param points: list of points to draw lines between :type points: list :param kwargs: keyword arguments for line :type kwargs: dict :return: image with the lines 


---

<a href="../cv_aid/utils.py#L394"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

:param frame: image to draw the box on :type frame: np.ndarray :param x: x coordinate of the top left corner :type x: int :param y: y coordinate of the top left corner :type y: int :param w: width of the box :type w: int :param h: height of the box :type h: int :param color: color of the box :type color: tuple :param thickness: thickness of the box :type thickness: int :param line_type: type of the box :type line_type: int :param max: if True, treat the box as a max box :type max: bool :return: image with the box 


---

<a href="../cv_aid/utils.py#L439"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `boxes`

```python
boxes(frame, cords, **kwargs)
```

Draws multiple boxes on an image. 

:param frame: image to draw the boxes on :type frame: np.ndarray :param cords: list of coordinates of the boxes :type cords: list :param kwargs: keyword arguments for box :type kwargs: dict :return: image with the boxes 


---

<a href="../cv_aid/utils.py#L456"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `canny`

```python
canny(frame: ndarray, threshold1=100, threshold2=200) → ndarray
```

Applies Canny edge detection to an image. 

:param frame: image to apply Canny edge detection to :type frame: np.ndarray :param threshold1: first threshold for Canny edge detection :type threshold1: int :param threshold2: second threshold for Canny edge detection :type threshold2: int :return: image with the Canny edge detection applied 


---

<a href="../cv_aid/utils.py#L471"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

:param frame: image to draw the text on :type frame: np.ndarray :param text_: text to draw :type text_: str :param x: x coordinate of the top left corner :type x: int :param y: y coordinate of the top left corner :type y: int :param font: font to use for the text :type font: int :param scale: scale of the text :type scale: float :param color: color of the text :type color: tuple :param thickness: thickness of the text :type thickness: int :return: image with the text 


---

<a href="../cv_aid/utils.py#L505"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

:param frame: image to draw the text on :type frame: np.ndarray :param text_: text to draw :type text_: str :param cords: coordinates of the box :type cords: tuple :param font: font to use for the text :type font: int :param scale: scale of the text :type scale: float :param color: color of the text :type color: tuple :param thickness: thickness of the text :type thickness: int :return: image with the text 


---

<a href="../cv_aid/utils.py#L545"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search`

```python
search(frame, template, method=5, threshold=0.8)
```

Searches for a template in an image. 

:param frame: image to search for the template in :type frame: np.ndarray :param template: template to search for :type template: np.ndarray :param method: method to use for template matching :type method: int :param threshold: threshold for template matching :type threshold: float :return: coordinates of the template in the image 


---

<a href="../cv_aid/utils.py#L566"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `stack`

```python
stack(frames: list, resize_=None, cols=2) → ndarray
```

Stacks frames into a single image. 

:param frames: frames to stack :type frames: list :param resize_: resize the frames :type resize_: tuple :param cols: number of columns in the stacked image :type cols: int :return: stacked frames 


---

<a href="../cv_aid/utils.py#L619"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_bytes`

```python
to_bytes(frame: ndarray) → bytes
```

Converts a frame to bytes. 

:param frame: frame to convert :type frame: np.ndarray :return: bytes 


---

<a href="../cv_aid/utils.py#L630"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_frame`

```python
to_frame(bytes_: bytes) → ndarray
```

Converts bytes to a frame. 

:param bytes_: bytes to convert :type bytes_: bytes :return: frame 


---

<a href="../cv_aid/utils.py#L641"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_base64`

```python
to_base64(bytes_: bytes) → str
```

Converts bytes to a base64 string. 

:param bytes_: bytes to convert :type bytes_: bytes :return: base64 string 


---

<a href="../cv_aid/utils.py#L652"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `from_base64`

```python
from_base64(base64_: str) → ndarray
```

Converts a base64 string to bytes. 

:param base64_: base64 string to convert :type base64_: str :return: np.ndarray frame 


---

<a href="../cv_aid/utils.py#L231"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TemplateResponse`
TemplateResponse class. 

<a href="../cv_aid/utils.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(frame, loc, template)
```

Initializes the TemplateResponse class. 

:param frame: frame to apply the template to :type frame: np.ndarray :param loc: location of the template :type loc: tuple :param template: template to apply :type template: np.ndarray 




---

<a href="../cv_aid/utils.py#L270"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `boxes`

```python
boxes(color=(0, 255, 0)) → Generator
```

Returns the boxes of the template. 

:param color: color of the boxes :type color: tuple :return: generator of boxes 

---

<a href="../cv_aid/utils.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `draw_boxes`

```python
draw_boxes() → TemplateResponse
```

Draws the boxes on the frame. 

:return: The resulting TemplateResponse object 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
