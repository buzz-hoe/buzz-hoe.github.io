<!DOCTYPE md>
<md lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HIMA PPKn UNRI 2025</title>
    <style>
        body {
            background-image: url('/static/images/bendera.jpg'), url('/static/images/pancasila.jpg');
            background-size: cover, contain;
            background-position: center, top right;
            background-repeat: no-repeat, no-repeat;
            text-align: center;
            color: rgb(0, 0, 0);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            font-size: 3em;
            margin-top: 20%;
            color: black;
        }
        .bubble-button {
            position: relative;
            padding: 15px 30px;
            font-size: 1.5em;
            color: rgb(0, 0, 0);
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            overflow: hidden;
            outline: none;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
        }
        .bubble-button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background-color: rgba(255, 255, 255, 0.15);
            border-radius: 50%;
            transform: translate(-50%, -50%) scale(0);
            transition: transform 0.5s ease-out;
        }
        .bubble-button:hover::before {
            transform: translate(-50%, -50%) scale(1);
        }
        .footer {
            margin-top: auto;
            padding: 10px;
            font-size: 1em;
            color: black;
            position: absolute;
            bottom: 10px;
            width: 100%;
            text-align: center;
        }
        .random-text {
            display: inline-block;
            animation: randomText 5s infinite;
        }
        @keyframes randomText {
            0%, 100% { content: "Made by Kominfo PPKn 2025"; }
            25% { content: "M4d3 by K0m1nf0 PPKn 2025"; }
            50% { content: "M@d3 by K0m1nf0 PPKn 2025"; }
            75% { content: "M4d3 by K0m1nf0 PPKn 2025"; }
        }
    </style>
</head>
<body>
    <h1>Pendaftaran Pengurus HIMA PRODI PPKn 2025</h1>
    <a href="/form_nama" class="bubble-button">Mulai Pendaftaran</a>
    <div class="footer">
        <span class="random-text">Made by Kominfo PPKn 2025</span>
    </div>
</body>
</html>
