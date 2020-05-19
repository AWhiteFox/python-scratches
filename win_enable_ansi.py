def win_enable_ansi():
    """
    Enables ANSI escape sequences support in Windows console
    """
    from ctypes import windll, wintypes, byref
    handle = windll.kernel32.GetStdHandle(-11)  # -11 for STDOUT
    mode = wintypes.DWORD()
    windll.kernel32.GetConsoleMode(handle, byref(mode))
    windll.kernel32.SetConsoleMode(handle, mode.value | 0x0004)
