<!-- markdownlint-disable -->

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `_dlib`






---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Dlib`
Provides a class for loading and using dlib models. 

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(landmark_predictor_path='shape_predictor_68_face_landmarks.dat')
```

Initializes Dlib. 

:param face_shape_path: path to face shape predictor :type face_shape_path: str 




---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `convert_and_trim_bb`

```python
convert_and_trim_bb(image, rectangle)
```

Converts a bounding box to a normal box with respect to the image. 



**Args:**
 
 - <b>`image`</b>:  image to convert and trim 
 - <b>`rect`</b>:  bounding box to convert and trim rectangle: 



**Returns:**
 trimmed image 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_faces`

```python
detect_faces(image: ndarray, **kwargs)
```

Detects faces in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect faces in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing faces 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_landmarks`

```python
detect_landmarks(image: ndarray, rectangle: tuple, **kwargs)
```

Detects landmarks in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect landmarks in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: 
 - <b>`rectangle`</b>:  tuple: **kwargs: 



**Returns:**
 list of rectangles containing landmarks 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `download_and_extract`

```python
download_and_extract(url, path='./')
```

Downloads and extracts shape predictor. 



**Args:**
 
 - <b>`url`</b>:  url to download file from 
 - <b>`path`</b>:  path to extract file to (Default value = "./") 



**Returns:**
 path to downloaded file 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `download_face_recognition_model_v1`

```python
download_face_recognition_model_v1(path='./')
```

Downloads face recognition model v1. 



**Args:**
 
 - <b>`path`</b> (str, optional):  path to download to (Default value = "./") 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `download_landmark_detector`

```python
download_landmark_detector(path='./')
```

Downloads landmark detector. 



**Args:**
 
 - <b>`path`</b> (str, optional):  path to download to (Default value = "./") 



**Returns:**
 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/_dlib.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `download_shape_predictor`

```python
download_shape_predictor(path='./')
```

Downloads shape predictor. 



**Args:**
 
 - <b>`path`</b> (str, optional):  path to download to (Default value = "./") 



**Returns:**
 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
