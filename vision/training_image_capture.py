from picamera2 import Picamera2
from datetime import datetime
import cv2
import os
import time

# Folder paths
GOOD_FOLDER = "Training images/Good box"
DAMAGED_FOLDER = "Training images/Damaged box"

os.makedirs(GOOD_FOLDER, exist_ok=True)
os.makedirs(DAMAGED_FOLDER, exist_ok=True)

# Camera setup
picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(
    main={"size": (1280, 720)}
)

picam2.configure(preview_config)
picam2.start()

time.sleep(2)

print("\n=== CARTON DATASET CAPTURE ===")
print("Press G = Good Box")
print("Press D = Damaged Box")
print("Press Q = Quit\n")

while True:

    frame = picam2.capture_array()

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    cv2.putText(
        frame,
        "G = Good | D = Damaged | Q = Quit",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Carton Dataset Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if key == ord("g"):

        filename = os.path.join(
            GOOD_FOLDER,
            f"good_{timestamp}.jpg"
        )

        picam2.capture_file(filename)

        print(f"Saved GOOD: {filename}")

    elif key == ord("d"):

        filename = os.path.join(
            DAMAGED_FOLDER,
            f"damaged_{timestamp}.jpg"
        )

        picam2.capture_file(filename)

        print(f"Saved DAMAGED: {filename}")

    elif key == ord("q"):
        break

cv2.destroyAllWindows()
picam2.stop()

print("Done!")
