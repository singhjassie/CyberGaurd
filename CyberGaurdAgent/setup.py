from setuptools import setup, find_packages

setup(
    name="filebeat_manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'filebeat-manager=filebeat_manager.main:main'
        ]
    },
    install_requires=[],
)

