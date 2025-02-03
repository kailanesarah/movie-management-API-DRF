<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>🎬 API de Gestão de Filmes</h1>

<p>Esta API foi desenvolvida em <strong>Django</strong> utilizando o <strong>Django REST Framework (DRF)</strong> para facilitar a gestão de filmes, atores, avaliações e gêneros.</p>

<h2>📌 Tecnologias Utilizadas</h2>
<ul>
    <li>Python 3.x</li>
        <li>Django</li>
        <li>Django REST Framework</li>
        <li>SQLite / PostgreSQL</li>
        <li>Docker (opcional)</li>
</ul>

<h2>⚙️ Funcionalidades</h2>
  <ul>
        <li>📽️ <strong>Movies</strong>: CRUD completo de filmes.</li>
        <li>🎭 <strong>Actors</strong>: Gerenciamento de atores e suas associações com os filmes.</li>
        <li>📝 <strong>Reviews</strong>: Permite que usuários adicionem avaliações para filmes.</li>
        <li>🎞️ <strong>Genres</strong>: Categorização dos filmes por gênero.</li>
  </ul>

<h2>🚀 Como Executar o Projeto</h2>

<h3>1. Clonar o Repositório</h3>
<pre><code>git clone https://github.com/kailanesarah/api-django-rest/</code></pre>

<h3>2. Criar e Ativar um Ambiente Virtual</h3>
<pre><code>python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows</code></pre>

<h3>3. Instalar Dependências</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Executar Migrações</h3>
<pre><code>python manage.py migrate</code></pre>

<h3>5. Rodar o Servidor</h3>
<pre><code>python manage.py runserver</code></pre>

<h2>📡 Endpoints Principais</h2>
    <ul>
        <li><code>/api/v1/movies/</code> - Lista e cria filmes.</li>
        <li><code>/api/v1/movies/&lt;pk&gt;/</code> - Detalha, atualiza e deleta um filme específico.</li>
        <li><code>/api/v1/actors/</code> - Lista e cria atores.</li>
        <li><code>/api/v1/actors/&lt;pk&gt;/</code> - Detalha, atualiza e deleta um ator específico.</li>
        <li><code>/api/v1/reviews/</code> - Lista e cria avaliações.</li>
        <li><code>/api/v1/reviews/&lt;pk&gt;/</code> - Detalha, atualiza e deleta uma avaliação específica.</li>
        <li><code>/api/v1/genres/</code> - Lista e cria gêneros.</li>
        <li><code>/api/v1/genres/&lt;pk&gt;/</code> - Detalha, atualiza e deleta um gênero específico.</li>
    </ul>
    <h2>📌 Contribuições</h2>
    <p>Contribuições são bem-vindas! Para contribuir, siga estes passos:</p>
    <ol>
        <li>Fork o repositório</li>
        <li>Crie uma branch (<code>git checkout -b minha-feature</code>)</li>
        <li>Faça suas alterações e commit (<code>git commit -m "Minha nova feature"</code>)</li>
        <li>Faça push para sua branch (<code>git push origin minha-feature</code>)</li>
        <li>Abra um Pull Request</li>
    </ol>

<h2>📜 Licença</h2>
<p>Este projeto está licenciado sob a <strong>MIT License</strong>.</p>

</body>
</html>
