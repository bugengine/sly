import sys
sys.path.insert(0, '../..')

import sly

class CxxLexer(sly.Lexer):
    tokens = [
        "floating-literal",
        "identifier",
        "integer-literal",
        "string-literal",
    ]
    literals = {
        ")",
        "}",
        "]",
        "(",
        "{",
        "[",
        "...",
        ":",
        ";",
        ".",
        ",",
        "::",
        "?",
        ".*",
        "->*",
        "->",
        "--",
        "++",
        "^=",
        "|=",
        "&=",
        ">>=",
        "<<=",
        "-=",
        "+=",
        "%=",
        "/=",
        "*=",
        "=",
        "!=",
        "==",
        ">=",
        "<=",
        ">",
        "<",
        "!",
        "&&",
        "||",
        ">>",
        "<<",
        "^",
        "~",
        "&",
        "|",
        "%",
        "/",
        "*",
        "-",
        "+",
        "",
        "<[",
        "]>",
        "doxycomment",
        "asm",
        "auto",
        "bool",
        "break",
        "case",
        "catch",
        "char",
        "class",
        "const",
        "const_cast",
        "continue",
        "default",
        "delete",
        "do",
        "double",
        "dynamic_cast",
        "else",
        "enum",
        "explicit",
        "extern",
        "false",
        "float",
        "for",
        "friend",
        "goto",
        "if",
        "inline",
        "int",
        "long",
        "mutable",
        "namespace",
        "new",
        "operator",
        "private",
        "protected",
        "public",
        "register",
        "reinterpret_cast",
        "return",
        "short",
        "signed",
        "sizeof",
        "static",
        "static_cast",
        "struct",
        "switch",
        "template",
        "this",
        "throw",
        "true",
        "try",
        "typedef",
        "typeid",
        "typename",
        "union",
        "unsigned",
        "using",
        "virtual",
        "void",
        "volatile",
        "wchar_t",
        "while",
        "u8",
        "u16",
        "u32",
        "u64",
        "i8",
        "i16",
        "i32",
        "i64",
        "published",
        "final",
        "override",
    }

class CxxParser(sly.Parser):
    tokens = CxxLexer.tokens
    debugfile = "cxxparser.out"
    start = 'translation_unit'

    @_('ptr_abstract_declarator')
    def abstract_declarator(self, p):
        pass

    @_('"private"')
    def access_specifier(self, p):
        pass

    @_('"protected"')
    def access_specifier(self, p):
        pass

    @_('"public"')
    def access_specifier(self, p):
        pass

    @_('"published"')
    def access_specifier(self, p):
        pass

    @_('additive_expression "-" multiplicative_expression')
    def additive_expression(self, p):
        pass

    @_('additive_expression "+" multiplicative_expression')
    def additive_expression(self, p):
        pass

    @_('multiplicative_expression')
    def additive_expression(self, p):
        pass

    @_('and_expression "&" equality_expression')
    def and_expression(self, p):
        pass

    @_('equality_expression')
    def and_expression(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "asm" "(" "string-literal" ")" ";"')
    def asm_definition(self, p):
        pass

    @_('decl_specifier_seq "asm" "(" "string-literal" ")" ";"')
    def asm_definition(self, p):
        pass

    @_('attribute_specifier_seq "asm" "(" "string-literal" ")" ";"')
    def asm_definition(self, p):
        pass

    @_('"asm" "(" "string-literal" ")" ";"')
    def asm_definition(self, p):
        pass

    @_('throw_expression')
    def assignment_expression(self, p):
        pass

    @_('logical_or_expression assignment_operator initializer_clause')
    def assignment_expression(self, p):
        pass

    @_('conditional_expression')
    def assignment_expression(self, p):
        pass

    @_('"|="')
    def assignment_operator(self, p):
        pass

    @_('"^="')
    def assignment_operator(self, p):
        pass

    @_('"&="')
    def assignment_operator(self, p):
        pass

    @_('"<<="')
    def assignment_operator(self, p):
        pass

    @_('">>="')
    def assignment_operator(self, p):
        pass

    @_('"-="')
    def assignment_operator(self, p):
        pass

    @_('"+="')
    def assignment_operator(self, p):
        pass

    @_('"%="')
    def assignment_operator(self, p):
        pass

    @_('"/="')
    def assignment_operator(self, p):
        pass

    @_('"*="')
    def assignment_operator(self, p):
        pass

    @_('"="')
    def assignment_operator(self, p):
        pass

    @_('attribute_specifier_seq ";"')
    def attribute_declaration(self, p):
        pass

    @_('"doxycomment"')
    def attribute_specifier(self, p):
        pass

    @_('attribute_specifier_seq attribute_specifier')
    def attribute_specifier_seq(self, p):
        pass

    @_('attribute_specifier')
    def attribute_specifier_seq(self, p):
        pass

    @_('":" base_specifier_list')
    def base_clause(self, p):
        pass

    @_('attribute_specifier_seq access_specifier "virtual" base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('access_specifier "virtual" base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('attribute_specifier_seq access_specifier base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('access_specifier base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('attribute_specifier_seq "virtual" access_specifier base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('"virtual" access_specifier base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('attribute_specifier_seq "virtual" base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('"virtual" base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('attribute_specifier_seq base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('base_type_specifier')
    def base_specifier(self, p):
        pass

    @_('base_specifier_list "," base_specifier')
    def base_specifier_list(self, p):
        pass

    @_('base_specifier')
    def base_specifier_list(self, p):
        pass

    @_('class_or_decltype')
    def base_type_specifier(self, p):
        pass

    @_('using_directive')
    def block_declaration(self, p):
        pass

    @_('using_declaration')
    def block_declaration(self, p):
        pass

    @_('namespace_alias_definition')
    def block_declaration(self, p):
        pass

    @_('asm_definition')
    def block_declaration(self, p):
        pass

    @_('simple_declaration')
    def block_declaration(self, p):
        pass

    @_('"=" initializer_clause')
    def brace_or_equal_initializer(self, p):
        pass

    @_('"void"')
    def builtin_type_specifier(self, p):
        pass

    @_('"float"')
    def builtin_type_specifier(self, p):
        pass

    @_('"double"')
    def builtin_type_specifier(self, p):
        pass

    @_('"signed"')
    def builtin_type_specifier(self, p):
        pass

    @_('"unsigned"')
    def builtin_type_specifier(self, p):
        pass

    @_('"char"')
    def builtin_type_specifier(self, p):
        pass

    @_('"wchar_t"')
    def builtin_type_specifier(self, p):
        pass

    @_('"bool"')
    def builtin_type_specifier(self, p):
        pass

    @_('"short"')
    def builtin_type_specifier(self, p):
        pass

    @_('"int"')
    def builtin_type_specifier(self, p):
        pass

    @_('"long"')
    def builtin_type_specifier(self, p):
        pass

    @_('"i8"')
    def builtin_type_specifier(self, p):
        pass

    @_('"i16"')
    def builtin_type_specifier(self, p):
        pass

    @_('"i32"')
    def builtin_type_specifier(self, p):
        pass

    @_('"i64"')
    def builtin_type_specifier(self, p):
        pass

    @_('"u8"')
    def builtin_type_specifier(self, p):
        pass

    @_('"u16"')
    def builtin_type_specifier(self, p):
        pass

    @_('"u32"')
    def builtin_type_specifier(self, p):
        pass

    @_('"u64"')
    def builtin_type_specifier(self, p):
        pass

    @_('"(" type_id ")" cast_expression')
    def cast_expression(self, p):
        pass

    @_('unary_expression')
    def cast_expression(self, p):
        pass

    @_('class_key attribute_specifier_seq base_clause')
    def class_head(self, p):
        pass

    @_('class_key base_clause')
    def class_head(self, p):
        pass

    @_('class_key attribute_specifier_seq')
    def class_head(self, p):
        pass

    @_('class_key')
    def class_head(self, p):
        pass

    @_('class_key attribute_specifier_seq id_type class_virt_specifier_seq base_clause')
    def class_head(self, p):
        pass

    @_('class_key id_type class_virt_specifier_seq base_clause')
    def class_head(self, p):
        pass

    @_('class_key attribute_specifier_seq id_type class_virt_specifier_seq')
    def class_head(self, p):
        pass

    @_('class_key id_type class_virt_specifier_seq')
    def class_head(self, p):
        pass

    @_('"class"')
    def class_key(self, p):
        pass

    @_('"struct"')
    def class_key(self, p):
        pass

    @_('"union"')
    def class_key(self, p):
        pass

    @_('id_type')
    def class_or_decltype(self, p):
        pass

    @_('class_head "{" member_specification "}"')
    def class_specifier(self, p):
        pass

    @_('class_head "{" "}"')
    def class_specifier(self, p):
        pass

    @_('')
    def class_virt_specifier_seq(self, p):
        pass

    @_('"{" statement_seq "}"')
    def compound_statement(self, p):
        pass

    @_('"{" "}"')
    def compound_statement(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq declarator "=" initializer_clause')
    def condition(self, p):
        pass

    @_('decl_specifier_seq declarator "=" initializer_clause')
    def condition(self, p):
        pass

    @_('expression')
    def condition(self, p):
        pass

    @_('logical_or_expression "?" expression ":" assignment_expression')
    def conditional_expression(self, p):
        pass

    @_('logical_or_expression')
    def conditional_expression(self, p):
        pass

    @_('conditional_expression')
    def constant_expression(self, p):
        pass

    @_('ptr_operator conversion_declarator')
    def conversion_declarator(self, p):
        pass

    @_('ptr_operator')
    def conversion_declarator(self, p):
        pass

    @_('"operator" conversion_type_id')
    def conversion_function_id(self, p):
        pass

    @_('type_specifier_seq conversion_declarator')
    def conversion_type_id(self, p):
        pass

    @_('type_specifier_seq')
    def conversion_type_id(self, p):
        pass

    @_('":" mem_initializer_list')
    def ctor_initializer(self, p):
        pass

    @_('"const"')
    def cv_qualifier(self, p):
        pass

    @_('"volatile"')
    def cv_qualifier(self, p):
        pass

    @_('cv_qualifier')
    def cv_qualifier_seq(self, p):
        pass

    @_('cv_qualifier cv_qualifier_seq')
    def cv_qualifier_seq(self, p):
        pass

    @_('storage_class_specifier')
    def decl_specifier(self, p):
        pass

    @_('type_specifier')
    def decl_specifier(self, p):
        pass

    @_('function_specifier')
    def decl_specifier(self, p):
        pass

    @_('"friend"')
    def decl_specifier(self, p):
        pass

    @_('"typedef"')
    def decl_specifier(self, p):
        pass

    @_('decl_specifier decl_specifier_seq')
    def decl_specifier_seq(self, p):
        pass

    @_('decl_specifier attribute_specifier_seq')
    def decl_specifier_seq(self, p):
        pass

    @_('decl_specifier')
    def decl_specifier_seq(self, p):
        pass

    @_('attribute_declaration')
    def declaration(self, p):
        pass

    @_('empty_declaration')
    def declaration(self, p):
        pass

    @_('namespace_definition')
    def declaration(self, p):
        pass

    @_('linkage_specification')
    def declaration(self, p):
        pass

    @_('explicit_specialization')
    def declaration(self, p):
        pass

    @_('explicit_instantiation')
    def declaration(self, p):
        pass

    @_('template_declaration')
    def declaration(self, p):
        pass

    @_('function_definition')
    def declaration(self, p):
        pass

    @_('block_declaration')
    def declaration(self, p):
        pass

    @_('declaration_seq declaration')
    def declaration_seq(self, p):
        pass

    @_('declaration')
    def declaration_seq(self, p):
        pass

    @_('block_declaration')
    def declaration_statement(self, p):
        pass

    @_('ptr_declarator')
    def declarator(self, p):
        pass

    @_('id_expression')
    def declarator_id(self, p):
        pass

    @_('id_type')
    def declarator_id(self, p):
        pass

    @_('"::" "delete" "[" "]" cast_expression')
    def delete_expression(self, p):
        pass

    @_('"delete" "[" "]" cast_expression')
    def delete_expression(self, p):
        pass

    @_('"::" "delete" cast_expression')
    def delete_expression(self, p):
        pass

    @_('"delete" cast_expression')
    def delete_expression(self, p):
        pass

    @_('"throw" "(" type_id_list ")"')
    def dynamic_exception_specification(self, p):
        pass

    @_('"throw" "(" ")"')
    def dynamic_exception_specification(self, p):
        pass

    @_('enum_key id_type')
    def elaborated_type_specifier(self, p):
        pass

    @_('class_key attribute_specifier_seq id_type')
    def elaborated_type_specifier(self, p):
        pass

    @_('class_key id_type')
    def elaborated_type_specifier(self, p):
        pass

    @_('";"')
    def empty_declaration(self, p):
        pass

    @_('')
    def enum_base(self, p):
        pass

    @_('enum_key attribute_specifier_seq id_type enum_base')
    def enum_head(self, p):
        pass

    @_('enum_key id_type enum_base')
    def enum_head(self, p):
        pass

    @_('enum_key attribute_specifier_seq enum_base')
    def enum_head(self, p):
        pass

    @_('enum_key enum_base')
    def enum_head(self, p):
        pass

    @_('"enum"')
    def enum_key(self, p):
        pass

    @_('enum_head "{" enumerator_list "," "}"')
    def enum_specifier(self, p):
        pass

    @_('enum_head "{" enumerator_list "}"')
    def enum_specifier(self, p):
        pass

    @_('enum_head "{" "}"')
    def enum_specifier(self, p):
        pass

    @_('"identifier"')
    def enumerator(self, p):
        pass

    @_('enumerator')
    def enumerator_definition(self, p):
        pass

    @_('enumerator "=" constant_expression')
    def enumerator_definition(self, p):
        pass

    @_('enumerator_definition')
    def enumerator_list(self, p):
        pass

    @_('enumerator_list "," enumerator_definition')
    def enumerator_list(self, p):
        pass

    @_('equality_expression "!=" relational_expression')
    def equality_expression(self, p):
        pass

    @_('equality_expression "==" relational_expression')
    def equality_expression(self, p):
        pass

    @_('relational_expression')
    def equality_expression(self, p):
        pass

    @_('"..."')
    def exception_declaration(self, p):
        pass

    @_('attribute_specifier_seq type_specifier_seq abstract_declarator')
    def exception_declaration(self, p):
        pass

    @_('type_specifier_seq abstract_declarator')
    def exception_declaration(self, p):
        pass

    @_('attribute_specifier_seq type_specifier_seq')
    def exception_declaration(self, p):
        pass

    @_('type_specifier_seq')
    def exception_declaration(self, p):
        pass

    @_('attribute_specifier_seq type_specifier_seq declarator')
    def exception_declaration(self, p):
        pass

    @_('type_specifier_seq declarator')
    def exception_declaration(self, p):
        pass

    @_('dynamic_exception_specification')
    def exception_specification(self, p):
        pass

    @_('exclusive_or_expression "^" and_expression')
    def exclusive_or_expression(self, p):
        pass

    @_('and_expression')
    def exclusive_or_expression(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "template" declaration')
    def explicit_instantiation(self, p):
        pass

    @_('decl_specifier_seq "template" declaration')
    def explicit_instantiation(self, p):
        pass

    @_('attribute_specifier_seq "template" declaration')
    def explicit_instantiation(self, p):
        pass

    @_('"template" declaration')
    def explicit_instantiation(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "template" "<[" "]>" declaration')
    def explicit_specialization(self, p):
        pass

    @_('decl_specifier_seq "template" "<[" "]>" declaration')
    def explicit_specialization(self, p):
        pass

    @_('attribute_specifier_seq "template" "<[" "]>" declaration')
    def explicit_specialization(self, p):
        pass

    @_('"template" "<[" "]>" declaration')
    def explicit_specialization(self, p):
        pass

    @_('expression "," assignment_expression')
    def expression(self, p):
        pass

    @_('assignment_expression')
    def expression(self, p):
        pass

    @_('initializer_list')
    def expression_list(self, p):
        pass

    @_('expression ";"')
    def expression_statement(self, p):
        pass

    @_('expression_statement')
    def for_init_statement(self, p):
        pass

    @_('simple_declaration')
    def for_init_statement(self, p):
        pass

    @_('ctor_initializer compound_statement')
    def function_body(self, p):
        pass

    @_('compound_statement')
    def function_body(self, p):
        pass

    @_('function_try_block')
    def function_body(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq declarator function_body')
    def function_definition(self, p):
        pass

    @_('decl_specifier_seq declarator function_body')
    def function_definition(self, p):
        pass

    @_('attribute_specifier_seq declarator function_body')
    def function_definition(self, p):
        pass

    @_('declarator function_body')
    def function_definition(self, p):
        pass

    @_('"inline"')
    def function_specifier(self, p):
        pass

    @_('"virtual"')
    def function_specifier(self, p):
        pass

    @_('"explicit"')
    def function_specifier(self, p):
        pass

    @_('"try" ctor_initializer compound_statement handler_seq')
    def function_try_block(self, p):
        pass

    @_('"try" compound_statement handler_seq')
    def function_try_block(self, p):
        pass

    @_('"catch" "(" exception_declaration ")" compound_statement')
    def handler(self, p):
        pass

    @_('handler')
    def handler_seq(self, p):
        pass

    @_('handler handler_seq')
    def handler_seq(self, p):
        pass

    @_('unqualified_expression_id')
    def id_expression(self, p):
        pass

    @_('qualified_expression_id')
    def id_expression(self, p):
        pass

    @_('unqualified_type_id')
    def id_type(self, p):
        pass

    @_('qualified_type_id')
    def id_type(self, p):
        pass

    @_('inclusive_or_expression "|" exclusive_or_expression')
    def inclusive_or_expression(self, p):
        pass

    @_('exclusive_or_expression')
    def inclusive_or_expression(self, p):
        pass

    @_('declarator initializer')
    def init_declarator(self, p):
        pass

    @_('declarator')
    def init_declarator(self, p):
        pass

    @_('init_declarator')
    def init_declarator_list(self, p):
        pass

    @_('init_declarator_list "," init_declarator')
    def init_declarator_list(self, p):
        pass

    @_('"(" expression_list ")"')
    def initializer(self, p):
        pass

    @_('brace_or_equal_initializer')
    def initializer(self, p):
        pass

    @_('assignment_expression')
    def initializer_clause(self, p):
        pass

    @_('initializer_list "," initializer_clause')
    def initializer_list(self, p):
        pass

    @_('initializer_clause')
    def initializer_list(self, p):
        pass

    @_('"for" "(" for_init_statement condition ";" expression ")" statement')
    def iteration_statement(self, p):
        pass

    @_('"for" "(" for_init_statement ";" expression ")" statement')
    def iteration_statement(self, p):
        pass

    @_('"for" "(" for_init_statement condition ";" ")" statement')
    def iteration_statement(self, p):
        pass

    @_('"for" "(" for_init_statement ";" ")" statement')
    def iteration_statement(self, p):
        pass

    @_('"do" statement "while" "(" expression ")" ";"')
    def iteration_statement(self, p):
        pass

    @_('"while" "(" condition ")" statement')
    def iteration_statement(self, p):
        pass

    @_('"break" ";"')
    def jump_statement(self, p):
        pass

    @_('"continue" ";"')
    def jump_statement(self, p):
        pass

    @_('"return" expression ";"')
    def jump_statement(self, p):
        pass

    @_('"return" ";"')
    def jump_statement(self, p):
        pass

    @_('"goto" "identifier" ";"')
    def jump_statement(self, p):
        pass

    @_('attribute_specifier_seq "default" ":" statement')
    def labeled_statement(self, p):
        pass

    @_('"default" ":" statement')
    def labeled_statement(self, p):
        pass

    @_('attribute_specifier_seq "case" constant_expression ":" statement')
    def labeled_statement(self, p):
        pass

    @_('"case" constant_expression ":" statement')
    def labeled_statement(self, p):
        pass

    @_('attribute_specifier_seq "identifier" ":" statement')
    def labeled_statement(self, p):
        pass

    @_('"identifier" ":" statement')
    def labeled_statement(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "string-literal" "{" declaration_seq "}"')
    def linkage_specification(self, p):
        pass

    @_('decl_specifier_seq "string-literal" "{" declaration_seq "}"')
    def linkage_specification(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "string-literal" "{" "}"')
    def linkage_specification(self, p):
        pass

    @_('decl_specifier_seq "string-literal" "{" "}"')
    def linkage_specification(self, p):
        pass

    @_('"floating-literal"')
    def literal(self, p):
        pass

    @_('"integer-literal"')
    def literal(self, p):
        pass

    @_('"string-literal"')
    def literal(self, p):
        pass

    @_('logical_and_expression "&&" inclusive_or_expression')
    def logical_and_expression(self, p):
        pass

    @_('inclusive_or_expression')
    def logical_and_expression(self, p):
        pass

    @_('logical_or_expression "||" logical_and_expression')
    def logical_or_expression(self, p):
        pass

    @_('logical_and_expression')
    def logical_or_expression(self, p):
        pass

    @_('mem_initializer_id "(" expression_list ")"')
    def mem_initializer(self, p):
        pass

    @_('mem_initializer_id "(" ")"')
    def mem_initializer(self, p):
        pass

    @_('class_or_decltype')
    def mem_initializer_id(self, p):
        pass

    @_('mem_initializer "," mem_initializer_list')
    def mem_initializer_list(self, p):
        pass

    @_('mem_initializer')
    def mem_initializer_list(self, p):
        pass

    @_('template_declaration')
    def member_declaration(self, p):
        pass

    @_('using_declaration')
    def member_declaration(self, p):
        pass

    @_('function_definition ";"')
    def member_declaration(self, p):
        pass

    @_('function_definition')
    def member_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq member_declarator_list ";"')
    def member_declaration(self, p):
        pass

    @_('decl_specifier_seq member_declarator_list ";"')
    def member_declaration(self, p):
        pass

    @_('attribute_specifier_seq member_declarator_list ";"')
    def member_declaration(self, p):
        pass

    @_('member_declarator_list ";"')
    def member_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq ";"')
    def member_declaration(self, p):
        pass

    @_('decl_specifier_seq ";"')
    def member_declaration(self, p):
        pass

    @_('attribute_specifier_seq ";"')
    def member_declaration(self, p):
        pass

    @_('";"')
    def member_declaration(self, p):
        pass

    @_('"identifier" attribute_specifier_seq ":" constant_expression')
    def member_declarator(self, p):
        pass

    @_('attribute_specifier_seq ":" constant_expression')
    def member_declarator(self, p):
        pass

    @_('"identifier" ":" constant_expression')
    def member_declarator(self, p):
        pass

    @_('":" constant_expression')
    def member_declarator(self, p):
        pass

    @_('declarator pure_specifier')
    def member_declarator(self, p):
        pass

    @_('declarator')
    def member_declarator(self, p):
        pass

    @_('member_declarator_list "," member_declarator')
    def member_declarator_list(self, p):
        pass

    @_('member_declarator')
    def member_declarator_list(self, p):
        pass

    @_('access_specifier ":" member_specification')
    def member_specification(self, p):
        pass

    @_('access_specifier ":"')
    def member_specification(self, p):
        pass

    @_('member_declaration member_specification')
    def member_specification(self, p):
        pass

    @_('member_declaration')
    def member_specification(self, p):
        pass

    @_('multiplicative_expression "%" pm_expression')
    def multiplicative_expression(self, p):
        pass

    @_('multiplicative_expression "/" pm_expression')
    def multiplicative_expression(self, p):
        pass

    @_('multiplicative_expression "*" pm_expression')
    def multiplicative_expression(self, p):
        pass

    @_('pm_expression')
    def multiplicative_expression(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "namespace" "identifier" "=" id_type ";"')
    def namespace_alias_definition(self, p):
        pass

    @_('decl_specifier_seq "namespace" "identifier" "=" id_type ";"')
    def namespace_alias_definition(self, p):
        pass

    @_('attribute_specifier_seq "namespace" "identifier" "=" id_type ";"')
    def namespace_alias_definition(self, p):
        pass

    @_('"namespace" "identifier" "=" id_type ";"')
    def namespace_alias_definition(self, p):
        pass

    @_('declaration_seq')
    def namespace_body(self, p):
        pass

    @_('')
    def namespace_body(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "namespace" id_type "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('decl_specifier_seq "namespace" id_type "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('attribute_specifier_seq "namespace" id_type "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('"namespace" id_type "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "namespace" "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('decl_specifier_seq "namespace" "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('attribute_specifier_seq "namespace" "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('"namespace" "{" namespace_body "}"')
    def namespace_definition(self, p):
        pass

    @_('nested_name_specifier "template" "identifier" template_spec "::"')
    def nested_name_specifier(self, p):
        pass

    @_('nested_name_specifier "identifier" template_spec "::"')
    def nested_name_specifier(self, p):
        pass

    @_('nested_name_specifier "template" "identifier" "::"')
    def nested_name_specifier(self, p):
        pass

    @_('nested_name_specifier "identifier" "::"')
    def nested_name_specifier(self, p):
        pass

    @_('"identifier" template_spec "::"')
    def nested_name_specifier(self, p):
        pass

    @_('"identifier" "::"')
    def nested_name_specifier(self, p):
        pass

    @_('noptr_new_declarator')
    def new_declarator(self, p):
        pass

    @_('ptr_operator new_declarator')
    def new_declarator(self, p):
        pass

    @_('ptr_operator')
    def new_declarator(self, p):
        pass

    @_('"::" "new" new_placement "(" type_id ")" new_initializer')
    def new_expression(self, p):
        pass

    @_('"new" new_placement "(" type_id ")" new_initializer')
    def new_expression(self, p):
        pass

    @_('"::" "new" "(" type_id ")" new_initializer')
    def new_expression(self, p):
        pass

    @_('"new" "(" type_id ")" new_initializer')
    def new_expression(self, p):
        pass

    @_('"::" "new" new_placement "(" type_id ")"')
    def new_expression(self, p):
        pass

    @_('"new" new_placement "(" type_id ")"')
    def new_expression(self, p):
        pass

    @_('"::" "new" "(" type_id ")"')
    def new_expression(self, p):
        pass

    @_('"new" "(" type_id ")"')
    def new_expression(self, p):
        pass

    @_('"::" "new" new_placement new_type_id new_initializer')
    def new_expression(self, p):
        pass

    @_('"new" new_placement new_type_id new_initializer')
    def new_expression(self, p):
        pass

    @_('"::" "new" new_type_id new_initializer')
    def new_expression(self, p):
        pass

    @_('"new" new_type_id new_initializer')
    def new_expression(self, p):
        pass

    @_('"::" "new" new_placement new_type_id')
    def new_expression(self, p):
        pass

    @_('"new" new_placement new_type_id')
    def new_expression(self, p):
        pass

    @_('"::" "new" new_type_id')
    def new_expression(self, p):
        pass

    @_('"new" new_type_id')
    def new_expression(self, p):
        pass

    @_('"(" expression_list ")"')
    def new_initializer(self, p):
        pass

    @_('"(" ")"')
    def new_initializer(self, p):
        pass

    @_('"(" expression_list ")"')
    def new_placement(self, p):
        pass

    @_('type_specifier_seq new_declarator')
    def new_type_id(self, p):
        pass

    @_('type_specifier_seq')
    def new_type_id(self, p):
        pass

    @_('"(" ptr_abstract_declarator ")"')
    def noptr_abstract_declarator(self, p):
        pass

    @_('noptr_abstract_declarator "[" constant_expression "]" attribute_specifier_seq')
    def noptr_abstract_declarator(self, p):
        pass

    @_('"[" constant_expression "]" attribute_specifier_seq')
    def noptr_abstract_declarator(self, p):
        pass

    @_('noptr_abstract_declarator "[" constant_expression "]"')
    def noptr_abstract_declarator(self, p):
        pass

    @_('"[" constant_expression "]"')
    def noptr_abstract_declarator(self, p):
        pass

    @_('noptr_abstract_declarator parameters_and_qualifiers')
    def noptr_abstract_declarator(self, p):
        pass

    @_('parameters_and_qualifiers')
    def noptr_abstract_declarator(self, p):
        pass

    @_('"(" ptr_declarator ")"')
    def noptr_declarator(self, p):
        pass

    @_('noptr_declarator "[" constant_expression "]" attribute_specifier_seq')
    def noptr_declarator(self, p):
        pass

    @_('noptr_declarator "[" "]" attribute_specifier_seq')
    def noptr_declarator(self, p):
        pass

    @_('noptr_declarator "[" constant_expression "]"')
    def noptr_declarator(self, p):
        pass

    @_('noptr_declarator "[" "]"')
    def noptr_declarator(self, p):
        pass

    @_('noptr_declarator parameters_and_qualifiers')
    def noptr_declarator(self, p):
        pass

    @_('declarator_id attribute_specifier_seq')
    def noptr_declarator(self, p):
        pass

    @_('declarator_id')
    def noptr_declarator(self, p):
        pass

    @_('noptr_new_declarator "[" constant_expression "]" attribute_specifier_seq')
    def noptr_new_declarator(self, p):
        pass

    @_('noptr_new_declarator "[" constant_expression "]"')
    def noptr_new_declarator(self, p):
        pass

    @_('"[" expression "]" attribute_specifier_seq')
    def noptr_new_declarator(self, p):
        pass

    @_('"[" expression "]"')
    def noptr_new_declarator(self, p):
        pass

    @_('"operator" overloadable_operator')
    def operator_function_id(self, p):
        pass

    @_('"[" "]"')
    def overloadable_operator(self, p):
        pass

    @_('"(" ")"')
    def overloadable_operator(self, p):
        pass

    @_('"->"')
    def overloadable_operator(self, p):
        pass

    @_('"->*"')
    def overloadable_operator(self, p):
        pass

    @_('","')
    def overloadable_operator(self, p):
        pass

    @_('"--"')
    def overloadable_operator(self, p):
        pass

    @_('"++"')
    def overloadable_operator(self, p):
        pass

    @_('"||"')
    def overloadable_operator(self, p):
        pass

    @_('"&&"')
    def overloadable_operator(self, p):
        pass

    @_('">="')
    def overloadable_operator(self, p):
        pass

    @_('"<="')
    def overloadable_operator(self, p):
        pass

    @_('"!="')
    def overloadable_operator(self, p):
        pass

    @_('"=="')
    def overloadable_operator(self, p):
        pass

    @_('">>="')
    def overloadable_operator(self, p):
        pass

    @_('"<<="')
    def overloadable_operator(self, p):
        pass

    @_('">>"')
    def overloadable_operator(self, p):
        pass

    @_('"<<"')
    def overloadable_operator(self, p):
        pass

    @_('"|="')
    def overloadable_operator(self, p):
        pass

    @_('"&="')
    def overloadable_operator(self, p):
        pass

    @_('"^="')
    def overloadable_operator(self, p):
        pass

    @_('"%="')
    def overloadable_operator(self, p):
        pass

    @_('"/="')
    def overloadable_operator(self, p):
        pass

    @_('"*="')
    def overloadable_operator(self, p):
        pass

    @_('"-="')
    def overloadable_operator(self, p):
        pass

    @_('"+="')
    def overloadable_operator(self, p):
        pass

    @_('">"')
    def overloadable_operator(self, p):
        pass

    @_('"<"')
    def overloadable_operator(self, p):
        pass

    @_('"="')
    def overloadable_operator(self, p):
        pass

    @_('"!"')
    def overloadable_operator(self, p):
        pass

    @_('"~"')
    def overloadable_operator(self, p):
        pass

    @_('"|"')
    def overloadable_operator(self, p):
        pass

    @_('"&"')
    def overloadable_operator(self, p):
        pass

    @_('"^"')
    def overloadable_operator(self, p):
        pass

    @_('"%"')
    def overloadable_operator(self, p):
        pass

    @_('"/"')
    def overloadable_operator(self, p):
        pass

    @_('"*"')
    def overloadable_operator(self, p):
        pass

    @_('"-"')
    def overloadable_operator(self, p):
        pass

    @_('"+"')
    def overloadable_operator(self, p):
        pass

    @_('"delete" "[" "]"')
    def overloadable_operator(self, p):
        pass

    @_('"new" "[" "]"')
    def overloadable_operator(self, p):
        pass

    @_('"delete"')
    def overloadable_operator(self, p):
        pass

    @_('"new"')
    def overloadable_operator(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq abstract_declarator "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq abstract_declarator "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq abstract_declarator')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq abstract_declarator')
    def parameter_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq')
    def parameter_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq declarator "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq declarator "=" initializer_clause')
    def parameter_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq declarator')
    def parameter_declaration(self, p):
        pass

    @_('decl_specifier_seq declarator')
    def parameter_declaration(self, p):
        pass

    @_('parameter_declaration_list "," "..."')
    def parameter_declaration_clause(self, p):
        pass

    @_('parameter_declaration_list')
    def parameter_declaration_clause(self, p):
        pass

    @_('')
    def parameter_declaration_clause(self, p):
        pass

    @_('parameter_declaration_list "," parameter_declaration')
    def parameter_declaration_list(self, p):
        pass

    @_('parameter_declaration')
    def parameter_declaration_list(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" attribute_specifier_seq cv_qualifier_seq ref_qualifier exception_specification')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" cv_qualifier_seq ref_qualifier exception_specification')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" attribute_specifier_seq ref_qualifier exception_specification')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" ref_qualifier exception_specification')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" attribute_specifier_seq cv_qualifier_seq ref_qualifier')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" cv_qualifier_seq ref_qualifier')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" attribute_specifier_seq ref_qualifier')
    def parameters_and_qualifiers(self, p):
        pass

    @_('"(" parameter_declaration_clause ")" ref_qualifier')
    def parameters_and_qualifiers(self, p):
        pass

    @_('pm_expression "->*" cast_expression')
    def pm_expression(self, p):
        pass

    @_('pm_expression ".*" cast_expression')
    def pm_expression(self, p):
        pass

    @_('cast_expression')
    def pm_expression(self, p):
        pass

    @_('"typeid" "(" type_id ")"')
    def postfix_expression(self, p):
        pass

    @_('"typeid" "(" expression ")"')
    def postfix_expression(self, p):
        pass

    @_('"const_cast" "<[" type_id "]>" "(" expression ")"')
    def postfix_expression(self, p):
        pass

    @_('"reinterpret_cast" "<[" type_id "]>" "(" expression ")"')
    def postfix_expression(self, p):
        pass

    @_('"static_cast" "<[" type_id "]>" "(" expression ")"')
    def postfix_expression(self, p):
        pass

    @_('"dynamic_cast" "<[" type_id "]>" "(" expression ")"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "--"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "++"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "->" "template" id_expression')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "->" id_expression')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "." "template" id_expression')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "." id_expression')
    def postfix_expression(self, p):
        pass

    @_('typename_specifier "(" expression_list ")"')
    def postfix_expression(self, p):
        pass

    @_('typename_specifier "(" ")"')
    def postfix_expression(self, p):
        pass

    @_('simple_type_specifier "(" expression_list ")"')
    def postfix_expression(self, p):
        pass

    @_('simple_type_specifier "(" ")"')
    def postfix_expression(self, p):
        pass

    @_('builtin_type_specifier "(" expression_list ")"')
    def postfix_expression(self, p):
        pass

    @_('builtin_type_specifier "(" ")"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "(" expression_list ")"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "(" ")"')
    def postfix_expression(self, p):
        pass

    @_('postfix_expression "[" expression "]"')
    def postfix_expression(self, p):
        pass

    @_('primary_expression')
    def postfix_expression(self, p):
        pass

    @_('literal')
    def primary_expression(self, p):
        pass

    @_('"this"')
    def primary_expression(self, p):
        pass

    @_('"(" expression ")"')
    def primary_expression(self, p):
        pass

    @_('id_expression')
    def primary_expression(self, p):
        pass

    @_('"true"')
    def primary_expression(self, p):
        pass

    @_('"false"')
    def primary_expression(self, p):
        pass

    @_('ptr_operator ptr_abstract_declarator')
    def ptr_abstract_declarator(self, p):
        pass

    @_('ptr_operator')
    def ptr_abstract_declarator(self, p):
        pass

    @_('noptr_abstract_declarator')
    def ptr_abstract_declarator(self, p):
        pass

    @_('noptr_declarator')
    def ptr_declarator(self, p):
        pass

    @_('ptr_operator ptr_declarator')
    def ptr_declarator(self, p):
        pass

    @_('nested_name_specifier "*" cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('nested_name_specifier "*"')
    def ptr_operator(self, p):
        pass

    @_('"::" nested_name_specifier "*" cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"::" nested_name_specifier "*"')
    def ptr_operator(self, p):
        pass

    @_('nested_name_specifier "*" attribute_specifier_seq cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('nested_name_specifier "*" attribute_specifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"::" nested_name_specifier "*" attribute_specifier_seq cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"::" nested_name_specifier "*" attribute_specifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"&"')
    def ptr_operator(self, p):
        pass

    @_('"&" attribute_specifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"*" cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"*"')
    def ptr_operator(self, p):
        pass

    @_('"*" attribute_specifier_seq cv_qualifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"*" attribute_specifier_seq')
    def ptr_operator(self, p):
        pass

    @_('"=" "integer-literal"')
    def pure_specifier(self, p):
        pass

    @_('"::" operator_function_id template_spec')
    def qualified_expression_id(self, p):
        pass

    @_('"::" operator_function_id')
    def qualified_expression_id(self, p):
        pass

    @_('"::" nested_name_specifier "template" unqualified_expression_id')
    def qualified_expression_id(self, p):
        pass

    @_('"::" nested_name_specifier unqualified_expression_id')
    def qualified_expression_id(self, p):
        pass

    @_('nested_name_specifier "template" unqualified_expression_id')
    def qualified_expression_id(self, p):
        pass

    @_('nested_name_specifier unqualified_expression_id')
    def qualified_expression_id(self, p):
        pass

    @_('"::" "identifier" template_spec')
    def qualified_type_id(self, p):
        pass

    @_('"::" "identifier"')
    def qualified_type_id(self, p):
        pass

    @_('"::" nested_name_specifier "template" unqualified_type_id')
    def qualified_type_id(self, p):
        pass

    @_('"::" nested_name_specifier unqualified_type_id')
    def qualified_type_id(self, p):
        pass

    @_('nested_name_specifier "template" unqualified_type_id')
    def qualified_type_id(self, p):
        pass

    @_('nested_name_specifier unqualified_type_id')
    def qualified_type_id(self, p):
        pass

    @_('')
    def ref_qualifier(self, p):
        pass

    @_('relational_expression ">=" shift_expression')
    def relational_expression(self, p):
        pass

    @_('relational_expression "<=" shift_expression')
    def relational_expression(self, p):
        pass

    @_('relational_expression ">" shift_expression')
    def relational_expression(self, p):
        pass

    @_('relational_expression "<" shift_expression')
    def relational_expression(self, p):
        pass

    @_('shift_expression')
    def relational_expression(self, p):
        pass

    @_('"switch" "(" condition ")" statement')
    def selection_statement(self, p):
        pass

    @_('"if" "(" condition ")" statement "else" statement')
    def selection_statement(self, p):
        pass

    @_('"if" "(" condition ")" statement')
    def selection_statement(self, p):
        pass

    @_('shift_expression ">>" additive_expression')
    def shift_expression(self, p):
        pass

    @_('shift_expression "<<" additive_expression')
    def shift_expression(self, p):
        pass

    @_('additive_expression')
    def shift_expression(self, p):
        pass

    @_('attribute_specifier_seq init_declarator ";"')
    def simple_declaration(self, p):
        pass

    @_('init_declarator ";"')
    def simple_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq init_declarator_list ";"')
    def simple_declaration(self, p):
        pass

    @_('decl_specifier_seq init_declarator_list ";"')
    def simple_declaration(self, p):
        pass

    @_('id_type')
    def simple_type_specifier(self, p):
        pass

    @_('builtin_type_specifier')
    def simple_type_specifier(self, p):
        pass

    @_('attribute_specifier_seq try_block')
    def statement(self, p):
        pass

    @_('try_block')
    def statement(self, p):
        pass

    @_('declaration_statement')
    def statement(self, p):
        pass

    @_('attribute_specifier_seq jump_statement')
    def statement(self, p):
        pass

    @_('jump_statement')
    def statement(self, p):
        pass

    @_('attribute_specifier_seq iteration_statement')
    def statement(self, p):
        pass

    @_('iteration_statement')
    def statement(self, p):
        pass

    @_('attribute_specifier_seq selection_statement')
    def statement(self, p):
        pass

    @_('selection_statement')
    def statement(self, p):
        pass

    @_('attribute_specifier_seq compound_statement')
    def statement(self, p):
        pass

    @_('compound_statement')
    def statement(self, p):
        pass

    @_('attribute_specifier_seq expression_statement')
    def statement(self, p):
        pass

    @_('expression_statement')
    def statement(self, p):
        pass

    @_('labeled_statement')
    def statement(self, p):
        pass

    @_('statement')
    def statement_seq(self, p):
        pass

    @_('statement_seq statement')
    def statement_seq(self, p):
        pass

    @_('"register"')
    def storage_class_specifier(self, p):
        pass

    @_('"static"')
    def storage_class_specifier(self, p):
        pass

    @_('"extern"')
    def storage_class_specifier(self, p):
        pass

    @_('"mutable"')
    def storage_class_specifier(self, p):
        pass

    @_('"auto"')
    def storage_class_specifier(self, p):
        pass

    @_('constant_expression')
    def template_argument(self, p):
        pass

    @_('type_id')
    def template_argument(self, p):
        pass

    @_('template_argument_list "," template_argument')
    def template_argument_list(self, p):
        pass

    @_('template_argument')
    def template_argument_list(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "template" "<[" template_parameter_list "]>" declaration')
    def template_declaration(self, p):
        pass

    @_('decl_specifier_seq "template" "<[" template_parameter_list "]>" declaration')
    def template_declaration(self, p):
        pass

    @_('attribute_specifier_seq "template" "<[" template_parameter_list "]>" declaration')
    def template_declaration(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" declaration')
    def template_declaration(self, p):
        pass

    @_('type_parameter')
    def template_parameter(self, p):
        pass

    @_('parameter_declaration')
    def template_parameter(self, p):
        pass

    @_('template_parameter')
    def template_parameter_list(self, p):
        pass

    @_('template_parameter_list "," template_parameter')
    def template_parameter_list(self, p):
        pass

    @_('"<[" template_argument_list "]>"')
    def template_spec(self, p):
        pass

    @_('"<[" "]>"')
    def template_spec(self, p):
        pass

    @_('"throw" assignment_expression')
    def throw_expression(self, p):
        pass

    @_('"throw"')
    def throw_expression(self, p):
        pass

    @_('cv_qualifier')
    def trailing_type_specifier(self, p):
        pass

    @_('typename_specifier')
    def trailing_type_specifier(self, p):
        pass

    @_('elaborated_type_specifier')
    def trailing_type_specifier(self, p):
        pass

    @_('simple_type_specifier')
    def trailing_type_specifier(self, p):
        pass

    @_('declaration_seq')
    def translation_unit(self, p):
        pass

    @_('')
    def translation_unit(self, p):
        pass

    @_('"try" compound_statement handler_seq')
    def try_block(self, p):
        pass

    @_('type_specifier_seq abstract_declarator')
    def type_id(self, p):
        pass

    @_('type_specifier_seq')
    def type_id(self, p):
        pass

    @_('type_id_list "," type_id')
    def type_id_list(self, p):
        pass

    @_('type_id')
    def type_id_list(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class" "identifier" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class" "identifier"')
    def type_parameter(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class"')
    def type_parameter(self, p):
        pass

    @_('"typename" "identifier" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"typename" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"typename" "identifier"')
    def type_parameter(self, p):
        pass

    @_('"typename"')
    def type_parameter(self, p):
        pass

    @_('"class" "identifier" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"class" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"class" "identifier"')
    def type_parameter(self, p):
        pass

    @_('"class"')
    def type_parameter(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class" "..." "identifier" "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"template" "<[" template_parameter_list "]>" "class" "..." "=" type_id')
    def type_parameter(self, p):
        pass

    @_('"typename" "..." "identifier"')
    def type_parameter(self, p):
        pass

    @_('"typename" "..."')
    def type_parameter(self, p):
        pass

    @_('"class" "..." "identifier"')
    def type_parameter(self, p):
        pass

    @_('"class" "..."')
    def type_parameter(self, p):
        pass

    @_('trailing_type_specifier')
    def type_specifier(self, p):
        pass

    @_('class_specifier')
    def type_specifier(self, p):
        pass

    @_('enum_specifier')
    def type_specifier(self, p):
        pass

    @_('type_specifier type_specifier_seq')
    def type_specifier_seq(self, p):
        pass

    @_('type_specifier attribute_specifier_seq')
    def type_specifier_seq(self, p):
        pass

    @_('type_specifier')
    def type_specifier_seq(self, p):
        pass

    @_('"typename" id_type')
    def typename_specifier(self, p):
        pass

    @_('"sizeof" "(" type_id ")"')
    def unary_expression(self, p):
        pass

    @_('delete_expression')
    def unary_expression(self, p):
        pass

    @_('new_expression')
    def unary_expression(self, p):
        pass

    @_('"sizeof" unary_expression')
    def unary_expression(self, p):
        pass

    @_('unary_operator cast_expression')
    def unary_expression(self, p):
        pass

    @_('"--" cast_expression')
    def unary_expression(self, p):
        pass

    @_('"++" cast_expression')
    def unary_expression(self, p):
        pass

    @_('postfix_expression')
    def unary_expression(self, p):
        pass

    @_('"*"')
    def unary_operator(self, p):
        pass

    @_('"&"')
    def unary_operator(self, p):
        pass

    @_('"+"')
    def unary_operator(self, p):
        pass

    @_('"-"')
    def unary_operator(self, p):
        pass

    @_('"!"')
    def unary_operator(self, p):
        pass

    @_('"~"')
    def unary_operator(self, p):
        pass

    @_('"~" "identifier"')
    def unqualified_expression_id(self, p):
        pass

    @_('conversion_function_id')
    def unqualified_expression_id(self, p):
        pass

    @_('operator_function_id template_spec')
    def unqualified_expression_id(self, p):
        pass

    @_('operator_function_id')
    def unqualified_expression_id(self, p):
        pass

    @_('"identifier" template_spec')
    def unqualified_type_id(self, p):
        pass

    @_('"identifier"')
    def unqualified_type_id(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "using" "typename" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('decl_specifier_seq "using" "typename" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('attribute_specifier_seq "using" "typename" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('"using" "typename" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "using" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('decl_specifier_seq "using" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('attribute_specifier_seq "using" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('"using" id_type ";"')
    def using_declaration(self, p):
        pass

    @_('attribute_specifier_seq decl_specifier_seq "using" "namespace" id_type ";"')
    def using_directive(self, p):
        pass

    @_('decl_specifier_seq "using" "namespace" id_type ";"')
    def using_directive(self, p):
        pass

    @_('attribute_specifier_seq "using" "namespace" id_type ";"')
    def using_directive(self, p):
        pass

    @_('"using" "namespace" id_type ";"')
    def using_directive(self, p):
        pass
