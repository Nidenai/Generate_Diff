from gendiff.cli import generate_diff, generation


def main():
    parser = generation()
    diff = generate_diff(
        parser.first_file,
        parser.second_file,
        parser.format
    )
    print(diff)


if __name__ == '__main__':
    main()
