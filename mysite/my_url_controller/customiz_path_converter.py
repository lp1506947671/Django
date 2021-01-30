#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CusPatCon:

    regex = r"[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "40d%s" % value
