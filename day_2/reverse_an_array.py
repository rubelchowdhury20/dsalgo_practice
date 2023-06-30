import argparse


def main(args):
    n = len(args.array)
    for idx, i in enumerate(args.array):
        print(args.array[n - 1 - idx])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--array', help='array to be reversed')
    main(parser.parse_args())