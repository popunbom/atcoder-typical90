#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from glob import glob
import subprocess as sp
from os import path

from rich.console import Console

DEFAULTS = {
    "EXEC_NAME": "main",
    "SAMPLE_DIRNAME": "samples",
    "INPUT_FILENAME_PATTERN": "input_*",
    "OUTPUT_FILENAME_PATTERN": "output_*",
}

console = Console()


class Args(argparse.Namespace):
    project_dir: str
    exec_name: str
    sample_dirname: str
    input_filename_pattern: str
    output_filename_pattern: str


def main(args: Args) -> int:
    input_files = sorted(glob(path.join(
        args.project_dir,
        args.sample_dirname,
        args.input_filename_pattern,
    )))
    output_files = sorted(glob(path.join(
        args.project_dir,
        args.sample_dirname,
        args.output_filename_pattern,
    )))

    all_ok = True
    for input_file, output_file in zip(input_files, output_files):
        expect: str = None
        with open(output_file) as f:
            expect = f.read().strip()

        result: sp.CompletedProcess[bytes] = None
        with open(input_file, "rb") as f:
            result = sp.run(
                path.abspath(path.join(args.project_dir, args.exec_name)),
                input=f.read(),
                stdout=sp.PIPE
            )
        assert result.returncode == 0

        actual = result.stdout.decode().strip()

        if expect != actual:
            console.print("\n".join([
                "[bold red]NG: {!r}[/]".format(
                    path.relpath(input_file),
                ),
                "  Expect: {!r}".format(expect),
                "  Actual: {!r}".format(actual),
            ]))
            all_ok = False
        else:
            console.print(
                "[bold green]OK: {!r}[/]".format(input_file)
            )

    if not all_ok:
        return -1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("project_dir", type=str,
                        help="Project directory")

    parser.add_argument("--exec_name", required=False, type=str,
                        default=DEFAULTS["EXEC_NAME"],
                        help="Executable name")
    parser.add_argument("--sample_dirname", required=False, type=str,
                        default=DEFAULTS["SAMPLE_DIRNAME"],
                        help="Directory name of input/output samples")
    parser.add_argument("--input_filename_pattern", required=False, type=str,
                        default=DEFAULTS["INPUT_FILENAME_PATTERN"],
                        help="Filename pattern for inputs")
    parser.add_argument("--output_filename_pattern", required=False, type=str,
                        default=DEFAULTS["OUTPUT_FILENAME_PATTERN"],
                        help="Filename pattern for outputs")

    exit(main(parser.parse_args()))
