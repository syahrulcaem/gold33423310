from setuptools import setup

setup(
    name='gold-33423310',
    version='0.1',
    packages=['gold'],
    entry_points={
        'console_scripts': [
            'gold=gold:hitung_golden_ratio',
        ],
    },
)
