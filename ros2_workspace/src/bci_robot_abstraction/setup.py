from setuptools import find_packages, setup

package_name = "bci_robot_abstraction"

setup(
    name=package_name,
    version="1.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Mohamed Abdelsalam",
    maintainer_email="alexlavander7@gmail.com",
    description="Robot-independent abstraction layer for the Hybrid Adaptive BCI.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "robot_node = bci_robot_abstraction.robot_node:main",
        ],
    },
)
