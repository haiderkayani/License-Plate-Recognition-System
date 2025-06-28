# License Plate Recognition System

This project is a Python-based License Plate Recognition System developed using **OpenCV**, **EasyOCR**, and **NumPy**. It detects and extracts the license plate from an image using image processing techniques, then uses Optical Character Recognition (OCR) to read and display the license plate text.

---

## Authors

- **Laiba Shafqat**
- **Haider Ali Kayani**

---

## Course

**Digital Image Processing – Semester Project**

---

## Concepts & Libraries Used

- **OpenCV**: Image processing and contour detection  
- **EasyOCR**: Text recognition from images  
- **NumPy**: Numerical operations  
- **Matplotlib**: Image display and visualization  
- **Imutils**: Convenient functions for image processing  

---

## Project Workflow

1. **Read the input image**
2. **Convert to grayscale**
3. **Apply bilateral filtering and Canny edge detection**
4. **Find contours and identify the number plate area**
5. **Mask and crop the number plate**
6. **Use OCR to extract the license plate text**
7. **Display the result with highlighted number plate and extracted text**

---

## 🗂️ Directory Structure

license-plate-recognition/
├── images/
│ └── 11.jpg # Sample image file
├── main.py # Main Python script for detection
├── README.md # Project documentation
