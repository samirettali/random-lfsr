#!/usr/bin/env python3
import random

class LFSR:
    def __init__(self, size):
        self.state = random.randint(0, (2 ** size) - 1)
        self.size = size

    def next(self):
        new_bit = (self.state ^ (self.state >> 1) ^ (self.state >> 5) ^ (self.state >> 7)) & 1
        new_bit = (self.state ^ (self.state >> 1)) & 1
        self.state = (self.state >> 1) | (new_bit << self.size - 1)
        return self.state

    def random(self, nbits=32):
        result = 0
        for i in range(nbits - 1):
            new = self.next() & 1
            result += self.next() & 1
            result = result << 1
        return result

