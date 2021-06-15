from scripts.migration.practicingtest import transform_dataframe
from pandas._testing import assert_frame_equal
import pandas as pd

def test_practicingtest():
    df = pd.DataFrame(
        {
            'A': [1, 2],
            'b': [1, 2]
        }
    )

    df_result = transform_dataframe(df)
    df_expected = pd.DataFrame(
        {
            'a': [1, 2],
            'b': [1, 2]
        }
    )
    assert_frame_equal(df_result, df_expected)
    