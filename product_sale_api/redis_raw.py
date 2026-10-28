'''Imports'''
import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "trocando_o_meu_valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")

# delete de dados
redis_conn.delete("chave_1")

### comandos para hash
meu_hash = {
    "nome": "Naruto",
    "idade": 25,
    "cidade": "Aldeia da Folha"
}

redis_conn.hset("meu_hash", "nome", "Naruto")
redis_conn.hset("meu_hash", "idade", 25)
redis_conn.hset("meu_hash", "cidade", "Aldeia da Folha")

valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")

redis_conn.hdel("meu_hash", "idade")

# buscas por existencia
elem = redis_conn.exists("chave_1")
print(elem)

elem_2 = redis_conn.hexists("meu_hash", "nome")
print(elem_2)

####
# dados -> TTL -> Time to Live [segundos]

redis_conn.set("chave_del", "esse valor sera deletado", 12)
redis_conn.expire("meu_hash", 30)
