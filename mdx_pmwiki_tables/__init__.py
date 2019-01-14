from .pmwiki_tables import PmWikiTables

def makeExtension(**kwargs):
    return PmWikiTables(**kwargs)
