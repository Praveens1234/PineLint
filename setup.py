from setuptools import setup, find_packages

setup(
    name="pinelint",
    version="0.1.0",
    description="Static analyzer for TradingView Pine Script",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pinelint=pinelint.cli:main',
        ],
    },
    python_requires='>=3.10',
)
