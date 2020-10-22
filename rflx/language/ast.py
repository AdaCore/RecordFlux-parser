from langkit.dsl import ASTNode, Field, abstract  # type: ignore


@abstract
class RFLXNode(ASTNode):
    pass


class NullID(RFLXNode):
    pass


class UnqualifiedID(RFLXNode):
    token_node = True


class ID(RFLXNode):
    parts = Field()


class PackageDeclarationNode(RFLXNode):
    name_start = Field()
    content = Field()
    name_end = Field()


@abstract
class TypeDef(RFLXNode):
    pass


@abstract
class IntegerTypeDef(TypeDef):
    pass


class RangeTypeDef(IntegerTypeDef):
    lower = Field()
    upper = Field()
    size = Field()


class ModularTypeDef(IntegerTypeDef):
    mod = Field()


@abstract
class AbstractMessage(TypeDef):
    pass


class NullMessage(AbstractMessage):
    pass


class Message(AbstractMessage):
    components = Field()
    checksums = Field()


class Type(RFLXNode):
    identifier = Field()
    type_definition = Field(type=TypeDef)


class BasedLiteral(RFLXNode):
    # base = Field()
    # value = Field()
    pass


class NumericLiteral(RFLXNode):
    value = Field()


class SizeAspect(RFLXNode):
    size = Field()


class Then(RFLXNode):
    name = Field()
    aspects = Field()
    condition = Field()


class First(RFLXNode):
    condition = Field()


class Last(RFLXNode):
    condition = Field()


class If(RFLXNode):
    condition = Field()


class NullComponent(RFLXNode):
    then = Field()


class Component(RFLXNode):
    name = Field()
    type_name = Field()
    thens = Field()


class Components(RFLXNode):
    null_component = Field()
    components = Field()


class ValueRange(RFLXNode):
    lower = Field()
    upper = Field()


class ChecksumAssoc(RFLXNode):
    name = Field()
    covered_fields = Field()


class ChecksumAspect(RFLXNode):
    associations = Field()


class Variable(RFLXNode):
    name = Field()


class Op(RFLXNode):
    enum_node = True
    alternatives = [
        "pow",
        "mul",
        "div",
        "add",
        "sub",
        "eq",
        "neq",
        "le",
        "lt",
        "gt",
        "ge",
        "and",
        "or",
    ]


class BinOp(RFLXNode):
    left = Field()
    op = Field(type=Op)
    right = Field()


class ParenExpression(RFLXNode):
    expr = Field()


class BooleanExpression(RFLXNode):
    expr = Field()


class MathematicalExpression(RFLXNode):
    expr = Field()