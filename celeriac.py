"""
celeriac

Usage:
	celeriac init <name>
	celeriac init <name> [-s | --skinos] [--flow]
	celeriac -h | --help
	celeriac -v | --version
	celeriac run

Options:
	-h --help    Show this screen.
    -s --skinos  With custom consumers.
"""
from docopt import docopt

if __name__ == '__main__':
    ARGS = docopt(__doc__)
    print(ARGS)

    FLOW = False
    SKINOS = False

    # print params
    if ARGS['-h'] or ARGS['--help']:
        print(__doc__)
        exit(0)
    elif ARGS['-v'] or ARGS['--version']:
        print('v0.0.1a')
        exit(0)

    if ARGS['run']:
        print('Not impremented yet.')
    elif ARGS['init']:
        if ARGS['--flow']:
            FLOW = True
        if ARGS['--skinos'] or ARGS['-s']:
            SKINOS = True
        print('Not impremented yet.')

    else:
        print(__doc__)
        exit(1)
