import os
from glob import glob

from setuptools import find_packages, setup

package_name = "bci_bringup"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"),
            glob("launch/*.launch.py")),
        (os.path.join("share", package_name, "config"),
            glob("config/*.csv")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Mohamed Abdelsalam",
    maintainer_email="alexlavander7@gmail.com",
    description="Bringup and hand trajectory adapter for the Hybrid Adaptive BCI.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "hand_trajectory_adapter = "
            "bci_bringup.trajectory_adapter:main",
        ],
    },
)
