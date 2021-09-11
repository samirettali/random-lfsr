#!/usr/bin/env python3
from lfsr import LFSR

def main():
    lsfr = LFSR(128)
    for i in range(10):
        print(lsfr.random())


if __name__ == '__main__':
    main()
