from tkinter import messagebox, filedialog, Tk, Text, Scrollbar, Label, Button
import winsound
import smtplib
# import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math

main = Tk()
main.title("Accident Detection")
main.geometry("1300x1200")


def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def uploadVideo():
    global filename
    filename = filedialog.askopenfilename(initialdir="videos", title="Select Video File",
                                          filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])

    if not filename:
        messagebox.showerror("Error", "Please select a valid video file.")
        return

    pathlabel.config(text=filename)
    text.delete('1.0', 'end')
    text.insert('end', filename + " loaded\n")


def sendEmail(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("testingautomation243@gmail.com", "yencnlayfhhpskri")
    recipients = ["alapatimanikanta0836@gmail.com", "manialapti15@gmail.com"]
    server.sendmail("22891a0567@gmail.com", recipients, message)
    server.quit()


def exit():
    main.destroy()


def webcam():
    global filename
    filename = ""
    detector()


def detector():
    img_path = filename

    if img_path != "":
        cap = cv2.VideoCapture(img_path)  # for video
    else:
        cap = cv2.VideoCapture(0)  # for webcam
        cap.set(3, 1280)
        cap.set(4, 720)

    model = YOLO("best.pt")

    classNames = ["fire_accident", "vehicle_accident"]

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to read frame. Exiting...")
            break

        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1

                # Additional check for valid dimensions
                if w > 0 and h > 0:
                    cvzone.cornerRect(img, (x1, y1, w, h))

                    # confidence
                    conf = math.ceil((box.conf[0] * 100)) / 100

                    # class name
                    cls = int(box.cls[0])
                    cvzone.putTextRect(img, f'{classNames[cls]}:{conf}', (max(0, x1), max(35, y1)), scale=0.6,
                                       thickness=1, offset=3)

                    # Check for accidents and update alert_message
                    if classNames[cls] in ["fire_accident", "vehicle_accident"]:
                        alert_message = f"Accident detected: {classNames[cls]}, Confidence: {conf}"

                        # If an accident is detected, send alert message
                        if alert_message:
                            print(alert_message)
                            sendEmail(alert_message)
                            beep()  # Optional: Beep to alert locally

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()


font = ('times', 16, 'bold')
title = Label(main, text='Accident Detection')
title.config(bg='light cyan', fg='pale violet red')
title.config(font=font)
title.config(height=3, width=120)
title.place(x=0, y=5)

pathlabel = Label(main)
pathlabel.config(bg='light cyan', fg='pale violet red')
pathlabel.config(font=('Arial', 12, 'bold'))
pathlabel.place(x=460, y=100)

webcamButton = Button(main, text="Browse System Videos", command=uploadVideo)
webcamButton.place(x=50, y=150)
webcamButton.config(font=('Arial', 12, 'bold'))

webcamButton = Button(main, text="Webcam", command=webcam)
webcamButton.place(x=50, y=200)
webcamButton.config(font=('Arial', 12, 'bold'))

webcamButton = Button(main, text="Start Accident Detector", command=detector)
webcamButton.place(x=50, y=250)
webcamButton.config(font=('Arial', 12, 'bold'))

exitButton = Button(main, text="Exit", command=exit)
exitButton.place(x=330, y=300)
exitButton.config(font=('Arial', 12, 'bold'))

text = Text(main, height=10)

main.mainloop()
