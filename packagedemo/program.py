#!/usr/bin/env python3
import sys
import pkg.multireader

# Modules with Packages

def main():
    """Main Function"""
    
    r = pkg.multireader.MultiReader('test.gz')
    print(r.read())
    r.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
