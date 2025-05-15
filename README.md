<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>🎬 Movie Management API - DRF</h1>

<p>This API was developed as part of the <strong>Django Master</strong> course by <strong>PyCode BR</strong>, using <strong>Django</strong> and the <strong>Django REST Framework (DRF)</strong> to facilitate the management of movies, actors, reviews, and genres.</p>

<h2>🚀 Project Overview</h2>

 <h3>🏞️ Situation</h3>
    <p>Managing movie databases efficiently is a challenge for developers and businesses. There was a need for an API that could streamline CRUD operations for movies, actors, reviews, and genres while ensuring scalability.</p>

<h3>🎯 Task</h3>
    <p>The goal was to create a structured RESTful API using Django that supports full CRUD operations for managing movie-related data, providing flexibility, reliability, and easy integration.</p>

<h3>🏃‍♂️ Action</h3>
    <ul>
        <li>Developed an API using Django REST Framework.</li>
        <li>Implemented full CRUD operations for movies, actors, reviews, and genres.</li>
        <li>Designed a clean and efficient data structure with SQLite/PostgreSQL support.</li>
        <li>Enhanced API scalability by integrating Docker (optional).</li>
    </ul>

 <h3>🎯 Result</h3>
    <ul>
        <li>A fully functional API that simplifies movie data management.</li>
        <li>Improved efficiency in handling actor associations and user reviews.</li>
        <li>Secure database handling and authentication mechanisms.</li>
        <li>Ready for future enhancements such as user ratings and advanced filtering.</li>
    </ul>

<h2>📌 Technologies Used</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Django</li>
        <li>Django REST Framework</li>
        <li>SQLite / PostgreSQL</li>
        <li>Docker (optional)</li>
    </ul>

<h2>⚙️ Features</h2>
    <ul>
        <li>📽️ <strong>Movies:</strong> Full CRUD for movie data.</li>
        <li>🎭 <strong>Actors:</strong> Management of actors and their associations with movies.</li>
        <li>📝 <strong>Reviews:</strong> Allows users to add reviews for movies.</li>
        <li>🎞️ <strong>Genres:</strong> Categorization of movies by genre.</li>
    </ul>

<h2>🚀 How to Run the Project</h2>

<h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/kailanesarah/movie-management-API-DRF/</code></pre>

<h3>2. Create and Activate a Virtual Environment</h3>
    <pre><code>python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows</code></pre>

<h3>3. Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Run Migrations</h3>
    <pre><code>python manage.py migrate</code></pre>

<h3>5. Start the Server</h3>
    <pre><code>python manage.py runserver</code></pre>

 <h2>📡 Main Endpoints</h2>
<table>
        <tr>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
        <tr><td>/api/v1/movies/</td><td>Lists and creates movies.</td></tr>
        <tr><td>/api/v1/movies/&lt;pk&gt;/</td><td>Shows, updates, and deletes a specific movie.</td></tr>
        <tr><td>/api/v1/actors/</td><td>Lists and creates actors.</td></tr>
        <tr><td>/api/v1/actors/&lt;pk&gt;/</td><td>Shows, updates, and deletes a specific actor.</td></tr>
        <tr><td>/api/v1/reviews/</td><td>Lists and creates reviews.</td></tr>
        <tr><td>/api/v1/reviews/&lt;pk&gt;/</td><td>Shows, updates, and deletes a specific review.</td></tr>
        <tr><td>/api/v1/genres/</td><td>Lists and creates genres.</td></tr>
        <tr><td>/api/v1/genres/&lt;pk&gt;/</td><td>Shows, updates, and deletes a specific genre.</td></tr>
    </table>

<h2>📌 Contributions</h2>
    <p>Contributions are welcome! To contribute, follow these steps:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b my-feature</code>).</li>
        <li>Make your changes and commit (<code>git commit -m "My new feature"</code>).</li>
        <li>Push your branch (<code>git push origin my-feature</code>).</li>
        <li>Open a Pull Request.</li>
    </ol>

<h2>📜 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>

</body>
</html>
