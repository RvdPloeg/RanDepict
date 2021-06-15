#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RanDepict",
    version="1.0.0-dev",
    author="Otto Brinkhaus",
    author_email="henning.brinkhaus@uni-jena.de, kohulan.rajan@uni-jena.de",
    maintainer="Otto Brinkhaus, Kohulan Rajan",
    maintainer_email="henning.brinkhaus@uni-jena.de, kohulan.rajan@uni-jena.de",
    description="RanDepict is an easy-to-use utility to generate a big variety of chemical structure depictions (random depiction styles and image augmentations).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OBrink/RanDepict",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=[
        "numpy>=1.19",
        "imgaug",
        "scikit-image",
        "epam.indigo",
        "jpype1",
        "ipyplot",
        "rdkit-pypi",
        "imagecorruptions",
    ],
      data_files=[('superatom', ['RanDepict/assets/superatom.txt']),
                  ('cdk_jar', ['RanDepict/assets/jar_files/cdk_2_5.jar']),
                  ('straight_arrows', ['RanDepict/assets/arrow_images/straight_arrows/*.png']),
                  ('curved_arrows', ['RanDepict/assets/arrow_images/curved_arrows/*.png']),
                  ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
