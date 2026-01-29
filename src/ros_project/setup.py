from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'description'),
            glob('description/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gautam',
    maintainer_email='gautam@example.com',
    description='Robot description package',
    license='Apache License 2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [],
    },
)
