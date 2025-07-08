import pywhatkit
import time
import datetime

def send_whatsapp_message(phone, message, delay_min=1):
    # Get current time
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + delay_min

    # Adjust for overflow
    if minute >= 60:
        hour += 1
        minute = minute % 60

    print(f"Scheduling message to {phone} at {hour}:{minute}")
    pywhatkit.sendwhatmsg(phone, message, hour, minute)
    time.sleep(10)  # Wait for WhatsApp Web to open and send

# -----------------------------
# ✨ MAIN LOGIC
# -----------------------------
print("=== WhatsApp Automation Tool ===")

contacts = []
while True:
    number = input("Enter WhatsApp number (with country code): ")
    contacts.append(number)
    more = input("Add another number? (y/n): ").lower()
    if more != 'y':
        break

message = input("Enter the message to send: ")
choice = input("Send instantly? (y/n): ").lower()

for phone in contacts:
    if choice == 'y':
        print(f"Sending instantly to {phone}")
        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)
    else:
        send_whatsapp_message(phone, message)

print("✅ Messages scheduled/sent successfully.")
