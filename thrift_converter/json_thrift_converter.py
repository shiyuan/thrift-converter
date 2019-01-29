import ptsd.ast as ast
from .thrift_converter import ThriftConverter


class JsonThriftConverter(ThriftConverter):
    def convert(self, data, identifier):
        return self._convert(data, self.table.get(identifier))

    def _convert(self, js, node):
        # identifier
        if isinstance(node, ast.Identifier):
            ret = self.convert(js, node.value)

        # base_type
        elif isinstance(node, ast.BaseType):
            if isinstance(node, ast.I16) or isinstance(node, ast.I32) or isinstance(node, ast.I64):
                # the map key in standard json can't be int, need convert back
                ret = int(js)
            else:
                ret = js

        # container_type
        elif isinstance(node, ast.Map):
            ret = {}
            for js_key, js_value in js.items():
                key = self._convert(js_key, node.key_type)
                value = self._convert(js_value, node.value_type)
                ret[key] = value

        elif isinstance(node, ast.List):
            ret = [self._convert(value, node.value_type) for value in js]

        elif isinstance(node, ast.Set):
            # WARN: set is not json serializable
            # use {None: [item0, item1, ...]} to represent set
            ret = set([self._convert(value, node.value_type) for value in js['null']])

        # struct
        elif isinstance(node, ast.Struct):
            ret = self._get_class(node.name.value)()
            for field in node.fields:
                key = field.name.value
                field_value = js.get(key)
                if field_value is not None:
                    setattr(ret, key, self._convert(field_value, field.type))

        # typedef
        elif isinstance(node, ast.Typedef):
            ret = self._convert(js, node.type)

        # enum
        elif isinstance(node, ast.Enum):
            # WARN: enum is stored as name str
            enum = self._get_class(node.name.value)()
            ret = getattr(enum, '_NAMES_TO_VALUES').get(js)

        else:
            raise TypeError("Unrecognized type {}".format(node.name.value))

        return ret
