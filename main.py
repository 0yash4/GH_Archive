import sys


def main():
    print(sys.executable)
    print(sys.version)
    print(sys.platform)
    print(sys.path)
    print(sys.argv)
    print(sys.modules)
    print(sys.getdefaultencoding())


if __name__ == "__main__":
    main()
