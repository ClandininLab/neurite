#!/usr/bin/env python

from setuptools import find_packages, setup

# run setup
setup(
    name="neurite",
    version="0.2",
    license="MIT",
    description="Neural Networks Toolbox for Medical Imaging",
    url="https://github.com/adalca/neurite",
    keywords=["imaging", "cnn"],
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "packaging",
        "six",
        "numpy>=1.17",
        "scipy",
        "tqdm",
        "matplotlib",
        "scikit-learn",
        "nibabel",
        "pystrum @ git+ssh://git@github.com/ClandininLab/pystrum.git@3282980923e2563d7b9947002a39e08163553709",
    ],
)
