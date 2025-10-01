#!/usr/bin/env python3
"""
Installation and Setup Script for AGEonT-st
"""
import subprocess
import sys


def install_dependencies():
    """Install required Python packages"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def download_nltk_data():
    """Download required NLTK data"""
    print("\nDownloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")
        return False


def verify_installation():
    """Verify all modules can be imported"""
    print("\nVerifying installation...")
    
    modules = [
        'streamlit',
        'requests',
        'bs4',
        'newspaper',
        'googletrans',
        'textblob',
        'nltk',
        'pandas',
        'plotly'
    ]
    
    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            all_ok = False
    
    return all_ok


def main():
    """Main setup function"""
    print("=" * 60)
    print("AGEonT-st Setup Script")
    print("=" * 60)
    
    if not install_dependencies():
        print("\n❌ Setup failed at dependency installation")
        return 1
    
    if not download_nltk_data():
        print("\n⚠️  NLTK data download failed, but continuing...")
    
    if not verify_installation():
        print("\n❌ Some modules failed to import")
        return 1
    
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("=" * 60)
    print("\nTo run the application:")
    print("  streamlit run app.py")
    print("\nThe application will open in your browser at http://localhost:8501")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
