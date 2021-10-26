from gendiff.cli import parse
from gendiff.engine.differ import generate_diff


def main():
    parser = parse()
    diff = generate_diff(
        parser.first_file,
        parser.second_file,
        parser.format
    )
    print(diff)


if __name__ == '__main__':
    main()
