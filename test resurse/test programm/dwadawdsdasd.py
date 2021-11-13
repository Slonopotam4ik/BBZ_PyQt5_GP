import sys
from PyQt5.QtCore import QTimeLine, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)
        self.w = self.size().width()

        self.timeline = QTimeLine(6000 * 2, self)
        self.timeline.setFrameRange(0, self.w + 100)

        self.timeline.frameChanged.connect(self.set_frame_func)
        self.timeline.setLoopCount(0)
        self.timeline.start()

        self.frame_geometry = None  # !!!

    def set_frame_func(self, frame):

        if self.frame_geometry != self.frameGeometry():  # !!!
            self.frame_geometry = self.frameGeometry()
            print(f' set_frame_func: -> {self.frame_geometry}')

    def resizeEvent(self, event):
        super(Demo, self).resizeEvent(event)
        self.w = self.size().width()
        self.timeline.setFrameRange(0, self.w + 100)
        duration = self.w * 20
        self.timeline.setDuration(duration)

        self.frame_geometry = self.frameGeometry()  # !!!
        print(f'+++ releaseEvent -> {self.frame_geometry}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())