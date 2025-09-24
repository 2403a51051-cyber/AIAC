from typing import Optional


def read_file(filename: str, encoding: str = "utf-8") -> str:

    try:
        with open(filename, "r", encoding=encoding) as file_handle:
            return file_handle.read()
    except FileNotFoundError as error:
        raise FileNotFoundError(f"File not found: {filename}") from error
    except PermissionError as error:
        raise PermissionError(f"Permission denied while reading: {filename}") from error
    except UnicodeDecodeError as error:
        raise UnicodeDecodeError(error.encoding, error.object, error.start, error.end, f"Failed to decode file '{filename}': {error.reason}")
    except OSError as error:
        raise OSError(f"I/O error while reading '{filename}': {error}") from error


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Read and print a text file.")
    parser.add_argument("filename", help="Path to the file to read")
    parser.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")
    args = parser.parse_args()

    try:
        print(read_file(args.filename, args.encoding))
    except Exception as exc:
        print(f"Error: {exc}")


