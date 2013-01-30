from setuptools import setup

setup(
	name='pypal',
	version='0.2',
	description='PayPal API bindings in Python',
	author='Jared Morse',
	author_email='jarcoal@gmail.com',
	url="https://github.com/jarcoal/pypal",
	packages=['pypal'],
	install_requires=['requests >= 1.0.0'],
    license="BSD",
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
)