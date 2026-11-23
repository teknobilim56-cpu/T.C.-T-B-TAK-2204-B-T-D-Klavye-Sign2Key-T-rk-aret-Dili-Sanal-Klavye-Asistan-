import sys
import os
import platform

def get_platform():
    return sys.platform if sys.platform != "win32" else "windows"

def is_windows():
    return sys.platform == "win32"

def is_linux():
    return sys.platform.startswith("linux")

def fix_locale():
    os.environ["LC_ALL"] = "C"
    if is_windows():
        os.environ["PYTHONIOENCODING"] = "utf-8"
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception:
            pass

def get_model_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def get_camera_backend():
    import cv2
    if is_windows():
        return cv2.CAP_DSHOW
    return cv2.CAP_ANY

def get_app_data_dir():
    if is_windows():
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
        path = os.path.join(base, "Sign2Key")
    else:
        path = os.path.join(os.path.expanduser("~"), ".sign2key")
    os.makedirs(path, exist_ok=True)
    return path
