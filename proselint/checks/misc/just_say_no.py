# -*- coding: utf-8 -*-
"""Avoid hedge words.

---
layout:     post
source:     Just Say No Linter
source_url: https://github.com/lexicalunit/linter-just-say-no
title:      avoid hedge words
date:       2016-9-16 12:31:19
categories: writing
---

Points out possible hedge words.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Check the text."""
    err = "misc.just_say_no"
    msg = "Possible hedge word. Avoid '{}'."

    hedge = [
      "a bit",
      "a little",
      "a tad",
      "a touch",
      "almost",
      "apologize",
      "apparently",
      "appears",
      "around",
      "basically",
      "bother",
      "could",
      "does that make sense",
      "effectively",
      "evidently",
      "fairly",
      "generally",
      "hardly",
      "hopefully",
      "I am about",
      "I think",
      "I will try",
      "I'll try",
      "I'm about",
      "I'm just trying",
      "I'm no expert",
      "I'm not an expert",
      "I'm trying",
      "in general",
      "just about",
      "just",
      "kind of",
      "largely",
      "likely",
      "mainly",
      "may",
      "maybe",
      "might",
      "more or less",
      "mostly",
      "nearly",
      "overall",
      "partially",
      "partly",
      "perhaps",
      "possibly",
      "presumably",
      "pretty",
      "probably",
      "quite clearly",
      "quite",
      "rather",
      "really quite",
      "really",
      "seem",
      "seemed",
      "seems",
      "some",
      "sometimes",
      "somewhat",
      "sorry",
      "sort of",
      "suppose",
      "supposedly",
      "think",
    ]

    return existence_check(text, hedge, err, msg, join=True)
