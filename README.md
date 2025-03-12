# Speed detection

This project detects motion in a live video feed and calculates the speed of a moving object using OpenCV and NumPy. The speed is estimated based on the time taken for an object to pass through the camera frame.

### Install Dependencies

```
pip install opencv-python numpy
```

### Clone the Repository
```
git clone https://github.com/your-username/speed_detection.git 
cd speed_detection
```
### Run the Script
```
python speed_detection.py 
```
Press 'q' to quit the program.

### How It Works

* The camera captures live video frames. 
* The first frame is stored as a reference background. 
* Each new frame is compared to the reference frame to detect motion. 
* When an object enters the frame, start time is recorded. 
* When the object leaves the frame, end time is recorded. 
* Using the time difference and a predefined distance, the speed is calculated. 

