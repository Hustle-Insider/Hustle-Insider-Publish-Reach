from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hustle-insider-publish-reach",
    version="1.0.0",
    author="HustleInsider.it.com",
    author_email="info@hustleinsider.it.com",
    description="Hustle Insider Publish Reach helps businesses, founders and brands get their news and content in front of the right audience through strategic digital visibility and content distribution.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hustleinsider.it.com",
    project_urls={
        "Homepage": "https://hustleinsider.it.com",
        "GitHub": "https://github.com/Hustle-Insider/Hustle-Insider-Publish-Reach",
        "Documentation": "https://hustle-insider-publish-reach.readthedocs.io",
        "PyPI": "https://pypi.org/project/hustle-insider-publish-reach",
    },
    py_modules=["publish_reach"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
    ],
    keywords=[
        "hustle-insider",
        "publish-reach",
        "digital-pr",
        "seo-geo",
        "ai-visibility",
        "founder-branding",
        "startup-pr",
        "saas-pr",
        "content-distribution",
    ],
    entry_points={
        "console_scripts": [
            "hustle-insider-reach=publish_reach:main",
        ],
    },
)
