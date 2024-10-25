#!/usr/bin/python3
"""
markdown2html.py: Converts a Markdown file to HTML.

This script reads a Markdown file, converts headings to HTML format, and outputs
the converted HTML to a specified file.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file (str): Path to the Markdown file to be converted.
    output_file (str): Path where the converted HTML file will be saved.

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re
import sys


def convert_markdown_to_html(markdown_file_path, html_file_path):
    """
    Converts a Markdown file to HTML by converting headings.

    Args:
        markdown_file_path (str): Path to the input Markdown file.
        html_file_path (str): Path to the output HTML file.
    """
    with open(markdown_file_path, encoding='utf-8') as md_file:
        markdown_lines = md_file.readlines()

    html_lines = []
    for line in markdown_lines:
        heading_match = re.match(r'(#){1,6} (.*)', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)
            html_lines.append(f'<h{heading_level}>{heading_text}</h{heading_level}>\n')
        else:
            html_lines.append(line)

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('markdown_file_path', help='Path to input Markdown file')
    parser.add_argument('html_file_path', help='Path to output HTML file')
    args = parser.parse_args()

    markdown_path = pathlib.Path(args.markdown_file_path)
    if not markdown_path.is_file():
        print(f'Missing {markdown_path}', file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(args.markdown_file_path, args.html_file_path)

