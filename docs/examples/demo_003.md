---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{warning}
This documentation page is still work in progress! Some information might be outdated.
```

# 3. Result Object

Which information is contained in the result of Psignifit

```{code-cell} ipython3
import numpy as np

import psignifit as ps

# to have some data we use the data from demo_001
data = np.array([[0.0010, 45.0000, 90.0000], [0.0015, 50.0000, 90.0000],
                 [0.0020, 44.0000, 90.0000], [0.0025, 44.0000, 90.0000],
                 [0.0030, 52.0000, 90.0000], [0.0035, 53.0000, 90.0000],
                 [0.0040, 62.0000, 90.0000], [0.0045, 64.0000, 90.0000],
                 [0.0050, 76.0000, 90.0000], [0.0060, 79.0000, 90.0000],
                 [0.0070, 88.0000, 90.0000], [0.0080, 90.0000, 90.0000],
                 [0.0100, 90.0000, 90.0000]])

# Run psignifit
res = ps.psignifit(data, sigmoid_name='norm', experiment_type='2AFC')
```

now we can have a look at the res dictionary and all its fields.

The most important result are the fitted parameters of the psychometric
function. They can be found in a dictionary format.


```{code-cell} ipython3
print(res.parameter_estimate)
```

For each of these parameters, also the confidence interval is contained
in the results as a dictionary.


```{code-cell} ipython3
# TODO: Uncomment if confidence intervals are implemented
# print(res.confidence_intervals)
```

In addition, the result contains the complete configuration which
was used to fit.


```{code-cell} ipython3
print(res.configuration)
```

Save, load, and repeat
----------=-----------
The results can be saved as a json file.


```{code-cell} ipython3
file_name = 'psignifit-result.json'
res.save_json(file_name)
```

This file can be loaded to get a result object again.


```{code-cell} ipython3
loaded_res = ps.Result.load_json(file_name)
assert res == loaded_res, "The original and loaded result should be equal."
```

Because the result object contains the configuration,
it is easy to restart the experiment with the same configuration.


```{code-cell} ipython3
restarted_res = ps.psignifit(data, res.configuration)
```

## Advanced fields

The result also contains weights and posterior probability
at a whole grid of possible parameter combinations.
These were generated during fitting the parameters and calculating
the confidence intervals.

They are useful for some advanced plots and analysis.