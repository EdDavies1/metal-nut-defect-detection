# Metal Nut Defect Detection

Defect detection on metal parts with PyTorch, testing whether synthetic Blender data helps when real defect images are scarce.

> Work in progress. This README is updated as each stage is completed.

## Data

This project uses the `metal_nut` category of the [MVTec Anomaly Detection dataset (MVTec AD)](https://www.mvtec.com/company/research/datasets/mvtec-ad). The images are not included in this repository. Download `metal_nut` from the MVTec website and extract it to `data/metal_nut/`.

### Image counts

Output of `python explore.py`:

| Folder | Images |
| --- | ---: |
| train/good | 220 |
| test/bent | 25 |
| test/color | 22 |
| test/flip | 23 |
| test/good | 22 |
| test/scratch | 23 |
| **Total defects** | **93** |

### What this means

- **Only 93 defect images exist**, about 23 per defect type. MVTec's training folder contains defect-free images only, so every defect image used for training has to come from the test folder. Train, validation and test splits will be made from these 93 images.
- **The training set will be very small.** Holding back about 20% for testing leaves around 74 images for training and validation, or roughly 15 per defect type.
- **This is why synthetic data is worth testing.** With so few real examples, a model is likely to overfit. Stage 3 measures whether rendered images of synthetic defects close that gap.

## Project stages

- [ ] Stage 0: Setup and data exploration (in progress)
- [ ] Stage 1: Classification, good or defective
- [ ] Stage 2: Detection with Faster R-CNN
- [ ] Stage 3: Synthetic data from Blender
- [ ] Stage 4: Results and write-up

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1    macOS/Linux: source .venv/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple
pip install numpy pillow matplotlib
python explore.py
```

## Licence and citation

The MVTec AD dataset is released under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence and is used here for non-commercial purposes only.

> Paul Bergmann, Kilian Batzner, Michael Fauser, David Sattlegger, Carsten Steger: The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection; in: International Journal of Computer Vision 129(4):1038-1059, 2021, DOI: 10.1007/s11263-020-01400-4.

> Paul Bergmann, Michael Fauser, David Sattlegger, Carsten Steger: MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection; in: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9584-9592, 2019, DOI: 10.1109/CVPR.2019.00982.
