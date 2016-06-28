from __future__ import print_function, division, absolute_import

import sys
from os.path import isfile, join
from optparse import OptionParser

from conda_verify.recipe import validate_recipe, RecipeError
from conda_verify.package import validate_package, PackageError


def main():
    p = OptionParser()

    p.add_option('-e', "--exit",
                 help="on error exit",
                 action="store_true")

    p.add_option('-q', "--quiet",
                 action="store_true")

    opts, args = p.parse_args()
    verbose = not opts.quiet

    for path in args:
        if isfile(join(path, 'meta.yaml')):
            if verbose:
                print("==> %s <==" % path)
            try:
                validate_recipe(path)
            except RecipeError as e:
                sys.stderr.write("Error: %s\n" % e)
                if opts.exit:
                    sys.exit(1)

        elif path.endswith('.tar.bz2'):
            if verbose:
                print("==> %s <==" % path)
            try:
                validate_package(path, verbose)
            except PackageError as e:
                sys.stderr.write("Error: %s\n" % e)
                if opts.exit:
                    sys.exit(1)

        else:
            if verbose:
                print("Ignoring: %s" % path)


if __name__ == '__main__':
    main()
