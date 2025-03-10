from setuptools import setup, find_packages

setup(
    name="f1_cli",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "requests",
        "rich",
        "prettytable"
    ],
    entry_points={
        "console_scripts": [
            "f1cli=f1_cli.main:app"
        ]
    },

    author="A",
    author_email="example@domain.com",
    description="A CLI tool to fetch Formula 1 data",
    url="https://github.com/monkspams/f1cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
