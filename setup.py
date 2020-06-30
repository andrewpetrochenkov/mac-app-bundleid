import setuptools

setuptools.setup(
    name='mac-app-bundleid',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/app-bundleid']
)
