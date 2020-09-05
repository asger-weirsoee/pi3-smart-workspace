from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt', 'r') as file:
    required = []
    for x in file.readline():
        required.append(x)


setup(
    name="pi3-smart-workspace",
    description="A smart switcher for multiple workspaces.",
    long_description=long_description,
    version="0.0.1",
    license="Apache License",
    author="Asger Geel Weirsøe",
    author_email="asger@weirsoe.dk",
    url="https://github.com/GeneralDenmark/PyOutputHandler",
    install_requires=required,
    packages=["pi3"],
    zip_safe=True,
    entry_points={"console_scripts": ["pi3-smart-workspace = pi3.smart-workspace:main"]},
    scripts=["pi3/smart-workspace.py"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Desktop Environment :: Window Managers",
    ],
)