import setuptools


requirements = [
    'xmltodict',
    'requests',
]

setuptools.setup(
    name="wmapi",
    version="0.1",
    url="https://github.com/sellerzoncom/wmapi",
    author="SellerZon",
    author_email="dev@sellerzon.com",
    description="Python Client for Walmart Canada Marketplace API",
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
