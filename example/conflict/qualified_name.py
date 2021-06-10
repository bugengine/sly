import sys
sys.path.insert(0, '../..')

import sly

class QualNameLexer(sly.Lexer):
    tokens = [
        "identifier",
    ]
    literals = { '::', ',' }

class QualNameParser(sly.Parser):
    tokens = QualNameLexer.tokens
    debugfile = "qualified_name.out"
    dotfile = "qualified_name.dot"


    @_("prog comma_opt id_expression")
    @_("id_expression")
    def prog(self, p):
        pass

    @_("qualified_id")
    @_("unqualified_id")
    def id_expression(self, p):
        pass

    @_("template_opt identifier")
    def unqualified_id(self, p):
        pass

    @_("'template'")
    @_("")
    def template_opt(self, p):
        pass

    @_("nested_name_specifier unqualified_id")
    @_("'::' nested_name_specifier unqualified_id")
    def qualified_id(self, p):
        pass

    @_("','")
    @_("")
    def comma_opt(self, p):
        pass

    @_("template_opt identifier '::'")
    def nested_name_specifier(self, p):
        pass


