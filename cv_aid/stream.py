from threading import Thread
from cv_aid import Frame
import cv2


class VideoStream:
    """
    A class for streaming video from a camera.

    :param src: The source of the video stream.

    Example:
    >>> from cv_aid import VideoStream
    >>> stream = VideoStream(src=0).start()
    >>> while True:
    >>>     frame = stream.read()
    >>>     cv2.imshow("Frame", frame.frame)
    >>>     if cv2.waitKey(1) & 0xFF == ord('q'):
    >>>         break
    >>> stream.stop()
    """

    def __init__(self, src):
        """
        Initialize the video stream and read the first frame from the stream.

        :param src: The source of the video stream.
        """
        self.src = src
        self.stopped = False
        self.paused = False
        self.stream = cv2.VideoCapture(src)
        self.frame = self.read()
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True

    def read(self):
        return Frame(self.stream.read())

    def start(self):
        """
        Start the video stream.
        """
        self.thread.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            if self.paused:
                continue
            self.frame = self.read()

    def pause(self):
        """
        Pause the video stream.
        """
        self.paused = True

    def resume(self):
        """
        Resume the video stream.
        """
        self.paused = False

    def stop(self):
        """
        Stop the video stream.
        """
        self.stopped = True
        self.stream.release()
        self.thread.join()
        return self

    def __del__(self):
        self.stream.release()
        self.thread.join()
