#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
from os import path
import os
import shutil
import string
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from rich.console import Console

INPUT_OUTPUT_DIRNAME = "samples"
PROJECT_DIR_PATTERN = "typical90_{index}"
PROJECT_ROOT = path.join(path.dirname(__file__), "../../")
PROJECT_TEMPLATE_DIR = path.join(path.dirname(__file__), "../template/")
URL_PATTERN = "https://atcoder.jp/contests/typical90/tasks/typical90_{index}"
VSCODE_WORKSPACE_FILE = path.join(
    path.dirname(__file__),
    "../../atcoder-typical90.code-workspace",
)


console = Console()


class Args(argparse.Namespace):
    prob_num: int


def add_project(dir_path: str, inputs: List[str], outputs: List[str]):
    shutil.copytree(PROJECT_TEMPLATE_DIR, dir_path)
    dir_path_io = path.join(dir_path, INPUT_OUTPUT_DIRNAME)
    os.makedirs(dir_path_io)
    for i, (input, output) in enumerate(zip(inputs, outputs), start=1):
        with open(path.join(dir_path_io, "input_{}".format(i)), "wt") as f:
            print(input, file=f)
        with open(path.join(dir_path_io, "output_{}".format(i)), "wt") as f:
            print(output, file=f)

    console.print("".join([
        "[green bold]",
        "Sucess to Create project: {!r}".format(dir_path),
    ]))


def main(args: Args) -> int:
    def gen_index(n: int) -> str:
        n -= 1
        s = " " + string.ascii_lowercase
        return (s[n // 26] + s[(n % 26) + 1]).strip()

    def extract_inputs_outputs(dom: BeautifulSoup, h3_text: str) -> List[str]:
        return [
            h3.next_sibling.text.replace("\r\n", "\n")
            for h3 in dom.find_all("h3")
            if h3_text in str(h3)
        ]

    index = gen_index(args.prob_num)
    url = URL_PATTERN.format(index=index)
    dom = BeautifulSoup(requests.get(url).text, features="html.parser")

    inputs = extract_inputs_outputs(dom, "入力例")
    outputs = extract_inputs_outputs(dom, "出力例")

    dir_name = PROJECT_DIR_PATTERN.format(index=index)
    dir_path = path.join(PROJECT_ROOT, dir_name)
    if path.isdir(dir_path):
        console.print("".join([
            "[yellow bold]",
            "Project already exists: {!r} -- abort.".format(
                dir_path,
            )
        ]))
        return -1

    add_project(dir_path, inputs, outputs)

    # Update .code-workspace
    workspace: Dict = None
    with open(VSCODE_WORKSPACE_FILE) as f:
        workspace = json.load(f)
    workspace["folders"] = [
        {"path": "./" + dir_name},
        *workspace["folders"],
    ]
    with open(VSCODE_WORKSPACE_FILE, "w") as f:
        json.dump(workspace, f, indent=2)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("prob_num", type=int,
                        help="Problem number ([1-90])")

    exit(main(parser.parse_args()))
