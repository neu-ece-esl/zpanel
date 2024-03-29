"""Setup."""

from setuptools import setup, find_packages

setup(
    name="zpanel",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "."},
    package_data={"zmon": ["data/views/*", "data/web_static/*"]},
    install_requires=[
        "pyzmq",
        "cheroot",
        "simpleaudio",
        "bottle @ git+https://github.com/bottlepy/bottle.git@master#egg=bottle",
    ],
    author="Bruno Morais",
    author_email="brunosmmm@gmail.com",
    description="Zpanel Zedboard IO emulator",
    scripts=["zpanel"],
)
