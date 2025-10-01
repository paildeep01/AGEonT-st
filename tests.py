"""
Test Suite for AGEonT-st System
Tests basic functionality without requiring all dependencies
"""
import sys
import os


def test_project_structure():
    """Test that all required files exist"""
    print("\n" + "="*60)
    print("TEST: Project Structure")
    print("="*60)
    
    required_files = [
        'app.py',
        'config.py',
        'requirements.txt',
        'setup.py',
        'README.md',
        'QUICKSTART.md',
        'LICENSE',
        '.gitignore',
        '.env.example',
        'utils/__init__.py',
        'utils/article_fetcher.py',
        'utils/translator.py',
        'utils/analyzer.py',
        'utils/summarizer.py',
        '.streamlit/config.toml'
    ]
    
    all_exist = True
    for file_path in required_files:
        exists = os.path.exists(file_path)
        status = "✓" if exists else "✗"
        print(f"{status} {file_path}")
        if not exists:
            all_exist = False
    
    if all_exist:
        print("\n✅ All required files present")
        return True
    else:
        print("\n❌ Some files are missing")
        return False


def test_python_syntax():
    """Test that all Python files have valid syntax"""
    print("\n" + "="*60)
    print("TEST: Python Syntax Validation")
    print("="*60)
    
    python_files = [
        'app.py',
        'config.py',
        'setup.py',
        'examples.py',
        'demo.py',
        'utils/__init__.py',
        'utils/article_fetcher.py',
        'utils/translator.py',
        'utils/analyzer.py',
        'utils/summarizer.py'
    ]
    
    all_valid = True
    for file_path in python_files:
        try:
            with open(file_path, 'r') as f:
                code = f.read()
                compile(code, file_path, 'exec')
            print(f"✓ {file_path} - Valid syntax")
        except SyntaxError as e:
            print(f"✗ {file_path} - Syntax error: {e}")
            all_valid = False
        except Exception as e:
            print(f"✗ {file_path} - Error: {e}")
            all_valid = False
    
    if all_valid:
        print("\n✅ All Python files have valid syntax")
        return True
    else:
        print("\n❌ Some Python files have syntax errors")
        return False


def test_module_structure():
    """Test that modules have correct structure"""
    print("\n" + "="*60)
    print("TEST: Module Structure")
    print("="*60)
    
    tests = [
        ("config.py contains APP_TITLE", "APP_TITLE" in open('config.py').read()),
        ("config.py contains SUPPORTED_LANGUAGES", "SUPPORTED_LANGUAGES" in open('config.py').read()),
        ("article_fetcher.py contains ArticleFetcher class", "class ArticleFetcher" in open('utils/article_fetcher.py').read()),
        ("translator.py contains Translator class", "class Translator" in open('utils/translator.py').read()),
        ("analyzer.py contains ContentAnalyzer class", "class ContentAnalyzer" in open('utils/analyzer.py').read()),
        ("summarizer.py contains TextSummarizer class", "class TextSummarizer" in open('utils/summarizer.py').read()),
        ("app.py contains main function", "def main" in open('app.py').read()),
        ("app.py contains Streamlit imports", "import streamlit" in open('app.py').read()),
    ]
    
    all_passed = True
    for test_name, result in tests:
        status = "✓" if result else "✗"
        print(f"{status} {test_name}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n✅ Module structure is correct")
        return True
    else:
        print("\n❌ Some module structure issues found")
        return False


def test_documentation():
    """Test that documentation exists and is comprehensive"""
    print("\n" + "="*60)
    print("TEST: Documentation")
    print("="*60)
    
    # Check README
    readme_content = open('README.md').read()
    readme_tests = [
        ("README has title", "# AGEonT-st" in readme_content),
        ("README has Features section", "## Features" in readme_content),
        ("README has Installation section", "## Installation" in readme_content),
        ("README has Usage section", "## Usage" in readme_content),
        ("README mentions Streamlit", "streamlit" in readme_content.lower()),
    ]
    
    # Check QUICKSTART
    quickstart_content = open('QUICKSTART.md').read()
    quickstart_tests = [
        ("QUICKSTART has installation", "Installation" in quickstart_content),
        ("QUICKSTART has usage examples", "Usage" in quickstart_content),
        ("QUICKSTART has examples", "Example" in quickstart_content),
    ]
    
    all_tests = readme_tests + quickstart_tests
    all_passed = True
    
    for test_name, result in all_tests:
        status = "✓" if result else "✗"
        print(f"{status} {test_name}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n✅ Documentation is comprehensive")
        return True
    else:
        print("\n❌ Documentation needs improvement")
        return False


def test_requirements():
    """Test that requirements.txt contains necessary packages"""
    print("\n" + "="*60)
    print("TEST: Requirements")
    print("="*60)
    
    requirements_content = open('requirements.txt').read()
    required_packages = [
        'streamlit',
        'requests',
        'beautifulsoup4',
        'newspaper3k',
        'transformers',
        'torch',
        'googletrans',
        'textblob',
        'nltk',
        'pandas',
        'plotly',
        'python-dotenv'
    ]
    
    all_present = True
    for package in required_packages:
        present = package in requirements_content
        status = "✓" if present else "✗"
        print(f"{status} {package}")
        if not present:
            all_present = False
    
    if all_present:
        print("\n✅ All required packages listed")
        return True
    else:
        print("\n❌ Some packages missing from requirements")
        return False


def test_gitignore():
    """Test that .gitignore is properly configured"""
    print("\n" + "="*60)
    print("TEST: Git Configuration")
    print("="*60)
    
    gitignore_content = open('.gitignore').read()
    important_ignores = [
        '__pycache__',
        '*.pyc',
        'venv',
        '.env',
        '.DS_Store'
    ]
    
    all_present = True
    for pattern in important_ignores:
        present = pattern in gitignore_content
        status = "✓" if present else "✗"
        print(f"{status} {pattern} ignored")
        if not present:
            all_present = False
    
    if all_present:
        print("\n✅ .gitignore properly configured")
        return True
    else:
        print("\n❌ .gitignore needs improvement")
        return False


def test_config_files():
    """Test configuration files"""
    print("\n" + "="*60)
    print("TEST: Configuration Files")
    print("="*60)
    
    tests = [
        (".env.example exists", os.path.exists('.env.example')),
        (".streamlit/config.toml exists", os.path.exists('.streamlit/config.toml')),
        ("LICENSE exists", os.path.exists('LICENSE')),
        ("LICENSE is MIT", "MIT License" in open('LICENSE').read()),
    ]
    
    all_passed = True
    for test_name, result in tests:
        status = "✓" if result else "✗"
        print(f"{status} {test_name}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n✅ Configuration files are correct")
        return True
    else:
        print("\n❌ Configuration files need attention")
        return False


def run_all_tests():
    """Run all tests and report results"""
    print("\n" + "="*60)
    print("AGEonT-st System Test Suite")
    print("="*60)
    
    tests = [
        test_project_structure,
        test_python_syntax,
        test_module_structure,
        test_documentation,
        test_requirements,
        test_gitignore,
        test_config_files
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append((test_func.__name__, result))
        except Exception as e:
            print(f"\n❌ Test {test_func.__name__} failed with error: {e}")
            results.append((test_func.__name__, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("\n" + "="*60)
    print(f"Results: {passed}/{total} tests passed")
    print("="*60)
    
    if passed == total:
        print("\n🎉 All tests passed! System is ready.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review.")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
