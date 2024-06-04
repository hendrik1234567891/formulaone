# content of test_sample.py

from formulaone.helpers import get_raw_data_path
import pandas as pd


def test_check_dataframe_size():
    df = pd.read_csv(get_raw_data_path() / 'form1data')
    assert df.size > 0

    ### Mit pytest/tests alle tests ausführen. Vorher das modul installieren mit pip install -e. oder so.
