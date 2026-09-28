from picamera2 import Picamera2
from datetime import datetime
import os

# Folder paths
GOOD_FOLDER = "Training images/Good box"
DAMAGED_FOLDER = "Training Images/Damaged box"

# Create folders if they don't exist
os.makedirs(GOOD_FOLDER, exist_ok=True)
os.makedirs(DAMAGED_FOLDER, exist_ok=True)

# Camera setup
picam2 = Picamera2()

config = picam2.create_still_configuration(
    main={"size": (4608, 2592)}
)

picam2.configure(config)
picam2.start()

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

print("Done!")
