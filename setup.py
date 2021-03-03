from setuptools import setup, find_packages

setup(
    name="scanoss-scanner",
    version="1.3.1",
    author="SCANOSS",
    author_email="info@scanoss.com",
    description='Simple Python library to use the SCANOSS API.',
    tests_require=["pytest", "grappa"],
    install_requires=["requests", "crc32c",
                      "binaryornot"],
    include_package_data=True,
    entry_points={
        'console_scripts': ['scanner.py=scanner:main'],
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5'
)
