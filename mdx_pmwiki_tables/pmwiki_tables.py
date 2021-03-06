from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import etree

TABLE_PATTERN = r'\|\| ?([^\|]+=\"?.+\"?)*\n(?:\|\|! ?(.*) ?\|\|!\n)?(?:\|\| ?(.*) ?\|\|)+'

class PmWikiTables(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(TablePattern(TABLE_PATTERN), "pmwiki_tables",
                                   20)

class TablePattern(InlineProcessor):
    def handleMatch(self, m, data):
        # The escaping and sanitization logic here is a pain so I'll do it
        # later
        lines = m.string.splitlines()
        table = etree.Element('table')
        thead = etree.SubElement(table, "thead")
        if lines[1].startswith("||!"):
            column_heads = [head.strip() for head in lines[1].split("||!") if head]
            for head in column_heads:
                th = etree.SubElement(thead, "th")
                th.text = head
        tbody = etree.SubElement(table, "tbody")
        rows_start = 2 if lines[1].startswith("||!") else 1
        for line in lines[rows_start:]:
            tr = etree.SubElement(tbody, 'tr')
            for data in m.groups()[2].split("||"):
                td = etree.SubElement(tr, "td")
                td.text = data.strip()
        return table, m.start(0), m.end(0)
        
