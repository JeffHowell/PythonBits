import sys
import argparse


def main (argv):
    ns = parse_cmd_line_args(argv)
    if ns.foo:
        print "oh foo!"
    if ns.baz:
        print "I'd like {} baz, please".format(ns.baz)

    print(ns)


def parse_cmd_line_args(argv, argParser=argparse.ArgumentParser()):
    # ap = argparse.ArgumentParser(description="hello from ArgumentParser")
    ap = argParser(description="hello from ArgumentParser")
    ap.add_argument('-foo', action='store_true', help='give a foo')
    ap.add_argument('-baz', type=int, help="how much baz")
    ap.add_argument('mumble', nargs='?', default='grumble')
    ns = ap.parse_args(argv)
    return ns


if __name__ == '__main__':
    print("hello")
    print (sys.argv)
    main(sys.argv)

