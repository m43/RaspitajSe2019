import cv2
from time import sleep, time
import re

class FPSmeter(object):
    def __init__(self, font=cv2.FONT_HERSHEY_SIMPLEX, pos_x=None, pos_y=None, font_scale=0.5, font_color=(255, 0, 0)):
        self.font = font
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.time = time()
        self.scale = font_scale
        self.color = font_color
        self.fps = None
        self.font = font
        return

    def tick(self, img):
        width, height, _ = img.shape
        now = time()
        delta = now - self.time
        self.time = now

        self.fps = 1 // delta
        if self.pos_x is None or self.pos_y is None:
            cv2.putText(img, "FPS: " + str(int(self.fps)), (height - 76, 14), self.font,
                        self.scale, self.color, 1)
        else:
            raise NotImplementedError("fps position not implemented yet")


def webcam_stream(stream_source=0, width=1280, height=720, image_handle=None, flip=True, wait_key=True,
                  force_resize=False, grayscale=False, show_fps=True, pause_key=True):
    from warnings import warn

    def dummy_image_show(img):
        cv2.imshow("dummy image function", img)

    if image_handle is None:
        image_handle = dummy_image_show

    capture = cv2.VideoCapture(stream_source)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    warned = False
    expected_shape = (height, width, 3)

    fps = None
    if show_fps:
        fps = FPSmeter()

    while True:
        return_code, bgr_image = capture.read()

        if bgr_image is None:
            break

        if bgr_image.shape != expected_shape:

            if not warned:
                warn("image{} not of expected shape{}{}".format(bgr_image.shape, expected_shape,
                                                                ", resizing!" if force_resize else ""))
                warned = True

            if force_resize:
                bgr_image = cv2.resize(bgr_image, (expected_shape[0:2]))

        if flip:
            bgr_image = cv2.flip(bgr_image, 1)

        if show_fps:
            fps.tick(bgr_image)

        if grayscale:
            bgr_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

        image_handle(bgr_image)

        key = chr(cv2.waitKey(1) & 0xFF)

        if pause_key and key == 'p':
            while True:
                sleep(0.3)
                key = chr(cv2.waitKey(1) & 0xFF)
                if key == 'p':
                    break

        if wait_key and key == 'q':
            print("done")
            break

    cv2.destroyAllWindows()
    
    print("[stream end]")


def tracking_algorithms():
    # returns dictionary with methods that initialize trackers

    # dict[TrackerName] -> (TrackerConstructor, TrackerCreateMethod)

    r = re.compile("Tracker.*_create")
    available = filter(r.match, dir(cv2))
    tracker_names = list(available)

    # print(tracker_names)

    tracker_create_methods = [getattr(cv2, tracker) for tracker in tracker_names]
    tracker_names = [name[0:-7] for name in tracker_names]
    tracker_constructors = [getattr(cv2, tracker) for tracker in tracker_names]

    # check if really a tracking algorithm
    instance_check = [isinstance(method(), cv2.Tracker) for method in tracker_create_methods]

    if False in instance_check:
        raise RuntimeError("Unable to list OpenCV implemented tracking algorithms")

    # pack values into dictionary
    result_dict = dict()
    for i, name in enumerate(tracker_names):
        result_dict[name] = (tracker_constructors[i], tracker_create_methods[i])

    return result_dict

if __name__ == '__main__':
    webcam_stream(stream_source=0,
                  width=320,
                  height=240,
                  flip=True,
                  wait_key=True,
                  force_resize=False,
                  grayscale=False,
                  show_fps=True)