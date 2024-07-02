from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="SAM",
    version="0.1",
    description="My personal antimalware system",
    executables=[Executable("main.py", base=base)],
    includes=["config.py", "mod_filecheck.py", "mod_urlcheck.py"],
    build_options={
        "packages":["tkinter"],
        "include_files": ["encrypted_api_key.txt", "key.key"]
    }
)