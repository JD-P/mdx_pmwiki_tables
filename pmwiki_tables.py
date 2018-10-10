from markdown.inlinepatterns import InlineProcessor
from markdown.util import etree

TABLE_PATTERN = r'\|\| (.+=\"?.+\"?[\n ])+|(?:\|\|! ([^\|]*))|(?:\|\| ([^\|]*))'

class TablePattern(InlineProcessor):
    def handleMatch(self, m, data):
        if m.string.startswith("||") and not m.string.strip().endswith("||"):
            # The escaping and sanitization logic here is a pain so I'll do it
            # later
            table = etree.Element('table')
            return table, m.start(0), m.end(0)
        if m.string.startswith("||!"):
            # Match a table header
            th = etree.Element('th')
            th.text = m.group().split()[1]
            return th
        else:
            pass
        
