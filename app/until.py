#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import hashids


class EncryptionHashIds(object):

    @property
    def __hashids(self):
        return hashids.Hashids(min_length=16)

    def encode_id(self, old_id):
        return self.__hashids.encode(old_id, int(time.time() * 1000))

    def decode_id(self, h):
        try:
            return self.__hashids.decode(h)[0]
        except IndexError:
            return None


encrypt = EncryptionHashIds()


if __name__ == '__main__':
    i = 1
    e = EncryptionHashIds()
    r = e.encode_id(i)
    d = e.decode_id(r)
    print(r, d)
