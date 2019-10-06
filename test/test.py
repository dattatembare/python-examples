from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('-a', '--inputfile', required=False, help='Input data file path')
    parser.add_argument('-b', '--inputspec', required=False, help='Input specification file path')
    parser.add_argument('-c', '--profile', required=False, help='Input profile file path')

    args = parser.parse_args().__dict__
    test_cfg = {'inputfile': 'val1', 'inputspec': 'val2', 'profile': 'val3'}
    test_cfg = {k: args.get(k) if args.get(k) else v for k, v in test_cfg.items()}

    print(test_cfg)


if __name__ == '__main__':
    main()
