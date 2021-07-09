from setuptools import setup, find_packages

setup(
    name="babysitterbot",
    description="A discord bot used to babysit and moderate a server.",
    version="0.0.0",
    author="Chris Webster",
    maintainer="Chris Webster",
    url="https://github.com/chriswebster98/babysitterbot",
    packages=find_packages(),
    entry_points={
        'console_scripts' : [
            'babysitter = babysitter.babysitter:main'
        ]
    }
)