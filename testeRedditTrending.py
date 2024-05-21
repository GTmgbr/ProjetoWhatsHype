import redditwarp as rw
from redditwarp.http.transport.aiohttp import AIOHTTPTransport

# Substitua 'SEU_CLIENT_ID' e 'SEU_CLIENT_SECRET' pelas suas credenciais do Reddit
client = rw.Client(
    client_id='SEU_CLIENT_ID',
    client_secret='SEU_CLIENT_SECRET',
    user_agent='script:temas_relevantes:v1.2.0 (por u/seu_nome_de_usuario)',
    transport=AIOHTTPTransport(),
)

# Função para buscar comentários com mais karma
def buscar_comentarios_mais_votados(subreddit: str, limite: int):
    subr = client.subreddit(subreddit)
    return subr.comments.top(time='all', limit=limite)

# Função para destacar controvérsias
def buscar_comentarios_controversos(subreddit: str, limite: int):
    subr = client.subreddit(subreddit)
    return subr.comments.controversial(time='all', limit=limite)

# Função para destacar novos comentários
def buscar_novos_comentarios(subreddit: str, limite: int):
    subr = client.subreddit(subreddit)
    return subr.comments.new(limit=limite)

# Exemplo de uso das funções
subreddit_alvo = 'all'  # Usando 'all' para buscar em todos os subreddits
limite_comentarios = 100

comentarios_mais_votados = buscar_comentarios_mais_votados(subreddit_alvo, limite_comentarios)
comentarios_controversos = buscar_comentarios_controversos(subreddit_alvo, limite_comentarios)
novos_comentarios = buscar_novos_comentarios(subreddit_alvo, limite_comentarios)

# Processar e imprimir os resultados
# Aqui você pode adicionar o código para processar os dados e identificar temas relevantes

# Get the top submissions sorted by the number of comments
top_commented = client.p.all.pull.top('day', sort='comments', limit=5)

# Print the title and number of comments for each submission
for submission in top_commented:
    print(f"Title: {submission.title}, Comments: {submission.num_comments}")
