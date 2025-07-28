def check_dependencies():
    try:
        import PyQt6  # noqa: E402, F401
        import psutil  # noqa: E402, F401
    except ImportError as e:
        print("\033[31mSome of required modules not installed or unavailable in default python3 interpreter !\031[0m\n")
        raise e
