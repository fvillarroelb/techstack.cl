import redis


class RedisCache():
    def __init__(self):
        self.r = redis.Redis(
        host='redis-17110.c1.asia-northeast1-1.gce.cloud.redislabs.com',
        port=17110,
        password='kFXKoEKn9Wk8ILWQGFIDK1k2In0Kg7qp')
     

    def saveValue(self,clave,valor):
        # Guardar un valor en Redis
       return self.r.set(clave,valor)

    def getValue(self,clave):
        # Obtener el valor de Redis
        valor = self.r.get(clave)
        # Imprimir el valor obtenido
        return valor