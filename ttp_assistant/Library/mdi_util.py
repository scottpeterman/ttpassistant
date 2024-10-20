from PyQt6.QtWidgets import QMdiSubWindow, QMenu, QMainWindow, QWidget
from PyQt6.QtGui import QAction


class CustomMdiSubWindow(QMdiSubWindow):
    def contextMenuEvent(self, event):
        # Check if the right-click is on the title bar
        if self.isMaximized() or event.pos().y() <= self.systemMenu().height():
            context_menu = QMenu(self)
            open_in_new_window_action = QAction("Open in New Window", self)
            open_in_new_window_action.triggered.connect(self.open_in_new_window)
            context_menu.addAction(open_in_new_window_action)
            context_menu.exec(event.globalPos())

    def open_in_new_window(self):
        try:

            # Get the widget inside this QMdiSubWindow
            widget = self.widget()

            # Reparent the widget to None
            widget.setParent(None)

            # Create a new standalone window and set the widget as the central widget
            standalone_window = QMainWindow()
            stub_widget = QWidget()
            standalone_window.setCentralWidget(stub_widget)

            # Set some properties for the standalone window
            standalone_window.setWindowTitle("Standalone Terminal")
            standalone_window.setGeometry(100, 100, 800, 600)
            main_win = self.mdiArea().parent()  # Get the MDIMainWindow instance
            main_win.standalone_windows.append(standalone_window)
            # Close the current QMdiSubWindow
            standalone_window.show()
            standalone_window.setCentralWidget(widget)
            standalone_window.update()
            self.close()

            # Show the standalone window
            standalone_window.show()

        except Exception as e:
            print(e)

