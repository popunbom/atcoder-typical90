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
    only_exec: bool
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
        input: str = None
        with open(input_file) as f:
            input = f.read().strip()
        input = "\n".join(line.strip() for line in input.splitlines())

        output: str = None
        with open(output_file) as f:
            output = f.read().strip()
        output = "\n".join(line.strip() for line in output.splitlines())

        stdout: str = None
        result: sp.CompletedProcess[bytes] = None
        with open(input_file, "rb") as f:
            result = sp.run(
                path.abspath(path.join(args.project_dir, args.exec_name)),
                input=input.encode(),
                stdout=sp.PIPE
            )
            assert result.returncode == 0
            stdout = result.stdout.decode().strip()
        stdout = "\n".join(line.strip() for line in stdout.splitlines())

        if args.only_exec:
            console.print("\n".join([
                "=== INPUT ===",
                input,
                "=== OUTPUT ===",
                stdout,
                "=== EXPECT ===",
                output,
                "",
            ]))
            continue

        if output != stdout:
            console.print("\n".join([
                "[bold red]NG: {!r}[/]".format(
                    path.relpath(input_file),
                ),
                "  Expect: {!r}".format(output),
                "  Actual: {!r}".format(stdout),
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

    parser.add_argument("--only_exec", required=False, action="store_true",
                        help="Only exec (not testing)")
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
