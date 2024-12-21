from setuptools import setup, find_packages

setup(
    name="mylib",
    version="1.0.0",
    test_suite='tests',
    author="Romitsina Spelov",
    author_email="romitsina.a.r@gmail.com",
    description="Библиотека для работы с факториалами и вычисления чисел из формул типа str",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    license='example',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
