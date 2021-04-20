#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Copyright (c) 2021 Nobuo Tsukamoto
    This software is released under the MIT License.
    See the LICENSE file in the project root for more information.
"""

import argparse
import os

import tabulate
import pandas as pd


KEY = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="File path of csv file.")
    args = parser.parse_args()

    result_df = pd.read_csv(args.csv_file)

    result_df["Model"] = result_df["Model"].str.replace("\\", "", regex=False)
    result_df[["AP", "AP50", "AP75", "APsmall", "APmedium", "APlarge", "ARmax=1", "ARmax=10", "ARmax=100", "ARsmall", "ARmidium", "ARlarge"]] = result_df[["AP", "AP50", "AP75", "APsmall", "APmedium", "APlarge", "ARmax=1", "ARmax=10", "ARmax=100", "ARsmall", "ARmidium", "ARlarge"]] * 100
    result_df = result_df.round(2)
    result_df.set_index("Model", inplace=True)

    print(result_df.to_markdown())

if __name__ == "__main__":
    main()