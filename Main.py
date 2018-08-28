from textx.metamodel import metamodel_from_file
from textx.scoping import MetaModelProvider
from textx.scoping.providers import FQNImportURI


class PortFQN():
    def __call__(self, obj, attr, obj_ref):
        ports = obj.prototype.ports
        for port in ports:
        #Does not work because interface is not yet resolved
            if port.interface.name == obj_ref.obj_name:
                return port
        return None

class ComponentHACK():
    def __call__(self, obj, attr, obj_ref):
        return obj.parent.parent.components[0]

class PrototypeHACK():
    def __call__(self, obj, attr, obj_ref):
        parent = obj
        while hasattr(parent, 'parent'):
            parent = parent.parent
        for model in parent._tx_model_repository.local_models.filename_to_model.values():
            return model.components[0]

if __name__ == '__main__':
    f_mm = metamodel_from_file('FModel.tx')
    i_mm = metamodel_from_file('IModel.tx')
    MetaModelProvider.add_metamodel('*.fmodel', f_mm)
    MetaModelProvider.add_metamodel('*.imodel', i_mm)

    f_mm.register_scope_providers({
        "*.interface": FQNImportURI(),
        "*.component": ComponentHACK(),
        "*.prototype": PrototypeHACK(),
        "*.port": PortFQN(),
    })
    f = f_mm.model_from_file("main.fmodel")
    print(f)

