"""This is the main startup of the app"""
import math
import os
import random
from pprint import pprint

import pandas
import pandas as pd
from pathlib import Path

from app.config import Config
from app.file_ops import FileOperations


class PandasCsvRead:
    """Read CSV with Pandas and return Data Frame"""

    @staticmethod
    def get_df(absolute_path: str):
        """Gets Data Frame"""
        return pandas.read_csv(absolute_path)


class PandasMean:
    """Pandas Mean"""

    @staticmethod
    def get_mean(data_frame: pandas.DataFrame, mean: str):
        """Get Mean"""
        return data_frame[mean].mean()


class PandasCount:
    """Pandas Count"""

    @staticmethod
    def get_count(data_frame: pandas.DataFrame, count: str):
        """Get Count"""
        return data_frame[count].count()


class PandasStdDev:
    """Pandas Std Deviation"""

    @staticmethod
    def get_stddev(data_frame: pandas.DataFrame, std: str):
        """Get StdDev"""
        return data_frame[std].std()


class PandasMin:
    """Pandas Min"""

    @staticmethod
    def get_min(data_frame: pandas.DataFrame, field_min: str):
        """Get Min"""
        return data_frame[field_min].min()


class PandasMax:
    """Pandas Max"""

    @staticmethod
    def get_max(data_frame: pandas.DataFrame, field_max: str):
        """Get Max"""
        return data_frame[field_max].max()


class SampleSize:
    """Calculate Sample Size"""

    @staticmethod
    def calculate_sample_size(pop_size, z_score, margin_of_error, std=0.5):
        """Calculating Sample Size"""
        n = pop_size
        z = z_score
        e = margin_of_error
        p = std
        z_score_squared = MathPowers.square(z)
        margin_error_squared = MathPowers.square(e)
        numerator = (z_score_squared * p * (1 - p)) / margin_error_squared
        denominator = 1 + (numerator * (1/n))
        return numerator / denominator


class PandasSample:
    """Pandas Sample"""

    @staticmethod
    def get_sample(data_frame: pandas.DataFrame, size: int):
        """Get Sample"""
        return data_frame.sample(size)


class PandasWrite:
    """Pandas Write"""

    @staticmethod
    def write(data_frame: pandas.DataFrame, path: str):
        """Get Results"""
        return data_frame.to_csv(path, index=False)


class RoundingToAppConfid:
    """Round the value to the apps rounding_precision config setting"""

    @staticmethod
    def get_result(value):
        """Get Results"""
        return round(value, Config.rounding_precision)


class MathPowers:
    """Calculate a numbers power"""

    @staticmethod
    def square(value):
        """Get Square"""
        return pow(value, 2)


class OutputFiles:
    """Outputting the files"""

    @staticmethod
    def get_output_files(data_frame: pandas.DataFrame):
        """function for outputting files"""
        count_pop = PandasCount.get_count(data_frame, Config.data_field)
        for e in Config.margin_of_error:
            for z in Config.z_scores:
                sample_size = int(SampleSize.calculate_sample_size(count_pop, z, e))

                sample = PandasSample.get_sample(data_frame, sample_size-2)

                output_name = "sample_data_number_" + str(z) + "_" + str(e) + "_" + str(sample_size) + ".csv"
                output_path = FileOperations.get_calculate_file_path(Config.sample_files_output, output_name)
                PandasWrite.write(sample, output_path)

