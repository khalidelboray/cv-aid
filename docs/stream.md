<!-- markdownlint-disable -->

<a href="../cv_aid/stream.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `stream`






---

<a href="../cv_aid/stream.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `VideoStream`
A class for streaming video from a camera. 

:param src: The source of the video stream. 

<a href="../cv_aid/stream.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(src, width=None, height=None, on_frame=None)
```

Initialize the video stream and read the first frame from the stream. 

:param src: The source of the video stream. :param width: The width of the frame. :type width: int :param height: The height of the frame. :type height: int 




---

<a href="../cv_aid/stream.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `close_windows`

```python
close_windows()
```





---

<a href="../cv_aid/stream.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../cv_aid/stream.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → Frame
```

Read a frame from the video stream and return it. 

---

<a href="../cv_aid/stream.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `resume`

```python
resume()
```

Resume the video stream. 

---

<a href="../cv_aid/stream.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start`

```python
start()
```

Start the video stream. 

---

<a href="../cv_aid/stream.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start_window`

```python
start_window(title=None)
```

Start a window to display the video stream. 

:param title: The title of the window. :type title: str 

---

<a href="../cv_aid/stream.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```

Stop the video stream. 

---

<a href="../cv_aid/stream.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
