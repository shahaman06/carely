# to confirm booking and set booking request
from .Utility.util import invalid_user, print_records, verify_user
import mysql.connector

print("\n*****************Booking Page****************\n")
per_id = input("Enter Personal Carely Id to set appointment: ").lower()
if per_id[:2] not in ["el", "ct"]:
    invalid_user()
else:
    conn = mysql.connector.connect(
        host="localhost",
        user="carely_admin",
        passwd="carely_admin",
        database="carelydb",
    )
    cur = conn.cursor()
    i = ["el", "ct"].index(per[:2])
    if i:
        print_records("Elderly")
        book_id = input("\nEnter Carely id of Oldie you want to take care of: ").lower()
    else:
        print_records("Carely")
        book_id = input(
            "\nEnter Carely id of Youngster, you want to be take care by: "
        ).lower()
    if not (
        verify_user(per_id, "per_id", "id") | verify_user(book_id, "Elderly", "id")
    ):
        invalid_user()
    pb = PendingBooking()
    val = (per_id, book_id) + pb.fill_info()
    sqlcmd = "insert into PendingBooking values (%s,%s,%s,%s)"
    cur.execute(sqlcmd, val)
    conn.commit()
print("\n\nThanks for Booking Appointment.")
print("\nWait for futher response from the Other Side.")
print("Thank You")
