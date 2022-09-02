import argparse
from Network import Network
from CreateStructure import create_structure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--number_switches',
        help='number of linear switches in topology.'
        ' Must be greater or equal than 0.',
        type=int,
        default = 0
    )

    parser.add_argument(
        '-v',
        '--verbose',
        help='increase output verbosity',
        action="store_true"
    )

    parser.add_argument(
        '-q',
        '--quiet',

        help='decrease output verbosity',
        action="store_true"
    )

    args = parser.parse_args()
    log_level = 'info'
    if (args.quiet):
        log_level = 'error'
    elif args.verbose:
        log_level = 'debug'

    if (args.number_switches <= 0):
        number_switches = 0
    elif (args.number_switches > 10):
        number_switches = 10
    else:
        number_switches = args.number_switches

    hosts, switches, links = create_structure(number_switches)

    network = Network(log_level, hosts, switches, links)
    network.run()

if __name__ == '__main__':
    main()
