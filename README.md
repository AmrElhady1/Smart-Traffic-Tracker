# Smart Traffic Tracker

A real-time computer vision pipeline for traffic analysis and vehicle counting. Built to simulate edge AI workloads, this system detects vehicles, maintains persistent object tracking across frames, and logs counts using a virtual tripwire.

## Demo
<img width="1904" height="969" alt="Screenshot 2026-09-04 013642" src="https://github.com/user-attachments/assets/81f1dd57-4689-430b-b1a9-349ac59193a8" />

<table>
  <tr>
    <th>Raw Input</th>
    <th>Processed Output (Tracking & Counting)</th>
  </tr>
  <tr>
    <td width="50%">
      <video src="https://github.com/user-attachments/assets/89379685-99e4-4cb9-9398-496d828e0a7f" width="100%" controls autoplay muted loop></video>
    </td>
    <td width="50%">
      <video src="https://github.com/user-attachments/assets/c0566b75-e9f5-4242-bc73-0bdf8ece95f1" width="100%" controls autoplay muted loop></video>
    </td>
  </tr>
</table>

## Features
* **Real-time Object Detection:** Uses YOLOv8 Nano for high-speed, lightweight inference.
* **Persistent Tracking:** Implements ByteTrack to assign and maintain unique IDs for vehicles, handling occlusion and overlapping bounding boxes.
* **Flow Analytics:** Virtual tripwire logic tracks crossing events to provide accurate vehicle counts.
* **Web UI:** Includes a containerized Gradio interface for easy video testing and visualization.

## Tech Stack
* **Language:** Python 3.10
* **Computer Vision:** OpenCV, Ultralytics (YOLOv8)
* **Frontend:** Gradio
* **Deployment:** Docker

## Local Setup

1. Clone the repository:
```bash

git clone https://github.com/AmrElhady1/traffic-analyzer.git
cd traffic-analyzer

```
                     







