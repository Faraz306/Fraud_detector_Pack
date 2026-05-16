from setuptools import setup

setup(
    name='yf_fraud_detector',  #* Your package will have this name
    packages=['yf_fraud_detector'],  #* Name the package again
    version='1.0.0',  #* To be increased every time your change your library
    license='MIT',  # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description='This package can be used to make Fraud Detector in 2 lines of code.',
    # Short description of your library
    author='Yamaan Faraz YF® official',  # Your name
    author_email='farazyamaan@gmail.com',  # Your email
    url='https://example.com',  # Homepage of your library (e.g. github or your website)
    keywords=['fraud detector', '2 lines Fraud Detector', 'YF', "Yamaan Faraz YF® official package"],  # Keywords users can search on pypi.org
    install_requires=['pandas', 'streamlit', 'scikit-learn'],  # Other 3rd-party libs that pip needs to install
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Type a license again
        'Programming Language :: Python :: 3.8',  # Python versions that your library supports
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
