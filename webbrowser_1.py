from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
import sys


class MinimalBrowser(QMainWindow):
    def __init__(self, url):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Minimal Browser")
        self.setGeometry(100, 100, 1024, 768)  # Default window size

        # Create a QWebEngineView to display the website
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        # Disable all safety procedures and enable all features
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.XSSAuditingEnabled, False)
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
        settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        settings.setAttribute(QWebEngineSettings.ShowScrollBars, True)

        # Create a layout and add the browser to it
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        # Create a central widget for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Launch in fullscreen mode
        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the browser
    browser = MinimalBrowser("https://www.kylekumar.com/kaps")
    browser.show()

    sys.exit(app.exec_())
