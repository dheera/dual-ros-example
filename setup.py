from setuptools import setup

package_name = 'dual_ros_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    # package_dir = {package_name: "src/" + package_name},
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    #zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    #entry_points={
    #    'console_scripts': [
    #        "example_node = dual_ros_example.example_node:main",
    #    ],
    #},
)
