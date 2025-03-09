from setuptools import setup, find_packages

setup(
	name="manadiai",
	version="0.1.0",
	packages=find_packages(),
	python_requires=">=3.8",
	install_requires=[
	"fastapi>=0.110.0",
	"uvicorn[standard]>=0.29.0",
	"python-dateutil>=2.8.2",
],
extras_require={
	"dev": [
	"pytest>=7.4.0",
	"pytest-cov>=4.1.0",
	"black>=24.0.0",
	"flake8>=6.1.0",
	"mypy>=1.8.0",
]
},
author="Gaurav Sood",
author_email="gsood07@gmail.com",
description="Capture, organize, and reuse GenAI interactions to fine-tune your personalized AI.",
license="MIT",
url="https://github.com/matmulai/manadiai",
classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
],
)

