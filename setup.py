import setuptools
from mautrix import __version__

setuptools.setup(
    name="mautrix",
    version=__version__,
    url="https://github.com/tulir/mautrix-python",

    author="Tulir Asokan",
    author_email="tulir@maunium.net",

    description="A Python 3 asyncio Matrix framework.",
    long_description=open("README.rst").read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3.0.1,<4",
        "future-fstrings>=0.4.2",
        "attrs>=18.2.0,<19",
    ],
    extras_require={
        "detect_mimetype": ["python-magic>=0.4.15,<0.5"],
    },
    python_requires="~=3.5",

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Communications :: Chat",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
