import os

def scan_large_files(directory, size_limit_mb=1):
    size_limit_bytes = size_limit_mb * 1024 * 1024
    print(f"Scanning '{directory}' for files larger than {size_limit_mb}MB...\n")
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                size = os.path.getsize(path)
                if size > size_limit_bytes:
                    print(f"{path} - {size/1024/1024:.2f} MB")
            except PermissionError:
                print(f"Skipping {path} (permission denied)")

if __name__ == "__main__":
    scan_large_files(".", 1)
