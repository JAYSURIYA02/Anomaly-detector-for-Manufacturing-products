from pathlib import Path
from PIL import Image

DATASET_PATH = Path("Dataset")

categories = [
    "bottle",
    "cable",
    "capsule",
    "carpet",
    "grid",
    "hazelnut",
    "leather",
    "metal_nut",
    "pill",
    "screw",
    "tile",
    "toothbrush",
    "transistor",
    "wood",
    "zipper"
]

for category in categories:

    category_path = DATASET_PATH / category

    train_path = category_path / "train"
    test_path = category_path / "test"

    print(f"\n========== {category} ==========")

    # Training images
    train_images = list(train_path.rglob("*.png"))

    # Test images
    test_images = list(test_path.rglob("*.png"))

    print("Training images :", len(train_images))
    print("Test images     :", len(test_images))

    # Inspect first image
    if train_images:
        image_path = train_images[0]

        with Image.open(image_path) as img:
            print("Example image   :", image_path.name)
            print("Image size      :", img.size)
            print("Image mode      :", img.mode)