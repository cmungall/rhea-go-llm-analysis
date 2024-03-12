import csv
import json
import glob
from collections import defaultdict
from typing import Dict, List
import pandas as pd

def read_mappings() -> List[Dict]:
    """
    Read the mappings from the file

    :return:
    """
    with open("../data/go.sssom.tsv", 'r') as file:
        reader = csv.DictReader(file, delimiter="\t")
        data = [row for row in reader]
        return data


def load_jsonl(file_path: str) -> List[Dict]:
    """
    Load a jsonl file into a list of dictionaries

    :param file_path:
    :return:
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data


def _replace_newlines(row: Dict) -> Dict:
    """
    Replace newlines in a dictionary

    :param row:
    :return:
    """
    for k, v in row.items():
        if isinstance(v, str):
            row[k] = v.replace("\n", " ")
    return row

def load_all(min_results=100) -> pd.DataFrame:
    """
    Load all jsonl files in ../results/*.jsonl

    :param min_results:
    :return:
    """
    paths = glob.glob("../results/*.jsonl")
    df = pd.DataFrame()
    for path in paths:
        data = load_jsonl(path)
        data = [_replace_newlines(row) for row in data]
        toks = path.split("/")[-1].split(".")[1:-1]
        n = "-".join(toks)
        if len(data) > min_results:
            temp_df = pd.DataFrame(data)
            temp_df['model'] = n
            df = pd.concat([df, temp_df], ignore_index=True)
    return df


def show(df: pd.DataFrame):
    """
    Render

    :param df:
    :param n:
    :return:
    """
    for i, row in df.iterrows():
        print(f"# Pair: {row['subject_id']} - {row['object_id']}")
        print("\nSUBJECT:\n")
        print(row['subject_info'])
        print("\nOBJECT:\n")
        print(row['object_info'])
        print(f"\nPROBLEMS: {row['problem_sum']} (confidence: {row['confidence_avg']})")
