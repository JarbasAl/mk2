from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("./version.py", "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

with open("./requirements.txt", "r", encoding="utf-8") as r:
    requirements = r.readlines()

setup(
    name='ovos_mk2_enclosure',
    version=version,
    packages=find_packages(),
    url='https://github.com/OpenVoiceOS/ovos-mk2-enclosure',
    license='Apache-2.0',
    install_requires=requirements,
    author='Neongecko',
    author_email='developers@neon.ai',
    description=long_description,
    entry_points={
        'console_scripts': [
            'ovos-mk2-enclosure=ovos_mk2_enclosure.__main__:main'
        ]
    }
)
