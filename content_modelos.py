# -*- coding: utf-8 -*-
"""Paginas por modelo / consulta concreta.

Una pagina por palabra clave del planificador. Son las que reciben trafico
comercial, asi que son tambien las que llevaran fichas de producto y enlaces
de afiliado cuando el sitio tenga posicionamiento.
"""


def add_pages(PAGES, SITE):
    PAGES["por-modelo/"] = {
        "title": "Micrófonos por modelo: fichas y comparativas",
        "desc": ("Índice de micrófonos analizados uno a uno: Behringer C-1 y C-3, "
                 "Neumann, HyperX QuadCast, micrófonos array, electret y Shure."),
        "h1": "Micrófonos por modelo",
        "crumb": "Por modelo",
        "lede": ("Cada ficha explica para qué sirve ese micrófono en concreto, qué "
                 "necesita para funcionar y en qué caso es mala compra."),
        "body": """
<h2 id="condensadores-economicos">Condensadores económicos</h2>
<div class="grid">
  <a class="tile" href="../behringer-c1/"><b>Behringer C-1</b>
  <span>Condensador cardioide de diafragma grande. Precio, phantom y para qué sirve.</span></a>
  <a class="tile" href="../behringer-c3/"><b>Behringer C-3</b>
  <span>Doble diafragma, patrón conmutable, pad y filtro de graves.</span></a>
  <a class="tile" href="../behringer-c1-vs-c3/"><b>C-1 vs C-3</b>
  <span>La comparativa directa entre los dos.</span></a>
</div>

<h2 id="gama-alta">Gama alta</h2>
<div class="grid">
  <a class="tile" href="../microfono-condensador-neumann/"><b>Condensador Neumann</b>
  <span>Qué justifica el precio y cuándo no tiene sentido comprarlo.</span></a>
</div>

<h2 id="streaming-usb">Streaming USB</h2>
<div class="grid">
  <a class="tile" href="../hyperx-quadcast-rgb/"><b>HyperX QuadCast (RGB)</b>
  <span>El condensador USB con luces: qué aporta y qué pagas de más.</span></a>
</div>

<h2 id="otros-tipos">Otros tipos de micrófono</h2>
<div class="grid">
  <a class="tile" href="../microfono-array/"><b>Micrófono array</b>
  <span>Varias cápsulas trabajando juntas: videoconferencia, salas y portátiles.</span></a>
  <a class="tile" href="../microfono-electronico/"><b>Micrófono electrónico</b>
  <span>Qué significa de verdad ese término y qué estás comprando.</span></a>
  <a class="tile" href="../shure-antena/"><b>Antenas Shure</b>
  <span>Inalámbricos: antenas, distribuidores y por qué se cortan.</span></a>
</div>

<h2 id="como-usar">Cómo usar este índice</h2>
<p>Si todavía no sabes qué <em>tipo</em> de micrófono necesitas, empieza por la
<a href="../">guía general</a> o por <a href="../usb-o-xlr/">USB vs XLR</a>. Estas
fichas asumen que ya tienes claro el tipo y quieres decidir entre modelos.</p>
""",
    }

    PAGES["behringer-c1/"] = {
        "title": "Behringer C-1: análisis, precio y qué necesitas para usarlo",
        "desc": ("Behringer C-1: condensador cardioide de diafragma grande. Para qué "
                 "sirve, precio orientativo, phantom 48 V y accesorios necesarios."),
        "h1": "Behringer C-1: el condensador barato que sí vale la pena",
        "crumb": "Behringer C-1",
        "article": True,
        "lede": ("Un condensador de estudio por el precio de unos auriculares. La "
                 "trampa no está en el micro: está en todo lo que necesita alrededor."),
        "toc": [
            ("que-es", "Qué es y qué hace"),
            ("precio", "Precio y coste real"),
            ("necesitas", "Qué necesitas para usarlo"),
            ("suena", "Cómo suena"),
            ("para-quien", "Para quién sí y para quién no"),
        ],
        "faq": [
            ("¿Cuánto cuesta el Behringer C-1?",
             "Su precio internacional orientativo está entre 40 y 70 dólares, y varía "
             "bastante por país e importación. El dato importante es otro: necesita "
             "además interfaz con phantom de 48 V, cable XLR, araña y filtro antipop, "
             "así que el conjunto realista ronda los 180-200 dólares."),
            ("¿El Behringer C-1 necesita alimentación phantom?",
             "Sí. Es un condensador XLR y no funciona sin 48 V de phantom procedentes "
             "de una interfaz de audio o un mezclador. Conectado a la entrada de "
             "micrófono del ordenador no sonará, o lo hará con volumen ínfimo y mucho "
             "ruido."),
            ("¿Sirve el Behringer C-1 para cantar y grabar voz?",
             "Sí, es su uso natural: voz, locución y podcast en una sala tranquila. "
             "Tiene un carácter algo brillante, así que en voces con eses marcadas "
             "conviene suavizarlas con un de-esser."),
            ("¿El C-1 sirve para streaming en un cuarto normal?",
             "Solo si el cuarto es silencioso. Al ser un condensador sensible capta el "
             "eco, el ventilador y el teclado con la misma fidelidad que tu voz. En un "
             "cuarto vivo, un micrófono dinámico da mejor resultado final."),
        ],
        "body": """
<h2 id="que-es">Qué es y qué hace</h2>
<p>El <strong>Behringer C-1</strong> es un micrófono de condensador de diafragma
grande, con patrón <strong>cardioide fijo</strong> y conexión XLR. Está pensado para
grabación de voz e instrumentos en estudio casero.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador, diafragma grande</td></tr>
<tr><td>Patrón polar</td><td>Cardioide (fijo, no conmutable)</td></tr>
<tr><td>Conexión</td><td>XLR balanceada</td></tr>
<tr><td>Alimentación</td><td>Phantom +48 V obligatoria</td></tr>
<tr><td>Pad / filtro de graves</td><td>No</td></tr>
<tr><td>Incluye</td><td>Soporte rígido y maletín (según lote)</td></tr>
</tbody></table>

<h2 id="precio">Precio y coste real</h2>
<p>La etiqueta engaña. Esto es lo que cuesta ponerlo a funcionar de verdad:</p>
<table>
<thead><tr><th>Concepto</th><th>¿Obligatorio?</th><th>Rango orientativo</th></tr></thead>
<tbody>
<tr><td>Behringer C-1</td><td>Sí</td><td>40-70 USD</td></tr>
<tr><td>Interfaz de audio con phantom</td><td>Sí</td><td>90-180 USD</td></tr>
<tr><td>Cable XLR</td><td>Sí</td><td>10-25 USD</td></tr>
<tr><td>Araña antivibración</td><td>Muy recomendable</td><td>15-35 USD</td></tr>
<tr><td>Filtro antipop</td><td>Sí</td><td>8-20 USD</td></tr>
<tr><td>Brazo articulado</td><td>Recomendable</td><td>25-60 USD</td></tr>
</tbody></table>
<div class="note">Si no tienes ya una interfaz, el C-1 <em>no</em> es la opción barata.
Un micrófono USB de 90 dólares te deja transmitiendo esta misma tarde.</div>

<h2 id="necesitas">Qué necesitas para usarlo</h2>
<ul class="checks">
<li><strong>Interfaz o mezclador con botón +48V.</strong> Innegociable.</li>
<li><strong>Cable XLR macho-hembra.</strong> No suele venir incluido.</li>
<li><strong>Un sitio tranquilo.</strong> Es sensible: oirá lo que tú no oyes.</li>
<li><strong>Orden de encendido.</strong> Conecta el cable, sube el phantom; al
terminar, hazlo al revés y con el volumen bajado.</li>
<li><strong>Distancia de 10-20 cm</strong> y ligeramente fuera de eje.</li>
</ul>

<h2 id="suena">Cómo suena</h2>
<p>Tiene el perfil típico de la gama: <strong>agudos realzados</strong>, que dan
sensación de detalle, y <strong>graves generosos</strong> cuando te acercas, por efecto
de proximidad. Eso favorece a voces oscuras o apagadas y castiga a las voces ya
brillantes o sibilantes.</p>
<p>Con un filtro paso alto en 80 Hz, un compresor suave y un de-esser discreto queda
perfectamente presentable para podcast y voz en off.</p>

<h2 id="para-quien">Para quién sí y para quién no</h2>
<ul class="checks">
<li><strong>Sí</strong> si ya tienes interfaz y grabas voz en una sala tranquila.</li>
<li><strong>Sí</strong> como segundo micrófono para instrumentos acústicos.</li>
<li><strong>No</strong> si tu cuarto tiene eco o ruido: mira un
<a href="../mejores-micros-streaming/">dinámico</a>.</li>
<li><strong>No</strong> si no piensas comprar interfaz: mira
<a href="../usb-o-xlr/">micros USB</a>.</li>
</ul>
<p>¿Dudas con su hermano mayor? <a href="../behringer-c3/">Ficha del Behringer C-3</a>
o la <a href="../behringer-c1-vs-c3/">comparativa directa</a>.</p>
""",
    }

    PAGES["behringer-c3/"] = {
        "title": "Behringer C-3: análisis, patrones polares y para qué sirve",
        "desc": ("Behringer C-3: condensador de doble diafragma con patrón cardioide y "
                 "omnidireccional, pad de -10 dB y filtro de graves. Usos y límites."),
        "h1": "Behringer C-3: el C-1 con opciones",
        "crumb": "Behringer C-3",
        "article": True,
        "lede": ("Doble diafragma, dos patrones polares, atenuación y filtro de graves. "
                 "Útil si grabas algo más que tu voz; irrelevante si no."),
        "toc": [
            ("que-es", "Qué es y qué hace"),
            ("patrones", "Los dos patrones polares"),
            ("pad", "Pad y filtro de graves"),
            ("usos", "Usos donde brilla"),
            ("merece", "¿Merece la diferencia de precio?"),
        ],
        "faq": [
            ("¿Qué patrones polares tiene el Behringer C-3?",
             "Cardioide y omnidireccional, seleccionables con un interruptor en el "
             "cuerpo del micrófono. El cardioide capta de frente y rechaza por detrás; "
             "el omnidireccional capta por igual en todas direcciones."),
            ("¿Para qué sirve el pad de -10 dB del C-3?",
             "Atenúa la señal antes del preamplificador para que fuentes muy fuertes "
             "—un amplificador de guitarra, una batería, alguien gritando muy cerca— no "
             "saturen la entrada. En voz hablada normal no hace falta activarlo."),
            ("¿El C-3 es mejor que el C-1 para streaming?",
             "No en sonido. En directo usarás siempre cardioide, que es lo único que "
             "ofrece el C-1. Lo que añade el C-3 —omni, pad, filtro— solo se aprovecha "
             "grabando instrumentos o ambientes."),
        ],
        "body": """
<h2 id="que-es">Qué es y qué hace</h2>
<p>El <strong>Behringer C-3</strong> es un condensador de estudio con
<strong>dos diafragmas</strong> enfrentados. Esa construcción es la que permite
combinar las cápsulas para obtener distintos patrones polares.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador, doble diafragma</td></tr>
<tr><td>Patrones</td><td>Cardioide y omnidireccional (conmutables)</td></tr>
<tr><td>Atenuación</td><td>Pad de -10 dB</td></tr>
<tr><td>Filtro de graves</td><td>Conmutable</td></tr>
<tr><td>Conexión</td><td>XLR, phantom +48 V</td></tr>
<tr><td>Rango orientativo</td><td>60-100 USD</td></tr>
</tbody></table>

<h2 id="patrones">Los dos patrones polares</h2>
<table>
<thead><tr><th>Patrón</th><th>Capta</th><th>Úsalo para</th><th>Evítalo en</th></tr></thead>
<tbody>
<tr><td>Cardioide</td><td>Solo de frente</td><td>Voz, streaming, podcast, instrumento aislado</td><td>—</td></tr>
<tr><td>Omnidireccional</td><td>Todas las direcciones</td><td>Ambiente de sala, mesa con varias personas, guitarra con su acústica</td><td>Cualquier directo: te traerá todo el cuarto</td></tr>
</tbody></table>
<div class="note">Comprueba el interruptor antes de cada sesión. Muchos «se me oye con
eco» son en realidad un micrófono que quedó en omnidireccional.</div>

<h2 id="pad">Pad y filtro de graves</h2>
<p>El <strong>pad de -10 dB</strong> te salva cuando la fuente es muy fuerte: evita que
la señal sature la entrada de la interfaz. Para voz hablada a distancia normal déjalo
desactivado, porque atenuar de más te obliga a subir ganancia y con ella el ruido.</p>
<p>El <strong>filtro de graves</strong> recorta las frecuencias bajas desde el propio
micrófono. Es cómodo, aunque puedes conseguir lo mismo —y con más control— aplicando un
filtro paso alto en 80 Hz dentro de OBS o de tu grabador.</p>

<h2 id="usos">Usos donde brilla</h2>
<ul class="checks">
<li><strong>Guitarra acústica:</strong> cardioide apuntando al traste 12, a un palmo.</li>
<li><strong>Ambiente de sala:</strong> omni en el centro de la habitación.</li>
<li><strong>Entrevista en mesa:</strong> omni entre dos personas, si no hay eco.</li>
<li><strong>Percusión y fuentes fuertes:</strong> cardioide más pad de -10 dB.</li>
<li><strong>Voz y podcast:</strong> cardioide, igual que haría un C-1.</li>
</ul>

<h2 id="merece">¿Merece la diferencia de precio?</h2>
<p>Depende de una sola pregunta: <strong>¿vas a grabar algo que no sea tu voz?</strong></p>
<ul class="checks">
<li><strong>Solo voz, streaming o podcast:</strong> no. El
<a href="../behringer-c1/">C-1</a> hace lo mismo por menos.</li>
<li><strong>Voz + instrumentos + ambientes:</strong> sí, el pad y el patrón omni se
amortizan rápido.</li>
</ul>
<p>Los dos comparten el mismo requisito: interfaz con phantom. Si no la tienes, lee
antes <a href="../usb-o-xlr/">USB o XLR</a>. Comparación directa:
<a href="../behringer-c1-vs-c3/">C-1 vs C-3</a>.</p>
""",
    }

    PAGES["microfono-condensador-neumann/"] = {
        "title": "Micrófono de condensador Neumann: qué pagas y cuándo no compensa",
        "desc": ("Condensadores Neumann: por qué cuestan lo que cuestan, qué aportan "
                 "frente a un condensador barato y en qué casos no merecen la pena."),
        "h1": "Condensador Neumann: qué estás pagando realmente",
        "crumb": "Condensador Neumann",
        "article": True,
        "lede": ("La marca de referencia en voz de estudio. También la compra que más "
                 "se desperdicia cuando el cuarto y la cadena no están a la altura."),
        "toc": [
            ("por-que", "Por qué cuestan tanto"),
            ("diferencia", "Qué notas frente a uno barato"),
            ("cuando-no", "Cuándo NO compensa"),
            ("requisitos", "Qué necesita alrededor"),
            ("alternativas", "Si aún no es tu momento"),
        ],
        "faq": [
            ("¿Merece la pena un Neumann para streaming?",
             "Solo si el cuarto está tratado acústicamente y la cadena de audio ya es "
             "buena. En una habitación normal, el micrófono reproducirá esa habitación "
             "con enorme fidelidad, que es justo lo que no quieres en un directo."),
            ("¿Qué diferencia hay entre un Neumann y un condensador de 60 dólares?",
             "Principalmente consistencia y comportamiento fuera de eje: el ruido propio "
             "es menor, la respuesta es más pareja y el sonido no se descompone cuando "
             "te mueves respecto al micrófono. La diferencia se nota más en una mezcla "
             "y en cuartos buenos que en una escucha rápida."),
            ("¿Un Neumann necesita phantom de 48 V?",
             "Los modelos de condensador con salida XLR sí requieren alimentación "
             "phantom de 48 V desde una interfaz o mezclador, igual que cualquier otro "
             "condensador de estudio."),
        ],
        "body": """
<h2 id="por-que">Por qué cuestan tanto</h2>
<p>La diferencia de precio de un condensador de gama alta no está en el marketing, pero
tampoco está donde mucha gente cree. Se concentra en tres cosas:</p>
<ul class="checks">
<li><strong>Tolerancias de fabricación.</strong> Dos unidades del mismo modelo suenan
prácticamente igual. En la gama baja, la variación entre unidades es real.</li>
<li><strong>Ruido propio bajo.</strong> Puedes grabar fuentes suaves y subir ganancia
sin que aparezca un siseo de fondo.</li>
<li><strong>Comportamiento fuera de eje.</strong> Cuando te mueves o hablas de lado, el
sonido sigue siendo natural en vez de volverse metálico.</li>
</ul>

<h2 id="diferencia">Qué notas frente a uno barato</h2>
<table>
<thead><tr><th>Aspecto</th><th>Condensador económico</th><th>Condensador de gama alta</th></tr></thead>
<tbody>
<tr><td>Agudos</td><td>Realzados, a veces ásperos</td><td>Extendidos y sin dureza</td></tr>
<tr><td>Ruido propio</td><td>Audible con ganancia alta</td><td>Muy bajo</td></tr>
<tr><td>Fuera de eje</td><td>Se vuelve nasal o metálico</td><td>Se mantiene natural</td></tr>
<tr><td>Consistencia</td><td>Variable entre unidades</td><td>Muy alta</td></tr>
<tr><td>Perdona el cuarto</td><td>No</td><td>Tampoco. Lo empeora.</td></tr>
</tbody></table>
<div class="note">La última fila es la importante. Un micrófono mejor no disimula un
cuarto malo: lo retrata con más detalle.</div>

<h2 id="cuando-no">Cuándo NO compensa</h2>
<ul class="checks">
<li>El cuarto no tiene absorción y se oye eco al aplaudir.</li>
<li>Hay ruido constante: aire acondicionado, calle, PC, nevera.</li>
<li>La interfaz es de gama de entrada y mete ruido audible.</li>
<li>Tu contenido es hablado en directo y con teclado mecánico.</li>
<li>Todavía no tienes técnica estable de distancia y ángulo.</li>
</ul>
<p>En cualquiera de esos casos, el mismo dinero rinde muchísimo más repartido entre
tratamiento acústico, un brazo decente y una interfaz silenciosa.</p>

<h2 id="requisitos">Qué necesita alrededor</h2>
<ol>
<li><strong>Cuarto tratado:</strong> absorción en primeras reflexiones y detrás de ti.</li>
<li><strong>Interfaz con preamplificadores limpios</strong> y phantom de 48 V.</li>
<li><strong>Araña elástica y brazo firme:</strong> el micro pesa y es sensible a golpes.</li>
<li><strong>Filtro antipop</strong> a un palmo de la cápsula.</li>
<li><strong>Técnica constante:</strong> misma distancia y mismo ángulo en cada toma.</li>
</ol>

<h2 id="alternativas">Si aún no es tu momento</h2>
<p>No es un «no», es un «todavía no». El orden que más resultado da:</p>
<ol>
<li>Trata el cuarto (cortinas, paneles, estantería llena).</li>
<li>Consigue un <a href="../mejores-micros-streaming/">dinámico de broadcast</a>, que
perdona el ambiente.</li>
<li>Cuando el cuarto esté bien, pasa al condensador de gama alta.</li>
</ol>
<p>Antes de decidir, repasa <a href="../microfono-condensador/">cómo funciona un
condensador</a>.</p>
""",
    }

    PAGES["hyperx-quadcast-rgb/"] = {
        "title": "HyperX QuadCast RGB: análisis para streaming y qué pagas de más",
        "desc": ("HyperX QuadCast y QuadCast S RGB: patrones polares, antivibración, "
                 "silenciador táctil y si las luces justifican la diferencia."),
        "h1": "HyperX QuadCast RGB: el micro con luces, sin marketing",
        "crumb": "HyperX QuadCast",
        "article": True,
        "lede": ("Condensador USB pensado para streaming, con araña incorporada y "
                 "silenciador táctil. Lo bueno es real; el RGB, opcional."),
        "toc": [
            ("que-es", "Qué es"),
            ("bueno", "Lo que hace bien"),
            ("pegas", "Las pegas reales"),
            ("rgb", "¿El RGB vale su precio?"),
            ("ajustes", "Ajustes recomendados"),
        ],
        "faq": [
            ("¿El HyperX QuadCast es bueno para streaming?",
             "Sí, es una opción sólida si tu cuarto es razonablemente silencioso: trae "
             "araña antivibración integrada, silenciador táctil, control de ganancia y "
             "salida de auriculares para monitoreo sin latencia. Al ser condensador, en "
             "cuartos con eco o ruido rinde peor que un dinámico."),
            ("¿Las luces RGB afectan al sonido del micrófono?",
             "No, la iluminación no interviene en la captación. Lo que sí afecta es al "
             "presupuesto: parte del precio se va en carcasa e iluminación en lugar de "
             "en la cápsula y la electrónica."),
            ("¿Qué patrón polar debo usar en el QuadCast para transmitir?",
             "Cardioide. Los otros patrones (omnidireccional, bidireccional y estéreo) "
             "son para grabación de ambiente o entrevistas presenciales y, en un "
             "directo, solo meten más cuarto en tu audio."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>HyperX QuadCast</strong> es un micrófono de condensador USB diseñado para
streaming. Su versión <strong>QuadCast S</strong> añade iluminación RGB configurable.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador USB</td></tr>
<tr><td>Patrones</td><td>Cardioide, omni, bidireccional y estéreo</td></tr>
<tr><td>Antivibración</td><td>Araña elástica integrada</td></tr>
<tr><td>Silenciador</td><td>Táctil, en la parte superior</td></tr>
<tr><td>Monitoreo</td><td>Salida de auriculares con escucha directa</td></tr>
<tr><td>Rango orientativo</td><td>110-170 USD según versión</td></tr>
</tbody></table>

<h2 id="bueno">Lo que hace bien</h2>
<ul class="checks">
<li><strong>La araña integrada.</strong> Es la mejor idea del producto: elimina buena
parte de los golpes de mesa sin comprar nada aparte.</li>
<li><strong>El silenciador táctil.</strong> Silenciar tocando la parte superior, sin
ruido de clic, es enormemente práctico en directo.</li>
<li><strong>Monitoreo sin latencia.</strong> Te escuchas antes de que la señal entre al
PC, lo que corrige errores de técnica al momento.</li>
<li><strong>Ganancia física.</strong> Rueda en la base, sin abrir menús.</li>
<li><strong>Cero instalación.</strong> USB y a funcionar.</li>
</ul>

<h2 id="pegas">Las pegas reales</h2>
<ul class="checks">
<li><strong>Es un condensador.</strong> Capta el cuarto. Si tienes eco, ventilador o
teclado mecánico, un dinámico te dará mejor resultado final.</li>
<li><strong>Los cuatro patrones son una trampa.</strong> Mucha gente lo deja en
omnidireccional o estéreo sin saberlo y luego se queja del eco.</li>
<li><strong>Ocupa espacio en la mesa.</strong> Y para acercarlo a la boca vas a querer
un brazo, que se compra aparte.</li>
<li><strong>Precio inflado por diseño.</strong> A igual coste, un micro sin iluminación
suele llevar mejor componente de audio.</li>
</ul>

<h2 id="rgb">¿El RGB vale su precio?</h2>
<p>Sinceramente: solo si sale en cámara. Si el micrófono es parte de tu plano y de tu
identidad visual, el RGB es una decisión de <em>producción</em>, no de audio, y ahí sí
tiene sentido. Si el micro está fuera de plano, ese dinero rinde más en un brazo
articulado sólido y algo de absorción acústica.</p>
<div class="note">Regla simple: si nadie va a ver el micrófono, no pagues por sus luces.</div>

<h2 id="ajustes">Ajustes recomendados</h2>
<ol>
<li><strong>Patrón cardioide</strong>, siempre, para un streamer en solitario.</li>
<li><strong>Distancia de 10-15 cm</strong>, con el micro ligeramente fuera de eje.</li>
<li><strong>Ganancia</strong> ajustada para picos alrededor de -12 dB.</li>
<li><strong>Filtro paso alto a 80 Hz</strong> en OBS.</li>
<li><strong>Compresor suave</strong>, ratio 3:1 y unos 6 dB de reducción máxima.</li>
<li><strong>Brazo articulado</strong> en cuanto puedas: la araña integrada ayuda, pero
no hace milagros con una mesa que vibra.</li>
</ol>
<p>Si dudas entre esto y la ruta profesional, lee
<a href="../usb-o-xlr/">USB o XLR</a>. Y si el cuarto es el problema, mira los
<a href="../mejores-micros-streaming/">dinámicos</a>.</p>
""",
    }

    PAGES["microfono-array/"] = {
        "title": "Micrófono array: qué es, cómo funciona y cuándo lo necesitas",
        "desc": ("Micrófono array o matriz de micrófonos: beamforming, cancelación de "
                 "ruido, usos en videoconferencia y por qué no sirve para streaming."),
        "h1": "Micrófono array: varias cápsulas, un solo sonido",
        "crumb": "Micrófono array",
        "article": True,
        "lede": ("Es la tecnología que llevan tu portátil, tu móvil y las barras de "
                 "sala de reuniones. Resuelve un problema muy concreto, y no es el tuyo "
                 "si transmites."),
        "toc": [
            ("que-es", "Qué es un micrófono array"),
            ("beamforming", "Beamforming explicado"),
            ("usos", "Dónde se usa"),
            ("streaming", "Por qué no sirve para streaming"),
            ("elegir", "Cómo elegir uno"),
        ],
        "faq": [
            ("¿Qué es un micrófono array?",
             "Es un conjunto de dos o más cápsulas separadas por distancias conocidas "
             "cuyas señales se combinan por software. Al comparar el instante en que el "
             "sonido llega a cada cápsula, el sistema deduce de qué dirección viene y "
             "puede reforzar esa dirección y atenuar las demás."),
            ("¿Un micrófono array sirve para streaming o podcast?",
             "No es la herramienta adecuada. Está optimizado para inteligibilidad de voz "
             "a distancia en salas, no para calidad tonal; el procesamiento aplica "
             "supresión de ruido agresiva que adelgaza la voz. Para streaming rinde "
             "mucho más un micrófono cardioide cerca de la boca."),
            ("¿El micrófono de mi portátil es un array?",
             "En la mayoría de portátiles y móviles actuales, sí: llevan dos o más "
             "cápsulas y usan procesamiento para aislar tu voz del ambiente y cancelar "
             "el eco de los altavoces."),
        ],
        "body": """
<h2 id="que-es">Qué es un micrófono array</h2>
<p>Un <strong>micrófono array</strong> (o matriz de micrófonos) no es un micrófono: es
un <em>sistema</em>. Varias cápsulas colocadas a distancias conocidas entre sí, más un
procesador que combina sus señales.</p>
<p>La idea es sencilla. Si un sonido llega a la cápsula izquierda una fracción de
milisegundo antes que a la derecha, el sistema sabe que viene de la izquierda. Con esa
información puede hacer algo que un micrófono suelto no puede: <strong>decidir de qué
dirección quiere escuchar</strong>, sin mover nada físicamente.</p>

<h2 id="beamforming">Beamforming explicado</h2>
<p>A esa técnica se la llama <strong>beamforming</strong>: formación de haz. El sistema
crea un «cono» virtual de escucha y lo apunta hacia quien está hablando.</p>
<table>
<thead><tr><th>Función</th><th>Qué hace</th><th>Efecto secundario</th></tr></thead>
<tbody>
<tr><td>Beamforming</td><td>Apunta la escucha hacia la voz</td><td>Cambios de timbre al moverte</td></tr>
<tr><td>Supresión de ruido</td><td>Elimina ruido constante de fondo</td><td>Adelgaza la voz y come los finales</td></tr>
<tr><td>Cancelación de eco</td><td>Quita lo que suena por los altavoces</td><td>Puede cortar sílabas al hablar a la vez</td></tr>
<tr><td>Control de ganancia</td><td>Nivela el volumen automáticamente</td><td>Sube el ruido en los silencios</td></tr>
</tbody></table>

<h2 id="usos">Dónde se usa</h2>
<ul class="checks">
<li><strong>Salas de reuniones:</strong> barras y paneles de techo que siguen a quien
habla sin micrófonos individuales.</li>
<li><strong>Portátiles y móviles:</strong> para que te entiendan en una llamada sin
acercarte al equipo.</li>
<li><strong>Altavoces inteligentes:</strong> detectan la palabra de activación entre
ruido.</li>
<li><strong>Coches:</strong> manos libres con motor y viento de fondo.</li>
</ul>
<p>Fíjate en el patrón común: <strong>voz a distancia, en condiciones malas, donde lo
importante es entender y no que suene bonito</strong>.</p>

<h2 id="streaming">Por qué no sirve para streaming</h2>
<p>Un array está diseñado para <em>inteligibilidad</em>, no para <em>calidad tonal</em>.
El procesamiento que lo hace útil en una sala de juntas es exactamente lo que arruina una
voz en un directo:</p>
<ul class="checks">
<li>La supresión de ruido deja la voz fina y con artefactos metálicos.</li>
<li>El control automático de ganancia sube el ruido cuando callas.</li>
<li>El timbre cambia si te mueves, porque el haz se recalcula.</li>
<li>Los finales de palabra se comen al confundirse con ruido.</li>
</ul>
<div class="note">Para streaming, la solución no es más tecnología: es acercar un
micrófono cardioide a tu boca. <a href="../mejores-micros-streaming/">Ver opciones</a>.</div>

<h2 id="elegir">Cómo elegir uno (si de verdad lo necesitas)</h2>
<p>Tiene sentido si tu problema es una <strong>sala con varias personas</strong> y no
quieres un micrófono por cabeza:</p>
<ul class="checks">
<li><strong>Cobertura:</strong> comprueba los metros y el ángulo que cubre de verdad.</li>
<li><strong>Cancelación de eco acústico:</strong> imprescindible si hay altavoces.</li>
<li><strong>Montaje:</strong> techo, mesa o barra. Cambia mucho el resultado.</li>
<li><strong>Tratamiento de la sala:</strong> ni el mejor array salva una sala con eco.</li>
</ul>
<p>Y si lo que buscabas era otra cosa, revisa el
<a href="../por-modelo/">índice por modelo</a>.</p>
""",
    }

    PAGES["microfono-electronico/"] = {
        "title": "Micrófono electrónico: qué significa y qué estás comprando",
        "desc": ("Qué es un micrófono electrónico o electret, en qué se diferencia de "
                 "un condensador de estudio y cuándo es suficiente."),
        "h1": "Micrófono electrónico: el término que confunde a todo el mundo",
        "crumb": "Micrófono electrónico",
        "article": True,
        "lede": ("Casi siempre se refiere a un micrófono de electret con electrónica "
                 "integrada. Entender eso te evita pagar de más o comprar de menos."),
        "toc": [
            ("que-significa", "Qué significa el término"),
            ("electret", "Qué es un electret"),
            ("comparativa", "Frente a un condensador de estudio"),
            ("cuando", "Cuándo es suficiente"),
            ("comprar", "Qué mirar antes de comprar"),
        ],
        "faq": [
            ("¿Qué es un micrófono electrónico?",
             "No es una categoría técnica formal. En la práctica se usa para referirse a "
             "micrófonos de electret con electrónica integrada: los pequeños módulos que "
             "llevan los teléfonos, portátiles, micrófonos de solapa y kits de "
             "electrónica, y que necesitan una pequeña tensión de alimentación para "
             "funcionar."),
            ("¿Un micrófono electret es lo mismo que un condensador?",
             "Funciona con el mismo principio, pero el electret lleva una carga eléctrica "
             "permanente en el material del diafragma, así que no necesita los 48 V de "
             "phantom: le basta una tensión muy pequeña, a menudo de 1,5 a 5 V."),
            ("¿Sirve un micrófono electret para grabar voz con calidad?",
             "Sí, y de hecho la mayoría de micrófonos de solapa profesionales son "
             "electret. La calidad depende mucho más de la cápsula concreta y de la "
             "colocación que de la etiqueta que lleve."),
        ],
        "body": """
<h2 id="que-significa">Qué significa el término</h2>
<p>«Micrófono electrónico» no es una categoría técnica reconocida. Es un término
coloquial que la gente usa para tres cosas distintas, y conviene saber cuál te están
vendiendo:</p>
<table>
<thead><tr><th>Lo que suele significar</th><th>Ejemplo típico</th><th>Alimentación</th></tr></thead>
<tbody>
<tr><td>Cápsula electret con electrónica integrada</td><td>Módulo de kit Arduino, micro de portátil</td><td>1,5-5 V</td></tr>
<tr><td>Micrófono de solapa o de diadema</td><td>Lavalier para móvil o cámara</td><td>Plug-in power o pila</td></tr>
<tr><td>Micrófono USB genérico</td><td>Micro de escritorio económico</td><td>Por USB</td></tr>
</tbody></table>
<p>En los tres casos hay algo en común: <strong>la cápsula es de electret</strong>.</p>

<h2 id="electret">Qué es un electret</h2>
<p>Un condensador clásico necesita una tensión externa para polarizar el diafragma: de
ahí los 48 V de phantom. Un <strong>electret</strong> resuelve eso de otra forma: el
material del diafragma lleva una <strong>carga eléctrica permanente</strong> incorporada
de fábrica, igual que un imán lleva magnetismo permanente.</p>
<p>Como ya está polarizado, no hace falta phantom. Solo necesita una tensión pequeña
para el preamplificador diminuto que lleva dentro, y eso se la puede dar un puerto USB,
una pila o la propia entrada del teléfono.</p>

<h2 id="comparativa">Frente a un condensador de estudio</h2>
<table>
<thead><tr><th></th><th>Electret</th><th>Condensador de estudio</th></tr></thead>
<tbody>
<tr><td>Polarización</td><td>Permanente, de fábrica</td><td>Externa, phantom 48 V</td></tr>
<tr><td>Tamaño</td><td>Muy pequeño</td><td>Grande</td></tr>
<tr><td>Coste</td><td>Muy bajo</td><td>Medio a alto</td></tr>
<tr><td>Ruido propio</td><td>Mayor</td><td>Menor</td></tr>
<tr><td>Uso típico</td><td>Solapa, móviles, kits, portátiles</td><td>Estudio, locución, canto</td></tr>
<tr><td>Envejecimiento</td><td>La carga se degrada muy lentamente</td><td>Estable</td></tr>
</tbody></table>

<h2 id="cuando">Cuándo es suficiente</h2>
<ul class="checks">
<li><strong>Vídeo hablando a cámara:</strong> un electret de solapa bien colocado supera
a cualquier micro de escritorio mal colocado.</li>
<li><strong>Grabación en movimiento:</strong> es prácticamente la única opción cómoda.</li>
<li><strong>Proyectos de electrónica:</strong> es exactamente lo que necesitas.</li>
<li><strong>Videollamadas:</strong> de sobra.</li>
</ul>
<p>Y cuándo no: para voz en off, canto o streaming sentado, un micrófono de escritorio
dedicado va a sonar mejor por simple tamaño de cápsula y calidad de preamplificador.</p>

<h2 id="comprar">Qué mirar antes de comprar</h2>
<ul class="checks">
<li><strong>Cómo se alimenta.</strong> Plug-in power, pila o USB: si te equivocas, no
sonará.</li>
<li><strong>El conector.</strong> Para móvil necesitas TRRS, no TRS. Es el fallo número
uno. Lo explicamos en <a href="../microfono-para-telefono/">micrófono para teléfono</a>.</li>
<li><strong>El patrón.</strong> Muchos electret baratos son omnidireccionales, lo que en
un cuarto con eco es mala idea.</li>
<li><strong>El paravientos.</strong> Imprescindible en exteriores.</li>
</ul>
<p>Si lo que buscas es un micrófono de escritorio, pasa mejor por
<a href="../mejores-micros-streaming/">la comparativa por presupuesto</a>.</p>
""",
    }

    PAGES["shure-antena/"] = {
        "title": "Antena Shure: sistemas inalámbricos, antenas y por qué se cortan",
        "desc": ("Antenas para sistemas inalámbricos Shure: tipos, colocación, "
                 "distribuidores de antena y cómo evitar cortes y ruido en directo."),
        "h1": "Antenas para micrófonos inalámbricos Shure",
        "crumb": "Antena Shure",
        "article": True,
        "lede": ("En un sistema inalámbrico, el 90 % de los cortes no vienen del "
                 "micrófono ni del receptor: vienen de las antenas y de dónde están "
                 "colocadas."),
        "toc": [
            ("tipos", "Tipos de antena"),
            ("diversity", "Por qué hay dos antenas"),
            ("colocacion", "Colocación: las reglas que importan"),
            ("distribuidor", "Distribuidores de antena"),
            ("problemas", "Diagnóstico de cortes"),
        ],
        "faq": [
            ("¿Por qué los sistemas inalámbricos tienen dos antenas?",
             "Usan un esquema llamado diversity: el receptor vigila las dos antenas y "
             "escoge en cada instante la que recibe mejor señal. Como las zonas de señal "
             "débil por cancelación no coinciden en dos puntos distintos del espacio, "
             "tener dos antenas separadas evita la mayoría de los cortes."),
            ("¿Puedo alargar el cable de la antena todo lo que quiera?",
             "No. El cable coaxial atenúa la señal, y cuanto más largo y más fino, más "
             "pérdida. Para tiradas largas se usa cable de baja pérdida y, si hace falta, "
             "un amplificador de antena; alargar sin compensar empeora el alcance en vez "
             "de mejorarlo."),
            ("¿Se pueden juntar varios receptores en una sola pareja de antenas?",
             "Sí, con un distribuidor de antena: reparte la señal de una sola pareja "
             "entre varios receptores y, de paso, suele alimentarlos. Es la forma "
             "correcta de montar varios canales sin llenar el rack de antenas."),
        ],
        "body": """
<h2 id="tipos">Tipos de antena</h2>
<table>
<thead><tr><th>Tipo</th><th>Cómo capta</th><th>Úsala cuando…</th></tr></thead>
<tbody>
<tr><td>Látigo (1/2 onda)</td><td>Omnidireccional</td><td>Salas pequeñas, distancias cortas, montaje directo en el receptor</td></tr>
<tr><td>Direccional (paddle)</td><td>En un ángulo hacia delante</td><td>Escenarios grandes o ambientes con mucha interferencia</td></tr>
<tr><td>Helicoidal</td><td>Direccional, polarización circular</td><td>El usuario mueve mucho el micrófono de orientación</td></tr>
<tr><td>Activa (amplificada)</td><td>Cualquiera, con amplificador</td><td>Tiradas largas de cable coaxial</td></tr>
</tbody></table>
<div class="note">Una antena direccional no «alcanza más» por arte de magia: concentra
la sensibilidad en una zona y rechaza el resto, lo que reduce interferencias.</div>

<h2 id="diversity">Por qué hay dos antenas</h2>
<p>Las ondas de radio rebotan en paredes, techos y personas. En algunos puntos del
espacio esos rebotes se cancelan entre sí y la señal casi desaparece. Si tu única antena
está justo en uno de esos puntos, el audio se corta.</p>
<p>El sistema <strong>diversity</strong> resuelve esto con dos antenas separadas: la
probabilidad de que las dos caigan a la vez en un punto muerto es mínima, y el receptor
va escogiendo la mejor sobre la marcha.</p>

<h2 id="colocacion">Colocación: las reglas que importan</h2>
<ol>
<li><strong>Línea de visión directa</strong> con el micrófono siempre que se pueda. Las
personas son bolsas de agua y bloquean la señal.</li>
<li><strong>Separa las dos antenas</strong> entre sí al menos un cuarto de la longitud
de onda; en la práctica, un palmo largo como mínimo, y mejor más.</li>
<li><strong>Fórmalas en V</strong>, a unos 45 grados cada una.</li>
<li><strong>Sácalas del rack metálico.</strong> Un rack cerrado es una jaula de Faraday;
usa panel frontal o soportes remotos.</li>
<li><strong>Aléjalas de LED, pantallas, fuentes conmutadas y wifi.</strong></li>
<li><strong>Súbelas</strong> por encima de la altura del público.</li>
</ol>

<h2 id="distribuidor">Distribuidores de antena</h2>
<p>Si tienes más de dos receptores, no pongas antenas a cada uno: acabarás con un bosque
de látigos interfiriéndose. Un <strong>distribuidor de antena</strong> toma una sola
pareja de antenas y reparte esa señal entre varios receptores, normalmente alimentándolos
a la vez.</p>
<ul class="checks">
<li>Menos antenas, menos interferencia mutua.</li>
<li>Una sola posición que optimizar en lugar de ocho.</li>
<li>Cableado del rack mucho más limpio.</li>
<li>Permite llevar las antenas lejos, cerca del escenario.</li>
</ul>

<h2 id="problemas">Diagnóstico de cortes</h2>
<table>
<thead><tr><th>Síntoma</th><th>Causa habitual</th><th>Qué hacer</th></tr></thead>
<tbody>
<tr><td>Cortes al moverse a un punto concreto</td><td>Punto muerto por rebotes</td><td>Separar más las antenas o moverlas</td></tr>
<tr><td>Ruido constante de fondo</td><td>Interferencia en la frecuencia</td><td>Reescanear y reasignar frecuencias</td></tr>
<tr><td>Alcance mucho menor del esperado</td><td>Cable coaxial largo o fino</td><td>Cable de baja pérdida o antena activa</td></tr>
<tr><td>Falla solo con público</td><td>Cuerpos bloqueando la señal</td><td>Subir las antenas por encima del público</td></tr>
<tr><td>Todo falla al añadir canales</td><td>Intermodulación entre frecuencias</td><td>Usar el planificador de frecuencias del fabricante</td></tr>
</tbody></table>
<p>Nada de esto es exclusivo de una marca: aplica a cualquier sistema inalámbrico de
UHF. Si lo tuyo es un directo desde casa y no un escenario, probablemente no necesitas
inalámbrico: mira la <a href="../mejores-micros-streaming/">comparativa de micros con
cable</a>, que por el mismo dinero suenan mejor y no se cortan.</p>
""",
    }
