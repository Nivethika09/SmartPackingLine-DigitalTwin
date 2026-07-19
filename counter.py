from ultralytics import YOLO
import cv2
import json

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    phone_count = 0
    defect_count = 0

    # Count detected objects
    for box in results[0].boxes:

        cls = int(box.cls[0])
        name = model.names[cls]
        confidence = float(box.conf[0])

        print("Detected:", name)

        # Count every detected object
        phone_count += 1

        # Low confidence = defect
        if confidence < 0.60:
            defect_count += 1

    # Save data for dashboard
    data = {
        "phone_count": phone_count,
        "defect_count": defect_count
    }

    with open("data.json", "w") as f:
        json.dump(data, f)

    # Draw YOLO detections
    annotated_frame = results[0].plot()

    # Show counts on screen
    cv2.putText(
        annotated_frame,
        f"Product Count: {phone_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Defect Count: {defect_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("Packing Line Counter", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()