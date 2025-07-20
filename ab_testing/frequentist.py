import numpy as np
from scipy import stats

def run_t_test(control,variant, alpha=0.05):
    """"
    Independent two-sample t-test.
    parameters:
    1.control: list or np.array of control group values
    2.carient: list or np.array of varient group values
    3.alpha: signifant level (default = 0.05)

    Returns:
    - Result dictionary with t-statistic, p-value, means,
    and significance decision
    """
    control = np.array(control)
    variant = np.array(variant)

    t_stat, p_value = stats.ttest_ind(control,variant,equal_var=False)
    result ={"control_mean": np.mean(control),
             "variant_mean":np.mean(variant),
             "mean_diff":np.mean(variant) - np.mean(control),
             "t_statistic": t_stat,
             "p_value":p_value,
             "is_significant":p_value < alpha
             }
    return result