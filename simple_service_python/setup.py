from setuptools import setup

package_name = 'simple_service_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='plantstoen',
    maintainer_email='plantstoen@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_service_server = simple_service_python.basic_service_server:main',
            'basic_service_client = simple_service_python.basic_service_client:main',
            'custom_service_server = simple_service_python.custom_service_server:main',
            'custom_service_client = simple_service_python.custom_service_client:main',
        
        ],
    },
)
