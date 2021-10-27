"""Some helpful utility functions for working with CSV files."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'rable'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8") 
    # Read that file

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result