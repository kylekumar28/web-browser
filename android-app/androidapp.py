from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from jnius import autoclass

class AndroidWebView(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_webview()

    def create_webview(self):
        # Get required Java classes
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')

        # Create a WebView instance
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)  # Enable JavaScript
        webview.getSettings().setDomStorageEnabled(True)  # Enable DOM storage
        webview.setWebViewClient(WebViewClient())  # Set WebView client
        webview.loadUrl('https://www.kylekumar.com/kaps')  # Load the URL

        # Add the WebView to the Android layout
        layout = activity.getWindow().getDecorView().findViewById(16908290)
        layout.addView(webview)

class MinimalBrowserApp(App):
    def build(self):
        return AndroidWebView()

if __name__ == "__main__":
    MinimalBrowserApp().run()