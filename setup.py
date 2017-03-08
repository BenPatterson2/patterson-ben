from setuptools import setup

setup(
    name='benpatterson.io',
    packages=['lib'],
    include_package_data=False,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest','lib'
    ],
)