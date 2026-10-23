from setuptools import setup, find_packages

setup(
    name="hemo_models",
    version="1.0.0",
    author="Division of Computational Physiology & Bioengineering",
    description="A non-linear, cubic polynomial progression engine for multi-system physiological modeling and microcontroller telemetry decoding.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free for Charitable Use",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.8",
    install_requires=[],  # Relies entirely on built-in standard math libraries for minimal overhead
)
