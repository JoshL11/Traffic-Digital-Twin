#traffic digital Twin
Developed a system capable of detecting the driver’s eyes and mouth to determine the driver’s sobriety status.

## Demo
![](./demo/blueprint/png)

## Requirements
```
pip install numpy opencv-python Pillow ultralytics
```

## Run
1. Install **[IP WebCam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US)** on your phone and open it.
2. Change the `ip_webcam_url` in `yolo_camera.py` to your ip in the bottom of WebCam app.
3. Run `yolo_camera.py`.
```
python yolo_camera.py
```
4. Run `gui_coloered_and_paid.py`
```
python gui_coloered_and_paid.py
```
