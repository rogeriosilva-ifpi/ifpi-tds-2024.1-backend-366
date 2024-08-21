Objetivo: Criar uma API de App de Corridas (Uber)

Recurso/Objeto: Corrida
- Atributos: origem, destino, distancia(km), valor(R$ 6,65 + R$ 2/km),
- Atributos: estado('Requisitada', 'Em Andamento', 'Finalizado')

Endpoints:
- POST - Criar Corrida
- GET - Listar Corridas
  > Filtros: Listar por Estado
  > GET /corridas?estado=requisitada
- PUT Alterar Corrida (somente para requisitadas e em andamento)
- POST - Iniciar Corrida (somente para requisitadas)
- POST - Finalizar Corrida (somente para em andamento)
- DELETE - Remover Corrida (somente requisitadas)