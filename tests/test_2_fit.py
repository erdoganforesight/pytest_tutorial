"""
test for rtanalysis
- in this test, we will create a simulated dataset and fit
it, ensuring that the answers are correct
"""

import numpy as np
from rtanalysis.rtanalysis import RTAnalysis
from rtanalysis.generate_testdata import generate_test_df


def test_rtanalysis_fit():
    rta = RTAnalysis()
    meanRT = 2.1
    sdRT = 0.9
    meanAcc = 0.8
    test_df = generate_test_df(meanRT, sdRT, meanAcc)
    rta.fit(test_df.rt, test_df.accuracy)
    assert np.allclose(meanRT, rta.meanrt_)
    assert np.allclose(meanAcc, rta.meanacc_)
    
    
  
def test_rtanalysis_fit2():
    rta = RTAnalysis()
    meanRT = 2.1
    sdRT = 0.9
    meanAcc = 0.8
    test_df = generate_test_df(meanRT, sdRT, meanAcc)
    rta.fit(test_df.rt, test_df.accuracy)
    assert np.allclose(meanRT, rta.meanrt_)
    assert np.allclose(meanAcc, rta.meanacc_)
