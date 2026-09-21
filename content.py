# -*- coding: utf-8 -*-
"""Contenido de las paginas. Editar aqui y volver a ejecutar build.py."""

SITE = {
    "name": "MicrosStreaming",
    "base": "https://poemasbiblicos.github.io/microstreaming.github.io",
    "desc": ("Guias independientes sobre micros para streaming: comparativas, "
             "consejos de configuracion y ayuda para elegir microfono."),
    "published": "2026-09-21",
    "updated": "2026-09-21",
}

PAGES = {}

# --------------------------------------------------------------------------
PAGES[""] = {
    "title": "Micros Streaming: guía para elegir micrófono en 2026",
    "desc": ("Guía honesta de micros para streaming: USB o XLR, condensador o "
             "dinámico, cuánto gastar y qué modelo encaja con tu cuarto."),
    "h1": "Micros para streaming: elige bien a la primera",
    "crumb": "Inicio",
    "lede": ("Ochenta por ciento de los directos que suenan mal no tienen un problema "
             "de micrófono, sino de cuarto, de patrón polar o de ganancia. Aquí "
             "aprendes a distinguir las tres cosas antes de gastar un peso."),
    "toc": [
        ("empezar", "Por dónde empezar"),
        ("tres-decisiones", "Las tres decisiones que importan"),
        ("por-situacion", "Qué micro según tu situación"),
        ("errores", "Errores que arruinan el sonido"),
        ("guias", "Todas las guías"),
    ],
    "faq": [
        ("¿Cuál es el mejor micro para streaming si apenas empiezo?",
         "Un dinámico USB o un condensador USB de gama media es suficiente para "
         "empezar. Si tu cuarto tiene eco, ruido de ventilador o vecinos, elige "
         "dinámico: rechaza mucho mejor el ambiente. Si el cuarto es silencioso y "
         "quieres una voz más detallada, elige condensador."),
        ("¿Un micro caro mejora mi directo automáticamente?",
         "No. Un micro de 400 dólares en un cuarto con eco suena peor que uno de 60 "
         "dólares bien colocado a 10 cm de la boca y con un poco de absorción "
         "acústica detrás. El orden correcto de inversión es: técnica, colocación, "
         "tratamiento del cuarto y, por último, micrófono."),
        ("¿Necesito interfaz de audio?",
         "Solo si eliges un micrófono XLR. Los micros USB llevan la conversión "
         "integrada y se conectan directo al PC. Un micro XLR necesita interfaz o "
         "mezclador, y si es condensador, además alimentación phantom de 48 V."),
        ("¿El micro del celular sirve para transmitir?",
         "Para pruebas sí, y hay soluciones de solapa por USB-C o Lightning que "
         "suenan sorprendentemente bien para streaming móvil. Lo tratamos en la "
         "guía de micrófono para teléfono."),
    ],
    "body": """
<h2 id="empezar">Por dónde empezar</h2>
<p>Si llegaste buscando <strong>micros para streaming</strong>, probablemente ya viste
veinte listas de «los 10 mejores». El problema de esas listas es que dan la respuesta
antes de hacer la pregunta. El micrófono correcto depende de tres cosas que solo tú
conoces: cómo suena tu cuarto, con qué te vas a conectar y cuánta voz vas a poner
delante de él.</p>

<p>Esta guía está escrita al revés: primero decides, después compras. Cada bloque de
abajo lleva a una guía específica cuando necesitas profundizar.</p>

<div class="note">
<strong>Regla de oro:</strong> la distancia entre tu boca y la cápsula es la variable
que más cambia tu sonido, y es gratis. A 10 cm tu voz domina el ambiente; a 50 cm tu
cuarto domina tu voz.
</div>

<h2 id="tres-decisiones">Las tres decisiones que importan</h2>

<h3>1. Dinámico o condensador</h3>
<p>Un <strong>micrófono dinámico</strong> usa una bobina móvil, es poco sensible y
necesita que le hables cerca. Esa «desventaja» es justo lo que quieres en un cuarto
normal: el teclado, el ventilador y el eco quedan fuera. Es lo que usan las radios.</p>
<p>Un <strong>micrófono de condensador</strong> usa un diafragma polarizado, es mucho
más sensible y capta detalle y aire en la voz. También capta el perro del vecino. Es
excelente en un cuarto tratado o silencioso, y problemático en uno vivo.</p>
<p class="pill">Cuarto ruidoso → dinámico</p><span class="pill">Cuarto silencioso →
condensador</span>
<p><a href="microfono-condensador/">Guía completa de micrófono de condensador →</a></p>

<h3>2. USB o XLR</h3>
<p>USB es un micrófono con tarjeta de sonido dentro: lo enchufas y funciona. XLR es
la conexión profesional: el micro solo entrega señal analógica y necesita una interfaz
que la convierta. XLR escala mejor (puedes cambiar micro o interfaz por separado, y
añadir un segundo invitado), pero cuesta más en total.</p>
<p><a href="usb-o-xlr/">Comparativa USB vs XLR con precios reales →</a></p>

<h3>3. Patrón polar</h3>
<p>El patrón polar dice desde dónde escucha el micro. Para streaming quieres
<strong>cardioide</strong>: capta de frente y rechaza por detrás. Los micros con
selector multipatrón (omni, bidireccional, estéreo) son útiles para entrevistas
presenciales, pero para un streamer solo suman botones que se pueden mover sin querer.</p>

<table>
<thead><tr><th>Patrón</th><th>Capta desde</th><th>Úsalo para</th></tr></thead>
<tbody>
<tr><td>Cardioide</td><td>Frente</td><td>Streaming en solitario, podcast, voz en off</td></tr>
<tr><td>Supercardioide</td><td>Frente, más estrecho</td><td>Cuartos con ruido lateral</td></tr>
<tr><td>Omnidireccional</td><td>Todas partes</td><td>Grabación ambiental, nunca para directo</td></tr>
<tr><td>Bidireccional</td><td>Frente y atrás</td><td>Entrevista cara a cara con un micro</td></tr>
</tbody></table>

<h2 id="por-situacion">Qué micro según tu situación</h2>
<div class="grid">
  <a class="tile" href="mejores-micros-streaming/"><b>Quiero una recomendación directa</b>
  <span>Comparativa de los micros para streaming que valen la pena, por rango de precio.</span></a>
  <a class="tile" href="micros-streaming-baratos/"><b>Tengo presupuesto ajustado</b>
  <span>Qué se puede lograr con poco dinero y qué recortes sí se notan.</span></a>
  <a class="tile" href="microfono-condensador/"><b>Quiero la voz más detallada</b>
  <span>Cómo funciona un condensador, phantom 48 V y cuándo no comprarlo.</span></a>
  <a class="tile" href="usb-o-xlr/"><b>No sé si necesito interfaz</b>
  <span>USB vs XLR: coste total, latencia y cuándo dar el salto.</span></a>
  <a class="tile" href="microfono-para-telefono/"><b>Transmito desde el celular</b>
  <span>Micrófonos para teléfono: solapa, USB-C, adaptadores y ajustes.</span></a>
  <a class="tile" href="behringer-c1-vs-c3/"><b>Behringer C-1 o C-3</b>
  <span>Dos condensadores económicos muy buscados, comparados sin marketing.</span></a>
  <a class="tile" href="por-modelo/"><b>Busco un modelo concreto</b>
  <span>Fichas una a una: Behringer, Neumann, QuadCast, array, electret y Shure.</span></a>
</div>

<h2 id="errores">Cinco errores que arruinan el sonido</h2>
<ul class="checks">
<li><strong>Ganancia al máximo.</strong> Sube la ganancia hasta que tus picos normales
lleguen a unos -12 dB, no a 0. Lo que subes de más se convierte en ruido de fondo.</li>
<li><strong>Micro sobre el escritorio.</strong> Cada tecla que pulsas viaja por la mesa
hasta la cápsula. Usa brazo articulado y araña antivibración, o al menos una base de
espuma.</li>
<li><strong>Hablarle de frente a bocajarro.</strong> Colócalo ligeramente fuera de eje,
apuntando a la comisura de la boca. Las «p» explosivas dejan de golpear el diafragma.</li>
<li><strong>Cuarto vacío.</strong> Una cortina, una estantería con libros y una alfombra
hacen más por tu audio que cambiar de micrófono.</li>
<li><strong>Cadena de efectos sin criterio.</strong> Una puerta de ruido mal ajustada te
corta las palabras. Empieza solo con un compresor suave y un filtro paso alto en 80 Hz.</li>
</ul>

<h2 id="guias">Todas las guías</h2>
<ul>
<li><a href="mejores-micros-streaming/">Mejores micros para streaming: comparativa por presupuesto</a></li>
<li><a href="microfono-condensador/">Micrófono de condensador: cómo elegirlo y cuándo evitarlo</a></li>
<li><a href="usb-o-xlr/">Micrófono USB o XLR: qué te conviene de verdad</a></li>
<li><a href="micros-streaming-baratos/">Micros de streaming baratos que no suenan baratos</a></li>
<li><a href="microfono-para-telefono/">Micrófono para teléfono: streaming desde el móvil</a></li>
<li><a href="behringer-c1-vs-c3/">Behringer C-1 vs C-3: cuál comprar</a></li>
</ul>

<h3>Fichas por modelo</h3>
<ul>
<li><a href="por-modelo/">Índice de micrófonos por modelo</a></li>
<li><a href="behringer-c1/">Behringer C-1: análisis, precio y requisitos</a></li>
<li><a href="behringer-c3/">Behringer C-3: patrones polares y usos</a></li>
<li><a href="microfono-condensador-neumann/">Condensador Neumann: qué estás pagando</a></li>
<li><a href="hyperx-quadcast-rgb/">HyperX QuadCast RGB: análisis sin marketing</a></li>
<li><a href="microfono-array/">Micrófono array: qué es y cuándo lo necesitas</a></li>
<li><a href="microfono-electronico/">Micrófono electrónico: qué significa el término</a></li>
<li><a href="shure-antena/">Antenas Shure para sistemas inalámbricos</a></li>
</ul>

<h3>Sobre el sitio</h3>
<ul>
<li><a href="quienes-somos/">Quiénes somos y cómo evaluamos</a></li>
</ul>
""",
}

# --------------------------------------------------------------------------
PAGES["mejores-micros-streaming/"] = {
    "title": "Mejores micros para streaming 2026: comparativa por presupuesto",
    "desc": ("Comparativa de los mejores micros para streaming por rango de precio: "
             "dinámicos, condensadores, USB y XLR, con sus pegas reales."),
    "h1": "Mejores micros para streaming, por presupuesto",
    "crumb": "Mejores micros",
    "article": True,
    "lede": ("Cinco categorías, criterios claros y las pegas que las fichas de producto "
             "no cuentan. Ordenado por lo que puedes gastar, no por lo que alguien "
             "quiere venderte."),
    "toc": [
        ("criterios", "Cómo evaluamos"),
        ("entrada", "Entrada: hasta 70 USD"),
        ("media", "Gama media: 70 a 160 USD"),
        ("alta", "Gama alta: 160 USD en adelante"),
        ("tabla", "Tabla comparativa"),
        ("veredicto", "Veredicto rápido"),
    ],
    "faq": [
        ("¿Cuál es el mejor micro para streaming en general?",
         "Para la mayoría de streamers en cuartos normales, un dinámico cardioide con "
         "salida USB es la opción con mejor relación entre resultado y riesgo: perdona "
         "el ruido ambiente, no necesita interfaz y se oye profesional a corta "
         "distancia."),
        ("¿Vale la pena un micro de más de 300 dólares para Twitch o YouTube?",
         "Solo si ya tienes el cuarto tratado, una interfaz decente y técnica de "
         "micrófono estable. Por debajo de eso, el mismo dinero rinde mucho más en "
         "paneles acústicos, un brazo sólido y un filtro antipop."),
        ("¿Los micros con luces RGB suenan peor?",
         "Las luces no afectan al sonido, pero sí al precio: parte del presupuesto se "
         "va en la carcasa y la iluminación en lugar de en la cápsula. A igual precio, "
         "un modelo sin RGB suele llevar mejor componente de audio."),
    ],
    "body": """
<h2 id="criterios">Cómo evaluamos</h2>
<p>No puntuamos micrófonos con un número inventado. Comparamos cinco factores que
cambian tu resultado real:</p>
<ul class="checks">
<li><strong>Rechazo de ambiente.</strong> Cuánto ruido de cuarto deja entrar a distancia
de uso normal.</li>
<li><strong>Coste total.</strong> Micro + interfaz + brazo + cable, no solo la etiqueta.</li>
<li><strong>Tolerancia a errores.</strong> Qué pasa si te alejas, gritas o mueves la mesa.</li>
<li><strong>Escalabilidad.</strong> Si mañana quieres un invitado o grabar instrumentos.</li>
<li><strong>Mantenimiento.</strong> Repuestos, drivers y soporte a largo plazo.</li>
</ul>
<p>Los precios son rangos internacionales orientativos en dólares. En Colombia, México
o Argentina súmales importación e impuestos; conviene comparar en tienda local antes
de decidir.</p>

<h2 id="entrada">Entrada: hasta 70 USD</h2>

<div class="card">
<h3>Dinámico USB de entrada</h3>
<p><span class="pill ok">Recomendado para empezar</span><span class="pill">Dinámico</span><span class="pill">USB</span></p>
<p>Es la compra más segura si tu cuarto no está tratado. Un dinámico cardioide por USB
te obliga a hablar cerca, y esa cercanía es exactamente lo que hace que tu voz suene
grande y el cuarto desaparezca. Modelos de referencia en esta franja: Samson Q2U, Behringer
BV44 y equivalentes con doble salida USB/XLR.</p>
<p><strong>Por qué gana:</strong> la doble salida USB + XLR te deja migrar a interfaz
más adelante sin cambiar de micrófono. Es la única gama de entrada que no se vuelve
basura cuando mejoras.</p>
<p><strong>Pega real:</strong> necesitas más ganancia que un condensador. Si tu PC mete
ruido por USB, se nota.</p>
</div>

<div class="card">
<h3>Condensador XLR económico (Behringer C-1, C-3 y similares)</h3>
<p><span class="pill">Condensador</span><span class="pill">XLR</span><span class="pill">Necesita phantom 48 V</span></p>
<p>Cápsulas sorprendentemente honestas por muy poco dinero. El truco está en que no
puedes usarlos solos: necesitas una interfaz con phantom, y eso duplica o triplica el
coste de entrada.</p>
<p><strong>Por qué gana:</strong> si ya tienes interfaz, es el salto de calidad más
barato que existe.</p>
<p><strong>Pega real:</strong> captan todo el cuarto. En un espacio con eco el resultado
será peor que con un dinámico de la mitad de precio.</p>
<p><a href="../behringer-c1-vs-c3/">Comparativa detallada C-1 vs C-3 →</a></p>
</div>

<h2 id="media">Gama media: 70 a 160 USD</h2>

<div class="card">
<h3>Condensador USB de escritorio</h3>
<p><span class="pill">Condensador</span><span class="pill">USB</span><span class="pill">Plug and play</span></p>
<p>Es la categoría más vendida del streaming: cuerpo metálico, base propia, salida de
auriculares con monitoreo directo y control de ganancia en el mismo micro. Familias
típicas: Blue Yeti, HyperX QuadCast, Rode NT-USB Mini, Audio-Technica AT2020USB.</p>
<p><strong>Por qué gana:</strong> cero fricción. Lo enchufas, ajustas ganancia y ya
tienes un sonido claramente superior al de unos auriculares gaming.</p>
<p><strong>Pega real:</strong> muchos vienen en omnidireccional o multipatrón y la gente
los deja mal configurados. Ponlo en cardioide siempre. Y la base de escritorio transmite
golpes: pásalo a brazo en cuanto puedas.</p>
</div>

<div class="card">
<h3>Dinámico XLR de radio</h3>
<p><span class="pill ok">Mejor sonido por dólar</span><span class="pill">Dinámico</span><span class="pill">XLR</span></p>
<p>Aquí entran los clásicos de broadcast tipo Shure SM58 / SM48 y equivalentes. Son
indestructibles, rechazan ambiente de forma ejemplar y envejecen muy bien: un micro de
este tipo te dura quince años.</p>
<p><strong>Por qué gana:</strong> es el sonido que asocias con «locutor profesional».</p>
<p><strong>Pega real:</strong> pide mucha ganancia limpia. Con una interfaz barata y
ruidosa puedes necesitar un preamplificador adicional, lo que suma coste.</p>
</div>

<h2 id="alta">Gama alta: 160 USD en adelante</h2>

<div class="card">
<h3>Dinámico de broadcast con interfaz decente</h3>
<p><span class="pill">Dinámico</span><span class="pill">XLR</span><span class="pill">Cuarto sin tratar OK</span></p>
<p>La configuración estándar de los streamers grandes: un dinámico de difusión (familia
Shure SM7B, Rode PodMic, Electro-Voice RE20) sobre brazo con muelle, más una interfaz
con preamplificadores silenciosos. Aguanta gritos, risas y cuartos imperfectos.</p>
<p><strong>Presupuesta el conjunto completo:</strong> el micro suele ser menos de la
mitad del gasto. Brazo robusto, cable XLR de calidad e interfaz con ganancia de sobra
son parte del paquete, no accesorios opcionales.</p>
</div>

<div class="card">
<h3>Condensador de diafragma grande en cuarto tratado</h3>
<p><span class="pill">Condensador</span><span class="pill">Requiere tratamiento acústico</span></p>
<p>Si grabas voz en off, cantas o tu contenido depende del detalle de la voz, un
condensador de diafragma grande con el cuarto tratado es otro nivel. Fuera de esas
condiciones, es dinero mal invertido.</p>
</div>

<h2 id="tabla">Tabla comparativa</h2>
<table>
<thead><tr><th>Perfil</th><th>Tipo</th><th>Conexión</th><th>Rango orientativo</th><th>Ideal si…</th></tr></thead>
<tbody>
<tr><td>Dinámico USB de entrada</td><td>Dinámico</td><td>USB (+XLR)</td><td>50-70 USD</td><td>Empiezas y el cuarto es ruidoso</td></tr>
<tr><td>Condensador XLR económico</td><td>Condensador</td><td>XLR</td><td>40-80 USD</td><td>Ya tienes interfaz con phantom</td></tr>
<tr><td>Condensador USB de escritorio</td><td>Condensador</td><td>USB</td><td>80-160 USD</td><td>Quieres cero complicación</td></tr>
<tr><td>Dinámico XLR de radio</td><td>Dinámico</td><td>XLR</td><td>100-160 USD</td><td>Buscas voz de locutor y durabilidad</td></tr>
<tr><td>Dinámico de broadcast</td><td>Dinámico</td><td>XLR</td><td>250-450 USD</td><td>Transmites a diario y ya tienes interfaz</td></tr>
<tr><td>Condensador de diafragma grande</td><td>Condensador</td><td>XLR</td><td>200 USD+</td><td>Tienes el cuarto tratado</td></tr>
</tbody></table>

<h2 id="veredicto">Veredicto rápido</h2>
<div class="note">
<p><strong>Si solo quieres la respuesta:</strong> cuarto normal y presupuesto normal →
dinámico cardioide con salida USB y XLR, sobre brazo articulado. Es la decisión que
menos gente lamenta.</p>
</div>
<p>¿Sigues dudando entre conexiones? Lee la
<a href="../usb-o-xlr/">comparativa USB vs XLR</a>. ¿Presupuesto muy justo? Empieza por
<a href="../micros-streaming-baratos/">micros baratos que no suenan baratos</a>.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["microfono-condensador/"] = {
    "title": "Micrófono de condensador: cómo elegirlo (y cuándo no comprarlo)",
    "desc": ("Qué es un micrófono de condensador, por qué necesita phantom 48 V, "
             "diafragma grande o pequeño y en qué cuartos es mala idea."),
    "h1": "Micrófono de condensador: guía sin humo",
    "crumb": "Condensador",
    "article": True,
    "lede": ("El condensador es el micro que más detalle da y el que más problemas "
             "causa en un cuarto sin tratar. Aquí está la línea exacta entre una cosa "
             "y la otra."),
    "toc": [
        ("como-funciona", "Cómo funciona"),
        ("phantom", "Alimentación phantom 48 V"),
        ("diafragma", "Diafragma grande o pequeño"),
        ("cuando-no", "Cuándo NO comprarlo"),
        ("configurar", "Cómo configurarlo bien"),
    ],
    "faq": [
        ("¿Qué es un micrófono de condensador?",
         "Es un micrófono cuya cápsula funciona como un condensador eléctrico: un "
         "diafragma muy fino se mueve frente a una placa fija y ese movimiento cambia "
         "la capacitancia, generando la señal. Al tener una masa mínima, responde a "
         "detalles y frecuencias altas que un dinámico pierde."),
        ("¿Todos los condensadores necesitan 48 V?",
         "Los condensadores de estudio con XLR sí necesitan alimentación phantom de "
         "48 V desde la interfaz o mezclador. Los condensadores USB y los de electret "
         "con pila no la necesitan porque se alimentan por el puerto o la batería."),
        ("¿Un condensador es mejor que un dinámico?",
         "No en términos absolutos: es más sensible y más detallado, lo cual es una "
         "ventaja en un cuarto silencioso y una desventaja en uno ruidoso. Para "
         "streaming en un dormitorio con ventilador y teclado mecánico, un dinámico "
         "suele dar mejor resultado final."),
        ("¿Puedo conectar un condensador XLR directo al PC con un adaptador?",
         "Técnicamente entra, pero no funcionará bien: la entrada de micro del PC no "
         "entrega phantom de 48 V ni tiene el preamplificador adecuado. Necesitas una "
         "interfaz de audio."),
    ],
    "body": """
<h2 id="como-funciona">Cómo funciona</h2>
<p>Dentro de un <strong>micrófono de condensador</strong> hay un diafragma
extremadamente fino, metalizado, suspendido a muy poca distancia de una placa metálica
fija. Los dos forman un condensador eléctrico. Cuando el sonido mueve el diafragma, la
distancia entre placas cambia, la capacitancia cambia y de ahí sale la señal.</p>
<p>La consecuencia práctica es una sola: el elemento que se mueve pesa casi nada, así
que reacciona a matices que una bobina de cobre nunca alcanzaría. Eso es el «aire» y
el detalle que oyes en una voz en off profesional.</p>
<p>Y la contrapartida es la misma frase vista al revés: también reacciona al aire
acondicionado, al eco de la pared de enfrente y a la moto de la calle.</p>

<h2 id="phantom">Alimentación phantom 48 V</h2>
<p>El circuito interno necesita corriente. Esa corriente viaja por el propio cable XLR
desde la interfaz: son los <strong>48 voltios de alimentación phantom</strong>, casi
siempre marcados como <code>+48V</code> o <code>P48</code> en un botón de la interfaz.</p>
<ul class="checks">
<li>Conecta el cable XLR <em>antes</em> de activar el phantom.</li>
<li>Apaga el phantom y espera unos segundos antes de desconectar.</li>
<li>Baja el volumen de tus auriculares al activarlo: suele soltar un golpe fuerte.</li>
<li>Un micrófono <strong>dinámico</strong> no necesita phantom, pero tampoco se daña
con él en una interfaz moderna y con cable balanceado correcto.</li>
</ul>
<div class="note">Si tu condensador «no se oye», la causa número uno no es el micro:
es el botón de 48 V apagado.</div>

<h2 id="diafragma">Diafragma grande o pequeño</h2>
<table>
<thead><tr><th></th><th>Diafragma grande (LDC)</th><th>Diafragma pequeño (SDC)</th></tr></thead>
<tbody>
<tr><td>Forma típica</td><td>Cuerpo ancho, rejilla grande</td><td>Lápiz delgado</td></tr>
<tr><td>Carácter</td><td>Voz con cuerpo, graves llenos</td><td>Muy preciso y neutro</td></tr>
<tr><td>Efecto proximidad</td><td>Marcado: cerca suena grave y grande</td><td>Leve</td></tr>
<tr><td>Uso habitual</td><td>Voz, locución, streaming, canto</td><td>Acústicas, platillos, ambientes</td></tr>
</tbody></table>
<p>Para streaming y podcast, si eliges condensador, quieres <strong>diafragma grande y
patrón cardioide</strong>. El resto de opciones son para grabación musical.</p>

<h2 id="cuando-no">Cuándo NO comprar un condensador</h2>
<p>Sé honesto con estas cinco preguntas. Si respondes «sí» a dos o más, compra un
dinámico:</p>
<ul class="checks">
<li>¿Tu cuarto tiene paredes desnudas y suelo duro?</li>
<li>¿Se oye eco cuando aplaudes en el centro de la habitación?</li>
<li>¿Hay ventilador, aire acondicionado o un PC ruidoso cerca?</li>
<li>¿Transmites con ruido de calle, familia o mascotas de fondo?</li>
<li>¿Usas teclado mecánico en directo?</li>
</ul>
<p>El condensador no «filtra» nada de eso: lo amplifica con fidelidad. Un dinámico a
5-10 cm de la boca sí lo deja fuera, simplemente porque no alcanza a captarlo.</p>

<h2 id="configurar">Cómo configurarlo bien</h2>
<ol>
<li><strong>Orientación.</strong> Un condensador de diafragma grande capta por el
<em>lado</em>, no por la punta. Habla hacia la cara donde está el logotipo.</li>
<li><strong>Distancia.</strong> Entre 10 y 20 cm. Más cerca y el efecto de proximidad
te enturbia los graves; más lejos y entra el cuarto.</li>
<li><strong>Fuera de eje.</strong> Gíralo unos 15-20 grados respecto a tu boca para
evitar las explosivas.</li>
<li><strong>Filtro antipop.</strong> Obligatorio, y a un palmo del micro, no pegado.</li>
<li><strong>Suspensión elástica.</strong> La araña aísla los golpes de mesa. Con
condensador se nota mucho más que con dinámico.</li>
<li><strong>Filtro paso alto en 80 Hz.</strong> Elimina retumbe de tráfico y mesa sin
tocar tu voz.</li>
</ol>
<p>¿Buscas modelos concretos? Hay dos muy preguntados en la gama baja:
<a href="../behringer-c1-vs-c3/">Behringer C-1 vs C-3</a>. Y si esto te suena a
demasiado cable, compara antes
<a href="../usb-o-xlr/">USB frente a XLR</a>.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["usb-o-xlr/"] = {
    "title": "Micrófono USB o XLR para streaming: cuál te conviene",
    "desc": ("USB vs XLR para streaming: coste total real, latencia, calidad, "
             "invitados y cuándo merece la pena dar el salto a interfaz."),
    "h1": "Micrófono USB o XLR: la decisión de verdad",
    "crumb": "USB o XLR",
    "article": True,
    "lede": ("No es una discusión de calidad. Es una discusión de coste total, "
             "flexibilidad y cuánto quieres aprender de audio."),
    "toc": [
        ("diferencia", "La diferencia real"),
        ("coste", "Coste total, no precio del micro"),
        ("mitos", "Tres mitos"),
        ("elige", "Elige en 30 segundos"),
        ("migrar", "Cómo migrar de USB a XLR"),
    ],
    "faq": [
        ("¿Suena mejor XLR que USB?",
         "No por la conexión en sí. Un micro USB de gama media puede sonar mejor que un "
         "XLR barato con una interfaz mala. XLR gana porque te da acceso a cápsulas y "
         "preamplificadores mejores, y porque puedes actualizar cada pieza por separado."),
        ("¿Puedo usar dos micrófonos USB a la vez en OBS?",
         "Sí, OBS admite varias fuentes de audio, pero es frágil: cada micro USB tiene "
         "su propio reloj y pueden desincronizarse en grabaciones largas. Para dos o más "
         "voces, una interfaz XLR de dos entradas es la solución estable."),
        ("¿Qué interfaz necesito para empezar con XLR?",
         "Una interfaz de dos entradas con phantom 48 V y salida de auriculares con "
         "monitoreo directo cubre el 95 % de los casos de streaming. Lo importante es "
         "que tenga ganancia suficiente y silenciosa si usas un dinámico."),
    ],
    "body": """
<h2 id="diferencia">La diferencia real</h2>
<p>Un <strong>micrófono USB</strong> lleva dentro lo que en XLR es una caja aparte:
preamplificador, conversor analógico-digital y tarjeta de sonido. Por eso funciona solo.</p>
<p>Un <strong>micrófono XLR</strong> entrega señal analógica balanceada y nada más. La
interfaz hace el resto del trabajo.</p>
<table>
<thead><tr><th></th><th>USB</th><th>XLR</th></tr></thead>
<tbody>
<tr><td>Instalación</td><td>Enchufar y listo</td><td>Interfaz, cable, drivers, ganancia</td></tr>
<tr><td>Coste de entrada</td><td>Bajo</td><td>Medio-alto</td></tr>
<tr><td>Actualizable por piezas</td><td>No</td><td>Sí</td></tr>
<tr><td>Varios micrófonos</td><td>Problemático</td><td>Nativo</td></tr>
<tr><td>Longitud de cable</td><td>~3 m sin amplificador</td><td>Decenas de metros sin pérdida</td></tr>
<tr><td>Monitoreo sin latencia</td><td>Solo en modelos con salida de auriculares</td><td>Sí, en la interfaz</td></tr>
<tr><td>Reventa</td><td>Pierde valor</td><td>Conserva valor muy bien</td></tr>
</tbody></table>

<h2 id="coste">Coste total, no precio del micro</h2>
<p>El error clásico es comparar el precio del micrófono. Compara el sistema completo:</p>
<table>
<thead><tr><th>Concepto</th><th>Ruta USB</th><th>Ruta XLR</th></tr></thead>
<tbody>
<tr><td>Micrófono</td><td>80-160 USD</td><td>60-160 USD</td></tr>
<tr><td>Interfaz de audio</td><td>—</td><td>90-180 USD</td></tr>
<tr><td>Cable XLR</td><td>—</td><td>10-25 USD</td></tr>
<tr><td>Brazo articulado</td><td>25-60 USD</td><td>25-60 USD</td></tr>
<tr><td>Filtro antipop</td><td>8-20 USD</td><td>8-20 USD</td></tr>
<tr><td><strong>Total aproximado</strong></td><td><strong>115-240 USD</strong></td><td><strong>195-445 USD</strong></td></tr>
</tbody></table>
<p>La ruta XLR cuesta grosso modo el doble para empezar. Lo que compras con esa
diferencia no es sonido inmediato: es techo. Dentro de dos años podrás cambiar solo el
micro, o solo la interfaz, o añadir un invitado.</p>

<h2 id="mitos">Tres mitos</h2>
<div class="card">
<h3>«USB es para aficionados»</h3>
<p>Falso. Hay micros USB con conversores excelentes que superan a combinaciones XLR
mal elegidas. La conexión no determina la calidad de la cápsula.</p>
</div>
<div class="card">
<h3>«XLR no tiene latencia»</h3>
<p>Impreciso. La latencia la introduce el conversor y el buffer del sistema, no el
conector. La ventaja real de una interfaz es el <em>monitoreo directo</em>: escuchas la
señal analógica antes de que entre al ordenador. Varios micros USB también lo llevan.</p>
</div>
<div class="card">
<h3>«Con un adaptador XLR a jack de 3,5 mm me ahorro la interfaz»</h3>
<p>No funciona bien. Esa entrada del PC no entrega phantom, no tiene ganancia suficiente
para un dinámico y suele ser ruidosa. Es el atajo que más devoluciones causa.</p>
</div>

<h2 id="elige">Elige en 30 segundos</h2>
<ul class="checks">
<li><strong>Elige USB si:</strong> transmites tú solo, quieres empezar esta semana, tu
espacio es limitado o viajas con el equipo.</li>
<li><strong>Elige XLR si:</strong> tendrás invitados presenciales, ya te interesa el
audio, quieres un micro que dure diez años, o vas a grabar además de transmitir.</li>
<li><strong>Elige un híbrido USB+XLR si:</strong> no lo tienes claro. Existen y son la
mejor forma de no equivocarse: empiezas por USB y migras a interfaz sin cambiar el
micrófono.</li>
</ul>

<h2 id="migrar">Cómo migrar de USB a XLR sin tirar dinero</h2>
<ol>
<li>Compra hoy un micro con doble salida USB y XLR.</li>
<li>Invierte primero en brazo y tratamiento acústico: eso sirve en las dos rutas.</li>
<li>Cuando notes el límite (invitado, segundo micro, ruido de puerto USB), añade la
interfaz.</li>
<li>Reutiliza el mismo micro por XLR y vende nada.</li>
</ol>
<p>Siguiente paso: la <a href="../mejores-micros-streaming/">comparativa por
presupuesto</a>, o la guía de <a href="../microfono-condensador/">condensadores</a> si
te tienta la ruta de estudio.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["micros-streaming-baratos/"] = {
    "title": "Micros de streaming baratos que no suenan baratos",
    "desc": ("Cómo conseguir audio decente para streaming con poco presupuesto: "
             "qué recortar, qué no, y los ajustes gratis que más se notan."),
    "h1": "Micros baratos para streaming: dónde sí se puede recortar",
    "crumb": "Baratos",
    "article": True,
    "lede": ("Con presupuesto corto, el orden de compra importa más que la marca. "
             "Esta es la secuencia que da el mejor sonido por cada peso gastado."),
    "toc": [
        ("orden", "El orden correcto de gasto"),
        ("recortar", "Qué recortar sin pagar el precio"),
        ("no-recortar", "Qué NO recortar nunca"),
        ("gratis", "Mejoras que cuestan cero"),
        ("segunda-mano", "Segunda mano: qué revisar"),
    ],
    "faq": [
        ("¿Cuánto cuesta como mínimo sonar bien en streaming?",
         "Con un dinámico USB de entrada, un brazo sencillo y un filtro antipop se "
         "consigue un sonido claramente competente por menos de 100 dólares en total. "
         "Por debajo de eso, la mayor mejora es gratis: acercarte al micro y bajar la "
         "ganancia."),
        ("¿Los micrófonos de solapa baratos sirven para transmitir?",
         "Para streaming móvil o contenido en movimiento, sí. Para un directo sentado "
         "frente al PC, no: al ir sobre la ropa captan roce y quedan lejos de la boca, "
         "lo que deja entrar más cuarto que un micro de escritorio bien colocado."),
        ("¿Vale la pena comprar un micro usado?",
         "Los dinámicos usados son una compra excelente porque casi no tienen piezas "
         "que se degraden. Los condensadores usados son más delicados: la humedad y los "
         "golpes afectan a la cápsula, y no siempre se detecta a simple vista."),
    ],
    "body": """
<h2 id="orden">El orden correcto de gasto</h2>
<p>Si tienes 100 dólares, no los pongas todos en el micrófono. El reparto que mejor
funciona en la práctica:</p>
<table>
<thead><tr><th>Prioridad</th><th>Concepto</th><th>Porción del presupuesto</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>1</td><td>Micrófono dinámico cardioide</td><td>~60 %</td><td>Es la base y define el techo</td></tr>
<tr><td>2</td><td>Brazo articulado o soporte firme</td><td>~25 %</td><td>Te permite acercarte sin golpes de mesa</td></tr>
<tr><td>3</td><td>Filtro antipop</td><td>~10 %</td><td>Deja hablar cerca sin explosivas</td></tr>
<tr><td>4</td><td>Absorción casera</td><td>~5 % o cero</td><td>Cortina, cojines, estantería</td></tr>
</tbody></table>
<div class="note">Un micrófono de 60 dólares a 8 cm de la boca sobre un brazo suena
mejor que uno de 150 dólares tirado en la mesa a medio metro. Sin excepción.</div>

<h2 id="recortar">Qué recortar sin pagar el precio</h2>
<ul class="checks">
<li><strong>Iluminación RGB.</strong> No aporta nada al audio y encarece bastante.</li>
<li><strong>Multipatrón.</strong> Vas a usar cardioide el 100 % del tiempo.</li>
<li><strong>Pantalla o controles táctiles.</strong> Un potenciómetro físico basta.</li>
<li><strong>Marca del cable XLR.</strong> Cualquier cable balanceado decente y bien
soldado cumple; no existe diferencia audible entre un cable correcto y uno caro.</li>
<li><strong>Mezcladores de streaming.</strong> OBS hace el enrutamiento gratis.</li>
</ul>

<h2 id="no-recortar">Qué NO recortar nunca</h2>
<ul class="checks">
<li><strong>El soporte.</strong> Un brazo flojo que se vence es dinero perdido dos
veces: lo acabas reemplazando.</li>
<li><strong>El patrón cardioide.</strong> Los micros omnidireccionales de bazar son la
causa más frecuente de «se me oye con eco».</li>
<li><strong>La ganancia limpia.</strong> Si eliges dinámico XLR, una interfaz sin
ganancia suficiente arruina el conjunto. Ahí sí conviene estirarse.</li>
<li><strong>Los auriculares para monitorear.</strong> Sin escucharte, no puedes
corregir nada.</li>
</ul>

<h2 id="gratis">Mejoras que cuestan cero</h2>
<ol>
<li><strong>Acércate.</strong> De 40 cm a 10 cm es la mejora más grande disponible.</li>
<li><strong>Baja la ganancia.</strong> Picos a -12 dB; el resto lo hace el compresor.</li>
<li><strong>Apunta fuera de eje.</strong> Adiós a las «p» y las «b» explosivas.</li>
<li><strong>Mueve el ventilador del PC.</strong> O al menos gíralo para que el micro
no lo mire de frente.</li>
<li><strong>Cierra la ventana y apaga el aire durante el directo.</strong></li>
<li><strong>Filtro paso alto a 80 Hz</strong> en OBS. Elimina retumbe sin tocar tu voz.</li>
<li><strong>Compresor suave</strong> con ratio 3:1 y unos 6 dB de reducción máxima.</li>
<li><strong>Cuelga una manta o cortina</strong> en la pared que tienes enfrente. Es
absorción acústica real y gratis.</li>
</ol>

<h2 id="segunda-mano">Segunda mano: qué revisar</h2>
<ul class="checks">
<li><strong>Rejilla abollada:</strong> en dinámicos suele ser cosmético; en
condensadores puede haber tocado el diafragma.</li>
<li><strong>Pines XLR:</strong> deben estar rectos y sin verdín.</li>
<li><strong>Ruido de fondo:</strong> pide una grabación de 20 segundos en silencio.
Un siseo fuerte con ganancia media indica electrónica dañada.</li>
<li><strong>Condensadores guardados en sótano o garaje:</strong> desconfía, la humedad
es su peor enemigo.</li>
<li><strong>Accesorios:</strong> la araña y el adaptador de rosca originales valen
dinero; que estén incluidos cambia el trato.</li>
</ul>
<p>¿Ya tienes claro el presupuesto? Pasa a la
<a href="../mejores-micros-streaming/">comparativa por rangos de precio</a>.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["microfono-para-telefono/"] = {
    "title": "Micrófono para teléfono: cómo transmitir con buen audio desde el móvil",
    "desc": ("Guía de micrófono para teléfono: solapa, USB-C, Lightning, "
             "adaptadores TRRS y ajustes para que el directo desde el móvil se oiga bien."),
    "h1": "Micrófono para teléfono: audio decente desde el móvil",
    "crumb": "Micrófono para teléfono",
    "article": True,
    "lede": ("El móvil es una cámara estupenda con un micrófono mediocre. Cambiar solo "
             "esa pieza transforma por completo un directo desde el celular."),
    "toc": [
        ("conexiones", "Conexiones: TRRS, USB-C y Lightning"),
        ("tipos", "Tipos de micrófono para móvil"),
        ("elegir", "Cuál elegir según el contenido"),
        ("ajustes", "Ajustes en el teléfono"),
        ("errores", "Errores típicos"),
    ],
    "faq": [
        ("¿Cualquier micrófono funciona con mi teléfono?",
         "No. Un micro con jack TRS de cámara no funciona en el conector del móvil sin "
         "un adaptador TRRS, y un micro XLR necesita una interfaz compatible con el "
         "teléfono. Las opciones directas son los micros con conector USB-C o Lightning "
         "y los de solapa TRRS."),
        ("¿Por qué mi micro de solapa no se oye al conectarlo al teléfono?",
         "Casi siempre es un problema de configuración de conector: el teléfono espera "
         "una clavija TRRS de cuatro contactos con el micro en el anillo correcto. Con "
         "una TRS de tres contactos el teléfono no detecta entrada y sigue usando su "
         "micrófono interno."),
        ("¿Se puede usar un micrófono USB con un teléfono Android?",
         "En muchos Android sí, mediante un adaptador USB-C OTG, siempre que el "
         "micrófono no consuma más corriente de la que el teléfono puede entregar. "
         "Los modelos con alto consumo pueden requerir un hub con alimentación externa."),
    ],
    "body": """
<h2 id="conexiones">Conexiones: TRRS, USB-C y Lightning</h2>
<p>Antes de mirar modelos, identifica qué entra en tu teléfono:</p>
<table>
<thead><tr><th>Conexión</th><th>Qué es</th><th>Ventaja</th><th>Pega</th></tr></thead>
<tbody>
<tr><td>TRRS 3,5 mm</td><td>Jack de cuatro contactos (audio + micro)</td><td>Barato y universal en móviles con jack</td><td>Señal analógica; muchos teléfonos ya no tienen jack</td></tr>
<tr><td>USB-C digital</td><td>El micro lleva su propio conversor</td><td>Mejor señal, sin ruido analógico del teléfono</td><td>Ocupa el puerto de carga</td></tr>
<tr><td>Lightning</td><td>Equivalente en iPhone antiguos</td><td>Integración limpia con iOS</td><td>Accesorios más caros y específicos</td></tr>
<tr><td>Inalámbrico 2,4 GHz</td><td>Transmisor de solapa + receptor</td><td>Libertad de movimiento</td><td>Baterías, emparejamiento e interferencias</td></tr>
</tbody></table>
<div class="note">Si tu micrófono trae jack <strong>TRS</strong> (tres contactos, típico
de micros de cámara) y tu teléfono pide <strong>TRRS</strong>, necesitas un adaptador
TRS→TRRS. No es opcional: sin él el teléfono ignora el micrófono.</div>

<h2 id="tipos">Tipos de micrófono para móvil</h2>

<div class="card">
<h3>Solapa (lavalier) con cable</h3>
<p><span class="pill ok">Mejor relación calidad-precio</span></p>
<p>Va prendido a la ropa, a unos 15-20 cm de la boca. Al estar tan cerca, deja fuera
casi todo el ambiente. Es la mejora más grande y más barata para vídeo hablado.</p>
<p><strong>Cuidado con:</strong> el roce de la tela. Pásalo por debajo de la camiseta y
fíjalo con una pinza o un poco de cinta.</p>
</div>

<div class="card">
<h3>Solapa inalámbrico</h3>
<p>Transmisor con pinza y receptor que se conecta al teléfono. Perfecto para contenido
en movimiento, calle, cocina o gimnasio.</p>
<p><strong>Cuidado con:</strong> la autonomía y las zonas con mucho wifi, que pueden
causar cortes en 2,4 GHz.</p>
</div>

<div class="card">
<h3>Micrófono de cañón sobre el teléfono</h3>
<p>Se monta en una jaula o soporte y apunta hacia quien habla. Bueno para entrevistas y
grabación a un metro de distancia.</p>
<p><strong>Cuidado con:</strong> el viento. Sin paravientos de espuma o peludo, en
exteriores es inservible.</p>
</div>

<div class="card">
<h3>Micrófono USB de escritorio conectado por OTG</h3>
<p>Si transmites desde el móvil pero sentado en un escritorio, un micro USB por
adaptador USB-C OTG es lo que mejor suena. Comprueba antes el consumo del micrófono.</p>
</div>

<h2 id="elegir">Cuál elegir según el contenido</h2>
<ul class="checks">
<li><strong>Directo sentado frente al teléfono:</strong> micro USB por OTG o un
condensador USB pequeño.</li>
<li><strong>Vídeo hablando a cámara, quieto:</strong> solapa con cable. Discreto y barato.</li>
<li><strong>Contenido en movimiento o exteriores:</strong> solapa inalámbrico con
paravientos.</li>
<li><strong>Entrevistas a dos:</strong> kit de dos solapas o dos transmisores a un
receptor de dos canales.</li>
<li><strong>Música o ambiente:</strong> micro estéreo sobre el teléfono; el micro
interno no tiene rango dinámico para eso.</li>
</ul>

<h2 id="ajustes">Ajustes en el teléfono</h2>
<ol>
<li><strong>Comprueba que el teléfono está usando el micro externo.</strong> Graba diez
segundos, tapa el micrófono externo con la mano y mira si el sonido baja. Si no baja,
está usando el interno.</li>
<li><strong>Desactiva la reducción de ruido agresiva</strong> si tu app de cámara la
ofrece: con un micro externo bueno, hace más daño que bien.</li>
<li><strong>Bloquea la exposición y el enfoque</strong> para que el móvil no cambie de
micrófono al recomponer la escena.</li>
<li><strong>Modo avión + wifi</strong> durante grabaciones para evitar interferencias
en cables analógicos.</li>
<li><strong>Usa una app con control manual de nivel</strong> si transmites en serio;
las cámaras nativas aplican control automático de ganancia que sube el ruido de fondo
en los silencios.</li>
</ol>

<h2 id="errores">Errores típicos</h2>
<ul class="checks">
<li>Usar un adaptador de carga + audio de mala calidad: introduce zumbido.</li>
<li>Dejar el solapa por fuera de la ropa expuesto al viento, sin peluche.</li>
<li>Grabar con el teléfono en un trípode a dos metros y confiar en el micro interno.</li>
<li>Olvidar que el conector USB-C queda ocupado: en directos largos la batería manda.</li>
</ul>
<p>¿Vas a montar también una configuración de escritorio? Empieza por la
<a href="../mejores-micros-streaming/">comparativa de micros para streaming</a>.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["behringer-c1-vs-c3/"] = {
    "title": "Behringer C-1 vs C-3: cuál comprar para voz y streaming",
    "desc": ("Comparativa Behringer C-1 y C-3: diferencias de patrón polar, "
             "accesorios, uso recomendado y qué necesitas además del micrófono."),
    "h1": "Behringer C-1 vs C-3: diferencias reales",
    "crumb": "Behringer C-1 vs C-3",
    "article": True,
    "lede": ("Dos condensadores de diafragma grande muy baratos y muy buscados. La "
             "diferencia principal no es la calidad de sonido: es la flexibilidad."),
    "toc": [
        ("resumen", "Resumen rápido"),
        ("diferencias", "Diferencias punto por punto"),
        ("necesitas", "Lo que necesitas además del micro"),
        ("cual", "Cuál te conviene"),
        ("alternativas", "Cuándo mirar otra cosa"),
    ],
    "faq": [
        ("¿Cuál es la diferencia entre el Behringer C-1 y el C-3?",
         "El C-1 es un condensador de diafragma grande con patrón cardioide fijo. El "
         "C-3 es de doble diafragma y ofrece patrones conmutables cardioide y "
         "omnidireccional, además de atenuación e interruptor de filtro de graves. Para "
         "voz sola, el C-1 cubre el caso; el C-3 añade opciones para grabación."),
        ("¿El Behringer C-1 necesita phantom?",
         "Sí. Es un condensador XLR y requiere alimentación phantom de 48 V desde una "
         "interfaz de audio o un mezclador. No funciona conectado directamente a la "
         "entrada de micrófono del ordenador."),
        ("¿Sirve el Behringer C-1 para streaming?",
         "Sirve si tu cuarto es silencioso y ya tienes interfaz. Al ser un condensador "
         "sensible, en una habitación con eco, ventilador o teclado mecánico captará "
         "todo eso; en ese escenario un micrófono dinámico da mejor resultado final."),
    ],
    "body": """
<h2 id="resumen">Resumen rápido</h2>
<table>
<thead><tr><th></th><th>Behringer C-1</th><th>Behringer C-3</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador diafragma grande</td><td>Condensador doble diafragma</td></tr>
<tr><td>Patrón polar</td><td>Cardioide fijo</td><td>Cardioide u omnidireccional conmutable</td></tr>
<tr><td>Atenuación (pad)</td><td>No en el modelo básico</td><td>Sí, -10 dB</td></tr>
<tr><td>Filtro de graves</td><td>No</td><td>Sí, conmutable</td></tr>
<tr><td>Alimentación</td><td>Phantom 48 V</td><td>Phantom 48 V</td></tr>
<tr><td>Uso ideal</td><td>Voz, locución, streaming en cuarto silencioso</td><td>Voz, instrumentos, ambientes, parejas estéreo</td></tr>
<tr><td>Rango orientativo</td><td>40-70 USD</td><td>60-100 USD</td></tr>
</tbody></table>
<div class="note">Si solo vas a grabar tu voz, la diferencia de precio no te compra
mejor voz: te compra opciones que quizá nunca uses.</div>
<p>Fichas completas de cada uno: <a href="../behringer-c1/">Behringer C-1</a> ·
<a href="../behringer-c3/">Behringer C-3</a></p>

<h2 id="diferencias">Diferencias punto por punto</h2>

<h3>Patrón polar</h3>
<p>El C-1 es cardioide y punto. El C-3 puede pasar a omnidireccional con un
interruptor, lo que sirve para grabar una sala, una reunión alrededor de una mesa o
un instrumento con su ambiente.</p>
<p>Para streaming <strong>siempre querrás cardioide</strong>, así que esta ventaja del
C-3 es irrelevante en directo y valiosa solo si además grabas música.</p>

<h3>Atenuación y filtro de graves</h3>
<p>El pad de -10 dB del C-3 evita saturar la entrada con fuentes muy fuertes
(amplificadores, batería, gritos). El filtro de graves conmutable recorta el retumbe
desde el propio micrófono, algo que también puedes hacer por software en OBS.</p>

<h3>Carácter de sonido</h3>
<p>Ambos comparten la firma de la gama: brillo marcado en agudos y graves generosos por
efecto de proximidad. Es un sonido que favorece voces oscuras y castiga voces ya de por
sí sibilantes. Si tienes eses fuertes, prevé un de-esser suave.</p>

<h3>Accesorios incluidos</h3>
<p>Suelen venir con soporte rígido y maletín. Ojo: <strong>soporte rígido no es araña
elástica</strong>. Con un condensador, la suspensión elástica marca una diferencia
enorme frente a los golpes de mesa, y suele comprarse aparte.</p>

<h2 id="necesitas">Lo que necesitas además del micrófono</h2>
<ul class="checks">
<li><strong>Interfaz de audio con phantom 48 V.</strong> Innegociable.</li>
<li><strong>Cable XLR.</strong> No viene incluido en muchos paquetes.</li>
<li><strong>Araña antivibración</strong> compatible con el diámetro del cuerpo.</li>
<li><strong>Filtro antipop.</strong> Con condensador es imprescindible.</li>
<li><strong>Brazo articulado sólido.</strong> Estos micros pesan más que un USB de plástico.</li>
</ul>
<p>Súmalo todo antes de comparar con un dinámico USB: un C-1 «de 50 dólares» se
convierte fácilmente en 180-200 dólares de sistema.</p>

<h2 id="cual">Cuál te conviene</h2>
<ul class="checks">
<li><strong>Solo voz, streaming y podcast:</strong> C-1. El C-3 no te dará nada que uses.</li>
<li><strong>Voz + guitarra acústica + grabaciones varias:</strong> C-3, por el pad y el
patrón omni.</li>
<li><strong>Cuarto con eco o ruido:</strong> ninguno de los dos. Compra un dinámico.</li>
<li><strong>No tienes interfaz y no piensas comprarla:</strong> ninguno de los dos.
Mira micros USB.</li>
</ul>

<h2 id="alternativas">Cuándo mirar otra cosa</h2>
<p>Estos micros son una buena compra en un escenario muy concreto: cuarto tranquilo,
interfaz ya disponible y ganas de aprender. Fuera de ahí, hay dos caminos mejores:</p>
<ol>
<li>Si el cuarto es el problema → <a href="../mejores-micros-streaming/">dinámico
cardioide</a>, que perdona mucho más.</li>
<li>Si la complicación es el problema → <a href="../usb-o-xlr/">un micro USB</a>, sin
interfaz ni phantom.</li>
</ol>
<p>Y si quieres entender qué estás comprando exactamente, lee primero
<a href="../microfono-condensador/">cómo funciona un condensador</a>.</p>
""",
}

# --------------------------------------------------------------------------
PAGES["quienes-somos/"] = {
    "title": "Quiénes somos y cómo evaluamos | MicrosStreaming",
    "desc": ("Quiénes están detrás de MicrosStreaming, cómo elaboramos las guías de "
             "micrófonos y por qué no usamos enlaces de afiliación."),
    "h1": "Quiénes somos y cómo evaluamos",
    "crumb": "Quiénes somos",
    "lede": ("Un sitio pequeño e independiente sobre audio para streaming. Sin tienda, "
             "sin patrocinadores y sin puntuaciones inventadas."),
    "body": """
<h2 id="que-es">Qué es este sitio</h2>
<p>MicrosStreaming es un proyecto editorial independiente dedicado a una sola cosa:
ayudar a que un directo, un podcast o un vídeo se oigan bien sin gastar de más.</p>

<h2 id="metodo">Cómo elaboramos las guías</h2>
<ul class="checks">
<li><strong>Partimos de la decisión, no del producto.</strong> Primero explicamos el
criterio (patrón polar, tipo de cápsula, conexión) y solo después hablamos de categorías
de producto.</li>
<li><strong>Hablamos de categorías y familias de micrófonos</strong>, no de unidades
concretas que no hemos medido. Cuando citamos modelos, es como referencia de una
categoría, con sus limitaciones explícitas.</li>
<li><strong>Los precios son rangos orientativos.</strong> Cambian por país, tienda,
impuestos e importación. Verifícalos siempre antes de comprar.</li>
<li><strong>Decimos cuándo NO comprar algo.</strong> Buena parte de estas guías consiste
en explicar en qué situaciones un micrófono caro empeora el resultado.</li>
</ul>

<h2 id="independencia">Independencia</h2>
<p>No vendemos micrófonos. No usamos enlaces de afiliación. No aceptamos pago por
recomendar marcas ni publicamos contenido patrocinado. Si eso cambia alguna vez,
aparecerá indicado de forma visible en la página correspondiente.</p>

<h2 id="correcciones">Correcciones</h2>
<p>Si encuentras un error técnico en una guía, es un error que queremos corregir.
Puedes abrir una incidencia en el repositorio público del sitio en GitHub, donde vive
todo el código y el contenido de estas páginas.</p>

<h2 id="aviso">Aviso</h2>
<p>El contenido es informativo y general. Las condiciones acústicas de cada espacio
son distintas, y ninguna guía sustituye a probar el equipo en tu propio cuarto.</p>

<p><a href="../">Volver al inicio →</a></p>
""",
}

# --------------------------------------------------------------------------
# Pagina 404. No entra en PAGES porque no lleva URL propia ni va al sitemap.
NOT_FOUND = {
    "title": "Página no encontrada | MicrosStreaming",
    "desc": "Esta página no existe. Vuelve al inicio o busca en las guías.",
    "h1": "Esta página no existe",
    "crumb": "404",
    "lede": "El enlace que seguiste está roto o la página cambió de dirección.",
    "body": """
<h2>Prueba con estas guías</h2>
<div class="grid">
  <a class="tile" href="BASEURL/"><b>Inicio</b><span>Cómo elegir micrófono para streaming.</span></a>
  <a class="tile" href="BASEURL/mejores-micros-streaming/"><b>Mejores micros</b><span>Comparativa por presupuesto.</span></a>
  <a class="tile" href="BASEURL/usb-o-xlr/"><b>USB o XLR</b><span>Coste total y cuándo dar el salto.</span></a>
  <a class="tile" href="BASEURL/microfono-condensador/"><b>Condensador</b><span>Cómo elegirlo y cuándo evitarlo.</span></a>
  <a class="tile" href="BASEURL/micros-streaming-baratos/"><b>Baratos</b><span>Dónde sí se puede recortar.</span></a>
  <a class="tile" href="BASEURL/microfono-para-telefono/"><b>Para teléfono</b><span>Streaming desde el móvil.</span></a>
</div>
""".replace("BASEURL", SITE["base"]),
}
