<!-- markdownlint-disable -->

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `haarcascades`






---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Haarcascades`
Class for loading and using haarcascades. 

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initializes Haarcascades. 




---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_all`

```python
detect_all(image: ndarray, **kwargs)
```

Detects all objects in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect objects in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing objects 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_eyes`

```python
detect_eyes(image: ndarray, **kwargs)
```

Detects eyes in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect eyes in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing eyes 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_fullbody`

```python
detect_fullbody(image: ndarray, **kwargs)
```

Detects full body in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect full body in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing full body 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_lowerbody`

```python
detect_lowerbody(image: ndarray, **kwargs)
```

Detects lower body in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect lower body in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing lower body 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_profileface`

```python
detect_profileface(image: ndarray, **kwargs)
```

Detects profile face in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect profile face in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing profile face 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_smiles`

```python
detect_smiles(image: ndarray, **kwargs)
```

Detects smiles in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect smiles in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing smiles 

---

<a href="https://github.com/khalidelboray/cv-aid/blob/main/cv_aid/haarcascades.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_upperbody`

```python
detect_upperbody(image: ndarray, **kwargs)
```

Detects upper body in an image. 



**Args:**
 
 - <b>`image`</b>:  image to detect upper body in 
 - <b>`kwargs`</b>:  kwargs for detectMultiScale 
 - <b>`image`</b>:  np.ndarray: **kwargs: 



**Returns:**
 list of rectangles containing upper body 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
