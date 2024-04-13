#traffic digital Twin
Developed a system capable of detecting the driver’s eyes and mouth to determine the driver’s sobriety status.

## Blueprint
![](./demo/blueprint.png)

![](./demo/1.mp4)

## Run
1. Download yolov3.weight
2. Run `infer_reid_vehicle.py`.
```
python infer_reid_vehicle.py --dets dets/taiwan 
```
3. Run `Run.py`
```
python Run.py
```
