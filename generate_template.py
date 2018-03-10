import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('entries', type=int)
    parser.add_argument('filename')
    return parser.parse_args()


def main():
    args = parse_args()
    filename = args.filename
    entries = args.entries
    single = "Topic:\nLink:\nTitle:\nTags:\n\n\n"
    with open(filename, 'w') as handle:
        result = single * entries
        handle.write(result)
    print('Done')




if __name__ == '__main__':
    main()
