from setuptools import setup,find_packages


setup(
    name="mathutils",
    version="0.10",
    description="package for math operations and geometry operations",
    package_data=find_packages(),
    classifiers=[
        "Programming Language ::Python ::3",
        "Liscence :: OSI Approved :: MIT Liscence",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)