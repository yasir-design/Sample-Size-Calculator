"""This is the main file"""
import math
import os
import random
from pprint import pprint

import pandas
import pandas as pd
from pathlib import Path

from app.config import Config
from app.file_ops import FileOperations
from app import pandas_calculations
from app.pandas_calculations import *


def main():
    data_directory = os.path.join(Config.data_directory)
    absolute_path = FileOperations.get_calculate_file_path(data_directory, Config.data_file_name)
    df = PandasCsvRead.get_df(absolute_path)

    population_count = PandasCount.get_count(df, Config.data_field)

    minimum = PandasMin.get_min(df, Config.data_field)
    maximum = PandasMax.get_max(df, Config.data_field)

    for e in Config.margin_of_error:
        for z in Config.z_scores:
            sample_size = RoundingToAppConfid.get_result(SampleSize.calculate_sample_size(population_count, z, e))

    df1 = pd.DataFrame([OutputFiles.get_output_files(df)])

    min_row = df[df[Config.data_field] == minimum]
    max_row = df[df[Config.data_field] == maximum]
    df2 = pd.DataFrame([[min_row], [max_row]])
    pd.concat([df1, df2])


if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()
