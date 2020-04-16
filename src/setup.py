import setuptools
import os

readname_path = os.path.join("..", "README.md")
with open(readname_path, "r") as f:
    long_description = f.read()

setuptools.setup(
    name = "zoopt-optimizer",
    version = "0.1.0",
    author = "vicenley",
    author_email = "vlk@ornl.gov",
    description = "Zero Order Optimization Algorithm in Orquestra",
    packages = setuptools.find_packages(where = "python"),
    package_dir = {"" : "python"},
    classifiers = (
        "programming language :: Python :: 3",
        "Operative System :: OS Independent"),
    install_requires=[
        'z-quantum-core',
        'zoopt'
    ]
)