from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys

class MinimalBrowser(QMainWindow):
    def __init__(self, url):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("KAPS")
        self.setGeometry(100, 100, 1400, 720)  # Default window size

        # Create a QWebEngineView to display the website
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        # Disable all safety procedures and enable all features
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.JavascriptEnabled, True)
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.PluginsEnabled, True)
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.JavascriptCanOpenWindows, True)
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.JavascriptCanAccessClipboard, True)
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.LocalStorageEnabled, True)
        self.browser.settings().setAttribute(self.browser.settings().WebAttribute.AllowRunningInsecureContent, True)

        # Create a layout and add the browser to it
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        # Create a central widget for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Launch in fullscreen mode
        # self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the browser
    browser = MinimalBrowser("https://www.kylekumar.com/kaps")
    browser.show()

    sys.exit(app.exec())
