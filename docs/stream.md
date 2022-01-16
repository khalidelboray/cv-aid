<!-- markdownlint-disable -->

<a href="../cv_aid/stream.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `stream`






---

<a href="../cv_aid/stream.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `VideoStream`
A class for streaming video from a camera. 



**Args:**
 
 - <b>`src`</b>:  The source of the video stream. 



**Returns:**
 

<a href="../cv_aid/stream.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(src, width=None, height=None, on_frame=None)
```

Initialize the video stream and read the first frame from the stream. 

:param src: The source of the video stream. :param width: The width of the frame. :type width: int :param height: The height of the frame. :type height: int 




---

<a href="../cv_aid/stream.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `close_windows`

```python
close_windows()
```





---

<a href="../cv_aid/stream.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `kill`

```python
kill()
```

Kill the video stream. 

---

<a href="../cv_aid/stream.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pause`

```python
pause()
```

Pause the video stream. 

---

<a href="../cv_aid/stream.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → Frame
```

Read a frame from the video stream and return it. 

---

<a href="../cv_aid/stream.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `resume`

```python
resume()
```

Resume the video stream. 

---

<a href="../cv_aid/stream.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start`

```python
start()
```

Start the video stream. 

---

<a href="../cv_aid/stream.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start_window`

```python
start_window(title=None)
```

Start a window to display the video stream. 



**Args:**
 
 - <b>`title`</b> (str, optional):  The title of the window. (Default value = None) 



**Returns:**
 

---

<a href="../cv_aid/stream.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```

Stop the video stream. 

---

<a href="../cv_aid/stream.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
