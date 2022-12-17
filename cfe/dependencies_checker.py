def check_dependencies():
    try:
        import PyQt5
        import psutil
    except ImportError as e:
        print("\033[31mSome of required modules not installed or unavailable in default python3 interpreter !\031[0m\n")
        raise e
