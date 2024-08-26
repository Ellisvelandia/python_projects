class SingletonComponenteCliente:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class SingletonComponentePago:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class SingletonComponenteInventario:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class SingletonComponenteEnvio:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

componente_cliente1 = SingletonComponenteCliente()
componente_cliente2 = SingletonComponenteCliente()

print(componente_cliente1 is componente_cliente2)  