from setuptools import setup, find_packages

setup(
    name="f1cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "requests",
        "rich",
        "prettytable"
    ],
    entry_points={
        "console_scripts": [
            "f1cli = main:app"
        ]
    },
    author="A",
    author_email="example@domain.com",
    description="A CLI tool to fetch Formula 1 data",
    url="https://github.com/yourusername/f1cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
