MSG = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Email Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;            
        }
       .body__ {
            background-color: #f5f5f5; /* Light grey */
       }
       .banner {
            width: 100%;
            text-align: center;
            padding: 20px 0;
        }
       .banner img {
            max-width: 100%;
            height: auto;
        }
       .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
        }
        h1, h2 {
            color: #333;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        .msg {
            font-size:1.25rem;
        }
        .footer {
            background-color: #0094FF;
            color: white;
            text-align: center;
            padding: 0.3rem;
        }
    </style>
</head>
<body>
<div class="body__">
    <div class="banner">
        <img src="cid:header_img" alt="Banner Image" width="600" height="300">
    </div>

    <div class="container">
        <p>Toda terça, 8h30 da manhã</p>
        <h1>🐍 Encontro 6 - (23/7/24)</h1>
        <div class="msg">
            <p>Olá!</p>
            <p>Depois dessa grande revisão de quinta passada, voltaremos a programação normal já na próxima terça.</p>
            <p>Levem notebooks!</p>
            <p>Portanto, é essencial que estudem o último notebook e vejam pelo menos as 1as horas desse curso:</p>
            <a href="https://www.youtube.com/watch?v=yTQDbqmv8Ho&t=1158s" target="_blank" title="Ver no youtube">
                <img src="http://i3.ytimg.com/vi/yTQDbqmv8Ho/hqdefault.jpg" alt="Clique para ver o vídeo" width="600" height="400">
              </a>            
            <p>Outros tutoriais, se você estuda melhor lendo do que vendo vídeos:</p>
            <ul>
                <li><a href="https://didatica.tech/tudo-sobre-variaveis-em-python-aprenda-com-exemplos-praticos">Variáveis</a></li>
                <li><a href="https://didatica.tech/tudo-sobre-listas-em-python/">Listas</a></li>
                <li><a href="https://www.datacamp.com/pt/tutorial/for-loops-in-python">Loops</a></li>
            </ul>
            <p>Até lá!</p>
        </div>
        <div class="footer">
            © 2024 - IG/Seplag.py
        </div>
    </div>
</div>

</body>
</html>
"""
