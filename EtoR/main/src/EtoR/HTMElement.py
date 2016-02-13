#!/usr/bin/env python
# -*- coding: utf-8 -*-

class El:
    """this class give a simplified representation of an html element"""


    @classmethod
    def enableStyle(self, style):
        El.printStyle = style

    def __init__(self, name, content="", refs=None):
        self.b = name
        self.v = []
        if(refs is None):
            refs = {}
        self.refs = refs
        self.v.append(content)

    def __str__(self):
        """
        A str representation of the html element
        :return: All values surrounded by tags
        """
        ret = "<" + self.b
        ret += self.attrToString()
        return ret + ">" + self.getValue() + "</" + self.b + ">"

    def attrToString(self):
        """
        String representation of the current attributes
        :return: ref="val" pairs of attributes
        """
        ret = ""
        for k,v in self.refs.items():
            ret += " " + k + '="'+ v + '"'
        return ret

    def insert(self, element):
        self.v.append(element)

    def getValue(self):
        """ Assembling all elements into a single string chain """
        ret = ""
        for v in self.v:
            ret += str(v)
        return ret

    def attr(self, ref, val):
        """
        Adds a value to a specified references
        There is no consistency check
        You can add as many attributes as you want to any refs
        :param ref: the reference to append ex : href
        :param val: the value to be associated with the reference ex : "www.perdu.com"
        """
        if not El.printStyle and ref == "style": return

        if(ref in self.refs): self.refs[ref] = self.refs[ref] + " " + val
        else : self.refs[ref] = val


