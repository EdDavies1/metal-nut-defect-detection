from pathlib import Path

# Folder this script lives in, so the path works on any machine
PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data" / "metal_nut"


def count_images(folder):
    """Return how many .png files are in a folder."""
    return len(list(folder.glob("*.png")))


def print_counts():
    print(f"{'folder':<15}{'images':>7}")
    print(f"{'train/good':<15}{count_images(DATA_DIR / 'train' / 'good'):>7}")

    total_defects = 0
    for defect_dir in sorted((DATA_DIR / "test").iterdir()):
        if not defect_dir.is_dir():
            continue
        n = count_images(defect_dir)
        print(f"{'test/' + defect_dir.name:<15}{n:>7}")
        if defect_dir.name != "good":
            total_defects += n

    print(f"{'total defects':<15}{total_defects:>7}")


if __name__ == "__main__":
    print_counts()