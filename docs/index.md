# `m5py`

*`scikit-learn`-compliant M5 and Model trees for python*

[![Python versions](https://img.shields.io/pypi/pyversions/m5py.svg)](https://pypi.python.org/pypi/m5py/) [![Build Status](https://github.com/smarie/python-m5p/actions/workflows/base.yml/badge.svg)](https://github.com/smarie/python-m5p/actions/workflows/base.yml) [![Tests Status](./reports/junit/junit-badge.svg?dummy=8484744)](./reports/junit/report.html) [![Coverage Status](./reports/coverage/coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html) [![codecov](https://codecov.io/gh/smarie/python-m5p/branch/main/graph/badge.svg)](https://codecov.io/gh/smarie/python-m5p) [![Flake8 Status](./reports/flake8/flake8-badge.svg?dummy=8484744)](./reports/flake8/index.html)

[![Documentation](https://img.shields.io/badge/doc-latest-blue.svg)](https://smarie.github.io/python-m5p/) [![PyPI](https://img.shields.io/pypi/v/m5py.svg)](https://pypi.python.org/pypi/m5py/) [![Downloads](https://pepy.tech/badge/m5py)](https://pepy.tech/project/m5py) [![Downloads per week](https://pepy.tech/badge/m5py/week)](https://pepy.tech/project/m5py) [![GitHub stars](https://img.shields.io/github/stars/smarie/python-m5p.svg)](https://github.com/smarie/python-m5p/stargazers)

In 1996 R. Quinlan introduced the M5 algorithm, a regression tree algorithm similar to CART (Breiman), with additional pruning so that leaves may contain linear models instead of constant values. The idea was to get smoother and simpler models.

The algorithm was later enhanced by Wang & Witten under the name M5 Prime (aka M5', or M5P), with an implementation in the Weka toolbox.

`m5py` is a python implementation leveraging `scikit-learn`'s regression tree engine.


## Installing

```bash
> pip install m5py
```

## Usage

See the [usage examples gallery](./generated/gallery).

## Main features / benefits

 * The classic `M5` algorithm in python, compliant with `scikit-learn`

## See Also

 * Weka's [M5P model](https://weka.sourceforge.io/doc.dev/weka/classifiers/trees/M5P.html)
 * LightGBM's [linear_tree](https://lightgbm.readthedocs.io/en/latest/Parameters.html#linear_tree)
 * [linear-tree](https://github.com/cerlymarco/linear-tree) that has a similar procedure than lightgbm's (from
   [discussion](https://github.com/scikit-learn/scikit-learn/issues/13106#issuecomment-808730062))

### Others

*Do you like this library ? You might also like [my other python libraries](https://github.com/smarie/OVERVIEW#python)* 

## Want to contribute ?

Details on the github page: [https://github.com/smarie/python-m5p](https://github.com/smarie/python-m5p)
