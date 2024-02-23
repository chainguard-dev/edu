#!/usr/bin/env python

"""
This script will output a Markdown formatted table showing the differences
between Wolfi and other distro's busybox and coreutils packages.
"""

import json
import sys

# This ought to be turned into an argument or env variable
with open("../../data/distro-package-comparisons.json", encoding="utf8") as f:
    all_distro_packages = json.load(f)


class DistroPackages:
    """glorified data storage class, but could use extended in future with other packages"""
    def __init__(self, distro) -> None:
        self.name = distro
        self.coreutils = self.get_package_utils("coreutils")
        self.busybox = self.get_package_utils("busybox")


    def get_package_utils(self, package):
        """return unique set of utilities in a given package"""
        return set(all_distro_packages[self.name][package])


class TablePrinter:
    """print union of sets of wolfi busybox + distro busybox + wolfi coreutils + distro coreutils"""
    def __init__(self, wolfi_packages, distro_packages) -> None:
        self.wolfi = wolfi_packages
        self.distro = distro_packages

        self.utils = self.wolfi.busybox.union(self.distro.busybox)
        self.utils = self.utils.union(self.wolfi.coreutils).union(self.distro.coreutils)

    def print(self):
        """print the markdown table of the set union"""
        header = f'''| Utility | \
Wolfi busybox | \
{self.distro.name.capitalize()} busybox | \
Wolfi coreutils | \
{self.distro.name.capitalize()} coreutils |\
\n|:-:|:-:|:-:|:-:|:-:|\
'''
        print(header)
        for util in sorted(self.utils):
            # Check if the filename exists in each set
            in_set1 = util in self.wolfi.busybox
            in_set2 = util in self.distro.busybox
            in_set3 = util in self.wolfi.coreutils
            in_set4 = util in self.distro.coreutils
            row = f'''| `{util}` | \
{'✅' if in_set1 else ''} | \
{'✅' if in_set2 else ''} | \
{'✅' if in_set3 else ''} | \
{'✅' if in_set4 else '' } |\
'''
            print(row)

if __name__ == "__main__":
    requested_distro = sys.argv[1]
    if requested_distro not in all_distro_packages.keys():
        print(f'{requested_distro} not found in distro-package-comparisons.json')
        sys.exit(1)

    wolfi = DistroPackages("wolfi")
    other_distro = DistroPackages(requested_distro)
    TablePrinter(wolfi, other_distro).print()
