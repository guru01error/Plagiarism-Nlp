# Real-Time Human Activity Recognition (HAR) System

An end-to-end Computer Vision and Machine Learning pipeline that classifies human physical activities in real-time using webcam video feeds. Built with **MediaPipe Pose**, **Scikit-Learn**, and **OpenCV**, featuring a modern dark-themed SaaS dashboard overlay.

---

## Key Features

* **3D Pose Estimation:** Extracts 33 key 3D spatial landmarks (99 feature coordinates) via MediaPipe Pose.
* **ML-Powered Classification:** High-accuracy real-time activity predictions using Random Forest classification.
* **Temporal Smoothing:** Majority voting mechanism via `collections.deque` to eliminate prediction flickering.
* **Modern HUD Dashboard:** Sleek, high-contrast dashboard displaying live confidence scores, dynamic progress bars, FPS metrics, and system stats.
* **Robust Hardware Management:** Automatic camera fallback, error handling, and memory cleanup.

---

## Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV, MediaPipe
* **Machine Learning:** Scikit-Learn, Joblib, NumPy
* **GUI & Rendering:** Pillow (PIL), Canvas Overlay

---

## System Architecture

```text
Webcam Feed ──> MediaPipe Pose ──> 3D Landmarks Extractor (99 Features)
                                                │
                                                ▼
UI Dashboard <── Temporal Smoothing <── Random Forest Model
(OpenCV + PIL)   (Majority Voting)