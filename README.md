# Image manipulator script
The script is responsible for image manipulation. It can:

- resize images to thumbnail
- change images name
- convert images to jpg format
- change the path of images
- change the contrast of images
- change the brightness of images
- crop images to specific size
- add a logo to images
- add a text to images

All option can be taken based on provided argument

## Usage
To show all availability option use following command:
```buildoutcfg
python main.py --help
```

## Example

```buildoutcfg
python main.py --jpg --brightness 0.5 --crop 800 800 --logo logo.png --quotes quotes.csv --name landscape
```
Before:

![landscape-4387209_1280](https://user-images.githubusercontent.com/32844693/64979720-9496be80-d8b8-11e9-83d8-3892da34ce3f.jpg)

![way-4459666_1280](https://user-images.githubusercontent.com/32844693/64979721-9496be80-d8b8-11e9-9f49-3de841b5167d.jpg)

After:

![landscape-1](https://user-images.githubusercontent.com/32844693/64979693-80eb5800-d8b8-11e9-9268-d87392a09a03.jpg)

![landscape-2](https://user-images.githubusercontent.com/32844693/64979694-80eb5800-d8b8-11e9-9d19-f41fa282abba.jpg)
## Technologies

- Python 3.7.0
- Pillow 6.0.0