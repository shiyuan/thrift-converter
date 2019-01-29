from ptsd.parser import Parser
from abc import abstractclassmethod


class ThriftConverter:
    def __init__(self, file_name):
        tree = self.init_ast(file_name)
        namespace = self._get_namespace(tree.namespaces, file_name)
        self._init_ttypes(namespace)
        self._init_table(tree.body)

    @abstractclassmethod
    def convert(self, data, identifier):
        pass

    @staticmethod
    def init_ast(file_name):
        with open(file_name, 'r') as f:
            return Parser().parse(f.read())

    @staticmethod
    def _get_namespace(namespaces, file_name):
        namespace_str = None
        for namespace in namespaces:
            if namespace.language_id == 'py':
                namespace_str = namespace.name.value
                break
        if namespace_str is None:
            namespace_str = file_name.split('/')[-1].split('.thrift')[0]
        return namespace_str

    def _init_ttypes(self, namespace):
        import importlib
        self.ttypes = importlib.import_module('{}.ttypes'.format(namespace))

    def _init_table(self, identifiers):
        table = {}
        for node in identifiers:
            table[node.name.value] = node
        self.table = table

    def _get_class(self, cls):
        return getattr(self.ttypes, cls)