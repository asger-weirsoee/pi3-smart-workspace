from setuptools import setup
with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name='pi3-smart-workspace',
    version='0.1.0',
    packages=['pi3'],
    url='https://github.com/GeneralDenmark/PyOutputHandler',
    license='Apache-2.0 License ',
    install_requires=[
        "evdev==1.3.0",
        "i3ipc==2.2.1",
        "pynput==1.7.1",
        "python-xlib==0.27",
        "six==1.15.0"
    ],
    entry_points={"console_scripts": ["pi3-smart-workspace=pi3.smart_workspace:main"]},
    scripts=["pi3/smart_workspace.py"],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Asger Geel Weirsøe',
    author_email='asger@weirsoe.dk',
    description='Simple program that looks through the i3 config and finds the bound workspaces for each output, and then opening that workspace on the output, that the mouse is currently on.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Desktop Environment :: Window Managers",
    ],
)
