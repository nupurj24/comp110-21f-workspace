"""Utility functions."""

__author__ = "730391424"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8") 
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """A function that produces a list of all values in a single column whose name is the second parameter."""
    column_values: list[str] = []
    for row in table: 
        item: str = row[column_name]
        column_values.append(item)
    return column_values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """A function that will turn a row-oriented table into a column oriented one."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """A function to produce a column based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        list_of_n: list[str] = []
        i: int = 0
        while i < n:
            list_of_n.append(column_table[column][i])
            i += 1
        result[column] = list_of_n
    return result 


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """A function that creates a column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result 


def concat(column_table_1: (dict[str, list[str]]), column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """A function that will produce a new column-based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table_1:
        result[column] = column_table_1[column]
    for column in column_table_2:
        if column in result:
            result[column] = column_table_2[column]
        else:
            result[column] = column_table_2[column]
    return result 


def count(input_list: list[str]) -> dict[str, int]:
    """A function that given a list of strings will return a dictionary of strings and integers."""
    result: dict[str, int] = {}
    for current_value in input_list:
        if current_value in result:
            result[current_value] += 1
        else:
            result[current_value] = 1
    return result 