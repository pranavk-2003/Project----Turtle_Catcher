from setuptools import find_packages, setup

package_name = 'turtle_catcher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pranav',
    maintainer_email='pranavkolekar13@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "turtle_catcher=turtle_catcher.turtle_catcher:main",
            "turtle_spawner=turtle_catcher.turtle_spawner:main"
        ],
    },
)
