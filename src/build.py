"""Build script to create executables for PDF Splitter"""

import os
import sys
import subprocess
import platform
import zipfile


def build_executable():
    """Build the executable using PyInstaller"""
    
    print("Building PDF Splitter executable...")
    print(f"Platform: {platform.system()}")
    
    # PyInstaller command
    pyinstaller_path = os.path.join(os.path.dirname(sys.executable), 'pyinstaller')
    cmd = [
        pyinstaller_path,
        "--name=PDF-Splitter",
        "--noconsole",  # No console window
        "--onefile",   # Single executable file
        "--icon=./assets/icon.png",
        "src/pdf_splitter.py"
    ]
    
    # Run PyInstaller
    try:
        subprocess.run(cmd, check=True)
        print("\n" + "="*50)
        print("Build completed successfully!")
        print("="*50)
        
        if platform.system() == "Windows":
            print("\nExecutable location: dist/PDF-Splitter.exe")
        elif platform.system() == "Darwin":
            print("\nExecutable location: dist/PDF-Splitter")
        else:
            print("\nExecutable location: dist/PDF-Splitter")
            
        print("\nYou can now distribute the executable from the 'dist' folder.")

        # Package the built executable into a platform-labelled zip under `versions/`
        try:
            cwd = os.getcwd()
            dist_dir = os.path.join(cwd, 'dist')

            if platform.system() == 'Windows':
                exe_name = 'PDF-Splitter.exe'
            else:
                exe_name = 'PDF-Splitter'

            exe_path = os.path.join(dist_dir, exe_name)

            if os.path.exists(exe_path):
                versions_dir = os.path.join(cwd, 'versions')
                os.makedirs(versions_dir, exist_ok=True)

                plat = platform.system().lower()
                arch = platform.machine().lower() or 'unknown'
                zip_filename = f"PDF-Splitter-{plat}-{arch}.zip"
                zip_path = os.path.join(versions_dir, zip_filename)

                with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                    zf.write(exe_path, arcname=os.path.basename(exe_path))

                print(f"\nPackaged installer: {zip_path}")
            else:
                print(f"\nExecutable not found at {exe_path}; skipping packaging.")
        except Exception as e:
            print(f"\nWarning: failed to package executable: {e}")
        
    except subprocess.CalledProcessError as e:
        print(f"\nError during build: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_executable()
