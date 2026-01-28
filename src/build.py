"""Build script to create executables for PDF Splitter"""

import os
import sys
import subprocess
import platform


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
        
    except subprocess.CalledProcessError as e:
        print(f"\nError during build: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_executable()
