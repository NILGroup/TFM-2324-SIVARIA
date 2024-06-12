import sys
from controller import Controller

def main():
    controller = Controller()
    output = controller.execute(sys.argv)
    print(output)

if __name__ == "__main__":
    sys.exit(main())
