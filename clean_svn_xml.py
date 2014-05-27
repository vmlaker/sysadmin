"""
Clean XML file of illegal characters.

Usage:  python clean_svn_xml.py <input_file> <output_file>

""" 

import sys
import re

# Strip illegal characters out of XML.
#
# As per Leo Simons' article:
#   http://lsimons.wordpress.com/2011/03/17/
#            stripping-illegal-characters-out-of-xml-in-python
#
_illegal_xml_chars_RE = re.compile(
    u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')
def escape(val, replacement='?'):
    """Return escaped string."""
    return _illegal_xml_chars_RE.sub(replacement, val)

# Open the XML file, read, escape and write.
with open(sys.argv[1], 'r') as f:
    i = f.read()
    j = escape(i)
    with open(sys.argv[2], 'w') as g:
        g.write(j)
