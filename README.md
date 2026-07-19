# Packing Line Optimization using Computer Vision Detection Models

## Project Overview

This project focuses on optimizing a packing line using computer vision and artificial intelligence. The system uses YOLOv8 and OpenCV to detect and count products in real time.

The project also includes a monitoring dashboard that displays important packing line information such as product count, defect count, and system efficiency.

## Technologies Used

* Python
* YOLOv8
* OpenCV
* Streamlit
* Computer Vision
* JSON
* ThingSpeak / IoT

## Key Features

* Real-time product detection
* Product counting
* Computer vision-based monitoring
* Packing line performance monitoring
* Efficiency calculation
* Streamlit dashboard
* IoT data monitoring

## Project Files

* `counter.py` – Detects and counts products using computer vision.
* `dashboard.py` – Displays packing line data through a Streamlit dashboard.
* `main.py` – Main project execution file.
* `yolotest.py` – YOLO object detection testing file.
* `data.json` – Stores project data and detection results.
* `ThingSpeak test.py` – Tests IoT data communication with ThingSpeak.

## How to Run

Install the required Python libraries:

```bash
pip install ultralytics opencv-python streamlit
```

Run the detection program:

```bash
python counter.py
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

## Applications

This project can be used in:

* Smart manufacturing
* Industrial automation
* Quality monitoring
* Packing line optimization
* Industry 4.0 applications

## Future Enhancements

* Custom-trained defect detection model
* Automatic defect classification
* Cloud-based monitoring
* IoT sensor integration
* Real-time alerts and notifications

## Author

Nivethika
