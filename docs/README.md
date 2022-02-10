<!-- markdownlint-disable -->

# API Overview

## Modules

- [`frame`](./frame.md#module-frame)
- [`haarcascades`](./haarcascades.md#module-haarcascades)
- [`dlib`](./dlib.md#module-dlib)
- [`stream`](./stream.md#module-stream)
- [`utils`](./utils.md#module-utils)

## Classes

- [`frame.Frame`](./frame.md#class-frame): A class to represent a frame of video.
- [`haarcascades.Haarcascades`](./haarcascades.md#class-haarcascades): Class for loading and using haarcascades.
- [`dlib.Dlib`](./dlib.md#class-Dlib): Provides a class for loading and using dlib models. 
- [`stream.VideoStream`](./stream.md#class-videostream): A class for streaming video from a camera.
- [`utils.TemplateResponse`](./utils.md#class-templateresponse): TemplateResponse class.

## Functions

- [`utils.batch`](./utils.md#function-batch): Batches an iterable.
- [`utils.blur`](./utils.md#function-blur): Blurs an image.
- [`utils.bordered_box`](./utils.md#function-bordered_box): Draws a box on an image with a border.
- [`utils.bordered_circle`](./utils.md#function-bordered_circle): Draws a circle on an image with a border.
- [`utils.box`](./utils.md#function-box): Draws a box on an image.
- [`utils.boxes`](./utils.md#function-boxes): Draws multiple boxes on an image.
- [`utils.canny`](./utils.md#function-canny): Applies Canny edge detection to an image.
- [`utils.circle`](./utils.md#function-circle): Draws a circle on an image.
- [`utils.concatenate`](./utils.md#function-concatenate): Concatenates two images.
- [`utils.copy_frame`](./utils.md#function-copy_frame): Copies the frame before applying the function.
- [`utils.cornerBox`](./utils.md#function-cornerbox): Draws a box with corners.
- [`utils.crop`](./utils.md#function-crop): Crops an image.
- [`utils.disk`](./utils.md#function-disk): Generate coordinates of pixels within circle.
- [`utils.dropshade`](./utils.md#function-dropshade): Shades a box.
- [`utils.find_fonts`](./utils.md#function-find_fonts): Finds all fonts in a directory.
- [`utils.find_images`](./utils.md#function-find_images): Finds all images in a directory.
- [`utils.find_videos`](./utils.md#function-find_videos): Finds all videos in a directory.
- [`utils.flip`](./utils.md#function-flip): Flips an image.
- [`utils.from_base64`](./utils.md#function-from_base64): Converts a base64 string to bytes.
- [`utils.gray`](./utils.md#function-gray): Converts a color image to grayscale.
- [`utils.is_type`](./utils.md#function-is_type): Checks if an object is of a certain type.
- [`utils.line`](./utils.md#function-line): Draws a line on an image.
- [`utils.lines`](./utils.md#function-lines): Draws multiple lines on an image.
- [`utils.resize`](./utils.md#function-resize): Resizes an image.
- [`utils.rotate`](./utils.md#function-rotate): Rotates an image.
- [`utils.search`](./utils.md#function-search): Searches for a template in an image.
- [`utils.set_color`](./utils.md#function-set_color): Set pixel color in the image at the given coordinates.
- [`utils.stack`](./utils.md#function-stack): Stacks frames into a single image.
- [`utils.text`](./utils.md#function-text): Draws text on an image.
- [`utils.text_above_box`](./utils.md#function-text_above_box): Draws text above a box on an image.
- [`utils.to_base64`](./utils.md#function-to_base64): Converts bytes to a base64 string.
- [`utils.to_bytes`](./utils.md#function-to_bytes): Converts a frame to bytes.
- [`utils.to_frame`](./utils.md#function-to_frame): Converts bytes to a frame.
- [`utils.verify_deepstack_config`](./utils.md#function-verify_deepstack_config): Verifies that the DeepStack config is correct.
- [`utils.verify_frame_type`](./utils.md#function-verify_frame_type): Verifies that the frame type is correct.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
