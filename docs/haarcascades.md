<!-- markdownlint-disable -->

<a href="../cv_aid/haarcascades.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `haarcascades`






---

<a href="../cv_aid/haarcascades.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Haarcascades`
Class for loading and using haarcascades. 

<a href="../cv_aid/haarcascades.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initializes Haarcascades. 




---

<a href="../cv_aid/haarcascades.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_all`

```python
detect_all(image: ndarray, **kwargs)
```

Detects all objects in an image. 

:param image: image to detect objects in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing objects 

---

<a href="../cv_aid/haarcascades.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_eyes`

```python
detect_eyes(image: ndarray, **kwargs)
```

Detects eyes in an image. 

:param image: image to detect eyes in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing eyes 

---

<a href="../cv_aid/haarcascades.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_faces`

```python
detect_faces(image: ndarray, **kwargs)
```

Detects faces in an image. 

:param image: image to detect faces in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing faces 

---

<a href="../cv_aid/haarcascades.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_fullbody`

```python
detect_fullbody(image: ndarray, **kwargs)
```

Detects full body in an image. 

:param image: image to detect full body in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing full body 

---

<a href="../cv_aid/haarcascades.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_lowerbody`

```python
detect_lowerbody(image: ndarray, **kwargs)
```

Detects lower body in an image. 

:param image: image to detect lower body in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing lower body 

---

<a href="../cv_aid/haarcascades.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_profileface`

```python
detect_profileface(image: ndarray, **kwargs)
```

Detects profile face in an image. 

:param image: image to detect profile face in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing profile face 

---

<a href="../cv_aid/haarcascades.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_smiles`

```python
detect_smiles(image: ndarray, **kwargs)
```

Detects smiles in an image. 

:param image: image to detect smiles in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing smiles 

---

<a href="../cv_aid/haarcascades.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `detect_upperbody`

```python
detect_upperbody(image: ndarray, **kwargs)
```

Detects upper body in an image. 

:param image: image to detect upper body in :param kwargs: kwargs for detectMultiScale :return: list of rectangles containing upper body 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
