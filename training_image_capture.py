from picamera2 import Picamera2, Preview
from datetime import datetime
import os
import time

# Folder paths
GOOD_FOLDER = "Training images/Good box"
DAMAGED_FOLDER = "Training images/Damaged box"

os.makedirs(GOOD_FOLDER, exist_ok=True)
os.makedirs(DAMAGED_FOLDER, exist_ok=True)

# Camera setup
picam2 = Picamera2()

config = picam2.create_still_configuration(
    main={"size": (4608, 2592)}
)

picam2.configure(config)

# LIVE PREVIEW WINDOW
picam2.start_preview(Preview.QTGL)

picam2.start()

# Let camera settle
time.sleep(2)

print("\n=== CARTON DATASET CAPTURE ===")
print("g = Good Box")
print("d = Damaged Box")
print("q = Quit\n")

while True:

    choice = input("Capture Good (g) / Damaged (d) / Quit (q): ").lower()

    if choice == "q":
        break

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "g":
        filename = os.path.join(
            GOOD_FOLDER,
            f"good_{timestamp}.jpg"
        )

    elif choice == "d":
        filename = os.path.join(
            DAMAGED_FOLDER,
            f"damaged_{timestamp}.jpg"
        )

    else:
        print("Invalid choice")
        continue

    picam2.capture_file(filename)
    print(f"Saved: {filename}")

picam2.stop_preview()
print("Done!")
