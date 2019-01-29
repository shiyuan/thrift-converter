from .thrift_converter import ThriftConverter
import ptsd.ast as ast


class ThriftJsonConverter(ThriftConverter):
    def convert(self, obj, identifier):
        return self._convert(obj, self.table.get(identifier))

    def _convert(self, obj, node):
        # identifier
        if isinstance(node, ast.Identifier):
            ret = self.convert(obj, node.value)

        # base_type
        elif isinstance(node, ast.BaseType):
            ret = obj

        # container_type
        elif isinstance(node, ast.Map):
            ret = {}
            for key, value in obj.items():
                key_ = self._convert(key, node.key_type)
                value_ = self._convert(value, node.value_type)
                ret[key_] = value_

        elif isinstance(node, ast.List):
            ret = [self._convert(value, node.value_type) for value in obj]

        elif isinstance(node, ast.Set):
            # WARN: set is not json serializable
            # use {None: [item0, item1, ...]} to represent set
            ret = {None: [self._convert(value, node.value_type) for value in obj]}

        # struct
        elif isinstance(node, ast.Struct):
            ret = {}
            for field in node.fields:
                key = field.name.value
                value = getattr(obj, key)
                if value is not None:
                    value = self._convert(value, field.type)
                    ret[key] = value

        # typedef
        elif isinstance(node, ast.Typedef):
            ret = self._convert(obj, node.type)

        # enum
        elif isinstance(node, ast.Enum):
            # WARN: enum is stored as name str
            enum = self._get_class(node.name.value)()
            ret = getattr(enum, '_VALUES_TO_NAMES').get(obj)

        else:
            raise TypeError("Unrecognized type {}".format(node.name.value))

        return ret

