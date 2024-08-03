import subprocess
import sys
import platform

def install_torch():
    system = platform.system()
    common_packages = [
        "lightning==2.3.3",
    ]

    if system == "Darwin":
        # Mac installation
        packages = [
            "torch==2.3.1",
            "torchvision==0.18.1",
        ] + common_packages
        subprocess.check_call([
            sys.executable, "-m", "pip", "install"
        ] + packages)
    elif system == "Linux":
        # Assume CUDA 11.8 for Linux
        packages = [
            "torch==2.3.1+cu121",
            "torchvision==0.18.1+cu121",
        ] + common_packages
        subprocess.check_call([
            sys.executable, "-m", "pip", "install"
        ] + packages + ["--extra-index-url", "https://download.pytorch.org/whl/cu121"])
    else:
        print(f"Unsupported system: {system}")
        sys.exit(1)

    # Verify installation
    try:
        import torch
        import torchvision
        import lightning

        print(f"PyTorch version: {torch.__version__}")
        print(f"TorchVision version: {torchvision.__version__}")
        print(f"Lightning version: {lightning.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
    except ImportError as e:
        print(f"Error importing packages: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_torch()
