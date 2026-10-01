# Main application entry point
# Main application entry point

from session.session_manager import (
    update_barcode,
    update_damage,
    ready,
    get_session,
    reset
)

print("Warehouse Vision POC Started")

while True:

    print("\nChoose an action:")
    print("1 = Scan Barcode")
    print("2 = Detect Damage")
    print("3 = Exit")

    choice = input("> ")

    if choice == "1":

        barcode = input("Enter barcode: ")

        update_barcode(barcode)

        print("Barcode stored.")

    elif choice == "2":

        damage_image = input("Enter damage image name: ")

        update_damage(damage_image)

        print("Damage stored.")

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid option.")
        continue

    if ready():

        print("\nCOMPLETE RECORD FOUND")

        print(get_session())

        print("\nUploading to GCP...")
        print("(placeholder only)")

        reset()

        print("Session reset.")
