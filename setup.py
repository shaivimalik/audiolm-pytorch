from setuptools import setup, find_packages
exec(open('audiolm_pytorch/version.py').read())

setup(
  name = 'audiolm-pytorch',
  packages = find_packages(exclude=[]),
  version = __version__,
  license='MIT',
  description = 'AudioLM - Language Modeling Approach to Audio Generation from Google Research - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/audiolm-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'audio generation'
  ],
  install_requires=[
    'accelerate==0.24.0',
    'beartype==0.16.1',
    'einops==0.7.0',
    'ema-pytorch==0.2.2',
    'encodec==0.1.1',
    'gateloop-transformer==0.2.3',
    'joblib==1.3.2',
    'local-attention==1.9.0',
    'pytorch-warmup==0.1.1',
    'scikit-learn==1.3.2',
    'sentencepiece==0.1.99',
    'torch==2.5.0',
    'torchaudio==2.5.0',
    'transformers==4.34.0',
    'vector-quantize-pytorch==1.12.5'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
