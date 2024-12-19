import time
import argparse
from pynput.mouse import Controller

def jiggle_mouse(interval, duration):
    mouse = Controller()
    start_time = time.time()
    print("Starting mouse jiggler...")

    while time.time() - start_time < duration:
        current_position = mouse.position
        mouse.move(3, 0)  # Move mouse slightly to the right
        time.sleep(0.1)
        mouse.position = current_position  # Move it back to the original position
        time.sleep(interval)

    print("Mouse jiggling stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI tool to jiggle the mouse and prevent idle.")
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=5,
        help="Interval in seconds between jiggles (default: 5s)"
    )
    parser.add_argument(
        "-d", "--duration",
        type=float,
        default=60,
        help="Total duration in seconds to jiggle the mouse (default: 60s)"
    )
    args = parser.parse_args()

    jiggle_mouse(args.interval, args.duration)