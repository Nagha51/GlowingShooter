# GlowingShooter
Splash boom Zbwa !

![Glowing shooter image][glowing_shooter_image]

# Install

### Python

```bash
pip install -e .
```

### Web
```bash
npm install
```

# Server CLI commands

- Start server:
```bash
glowing_shooter
```

- Show help

```bash
glowing_shooter --help
```

# Access web page

- Generate within `dist` folder the `index.html` including the generated `game.XXX.js` and `game.XXX.css`
```bash
npm run build
```

Open the freshly generated [Game Home Page: /dist/index.html](/dist/index.html)


# Development

### Python

- Install test extras
```bash
pip install -e .[test]
```

### Web

- Live-updating `game.XXX.js` and `game.XXX.css`
```bash
npm run watch
```


# Credits

- Nice base project of: https://github.com/vzhou842/example-.io-game
- Webpack explained [FR]: https://www.alsacreations.com/tuto/lire/1754-debuter-avec-webpack.html
- Flask-IO:https://flask-socketio.readthedocs.io/en/latest/
- Miguel FlaskIO tutorial: https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent



[glowing_shooter_image]: /docs/resources/glowing_shooter.png "Glowing shooter image"