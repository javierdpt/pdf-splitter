"""Small helper to package the built executable into `versions/` without re-running PyInstaller.

Usage: run with the project's venv Python so paths resolve the same way as builds.
"""
import os
import platform
import zipfile

cwd = os.getcwd()
dist_dir = os.path.join(cwd, 'dist')

if platform.system() == 'Windows':
    exe_name = 'PDF-Splitter.exe'
else:
    exe_name = 'PDF-Splitter'

exe_path = os.path.join(dist_dir, exe_name)

if not os.path.exists(exe_path):
    print(f"Executable not found at {exe_path}; nothing to package.")
    raise SystemExit(1)

versions_dir = os.path.join(cwd, 'versions')
os.makedirs(versions_dir, exist_ok=True)

plat = platform.system().lower()
arch = platform.machine().lower() or 'unknown'
zip_filename = f"PDF-Splitter-{plat}-{arch}.zip"
zip_path = os.path.join(versions_dir, zip_filename)

with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(exe_path, arcname=os.path.basename(exe_path))

print(f"Packaged installer created: {zip_path}")
