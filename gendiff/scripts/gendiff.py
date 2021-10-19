from gendiff.engine import gendiff


def main():
    parser = gendiff.generation()
    diff = gendiff.generate_diff(
        parser.first_file,
        parser.second_file,
        parser.format
    )
    print(diff)

if __name__ == '__main__':
    main()
