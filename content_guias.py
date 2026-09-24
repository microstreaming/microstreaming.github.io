# -*- coding: utf-8 -*-
"""Guias de apoyo para el nicho ampliado.

El publico no son solo streamers: tambien gente que graba YouTube de
formato largo, podcast y voz en off. Estas paginas cubren la parte
informacional (como elegir, como configurar) que alimenta con enlaces
internos a las fichas por modelo, que son las comerciales.
"""


def add_pages(PAGES, SITE):

    # ------------------------------------------------------------------
    PAGES["dinamico-vs-condensador/"] = {
        "title": "Micrófono dinámico vs condensador: cuál elegir de verdad",
        "desc": ("Diferencias reales entre micrófono dinámico y condensador: "
                 "sensibilidad, ruido de cuarto, phantom y cuál conviene según "
                 "dónde grabas."),
        "h1": "Dinámico vs condensador: la decisión que más te va a importar",
        "crumb": "Dinámico vs condensador",
        "article": True,
        "lede": ("No es una cuestión de calidad. Es una cuestión de cuánto ruido "
                 "tiene la habitación donde grabas. Con eso resuelto, el resto "
                 "se decide solo."),
        "toc": [
            ("como-funcionan", "Cómo funciona cada uno"),
            ("tabla", "Comparativa directa"),
            ("test", "El test de los tres aplausos"),
            ("mitos", "Cuatro mitos"),
            ("veredicto", "Veredicto por situación"),
        ],
        "faq": [
            ("¿Qué es mejor, un micrófono dinámico o uno de condensador?",
             "Ninguno es mejor en abstracto. El condensador capta más detalle y más "
             "ambiente; el dinámico capta menos de las dos cosas. En una habitación "
             "silenciosa y tratada gana el condensador; en un cuarto normal con eco, "
             "teclado o ruido de calle gana el dinámico, y por bastante."),
            ("¿Por qué los locutores de radio usan micrófonos dinámicos?",
             "Porque trabajan cerca del micrófono y necesitan que no se cuele el "
             "estudio, los papeles ni los compañeros. La baja sensibilidad del "
             "dinámico, que en un estudio de grabación sería una limitación, ahí es "
             "exactamente la ventaja que buscan."),
            ("¿Un dinámico necesita alimentación phantom?",
             "No. Un dinámico genera su propia señal por inducción y funciona sin "
             "alimentación externa. Dejar el phantom encendido no lo daña en una "
             "interfaz moderna con cable balanceado correcto, pero no le aporta nada."),
            ("¿Puedo usar un condensador si mi cuarto tiene eco?",
             "Puedes, pero el resultado será peor que con un dinámico del mismo "
             "precio. El condensador no distingue entre tu voz y el rebote de la "
             "pared: reproduce los dos con la misma fidelidad. Antes de comprarlo, "
             "trata el cuarto."),
        ],
        "body": """
<h2 id="como-funcionan">Cómo funciona cada uno</h2>
<p>La diferencia está en qué se mueve dentro de la cápsula, y eso lo explica todo lo
demás.</p>
<p>En un <strong>dinámico</strong>, el sonido mueve un diafragma unido a una bobina de
cobre que se desplaza dentro de un imán. Esa bobina pesa. Hace falta bastante energía
para moverla, así que solo reacciona a lo que le llega fuerte: tu voz a 5 cm, sí; el
ventilador del otro lado del cuarto, no.</p>
<p>En un <strong>condensador</strong>, lo que se mueve es una lámina finísima
metalizada frente a una placa fija. No pesa casi nada, así que reacciona a
prácticamente cualquier variación de presión. Por eso capta el aire de tu voz. Y por eso
capta también el perro del vecino.</p>

<div class="note">
<strong>La misma frase describe la ventaja y el problema:</strong> el condensador oye
todo lo que hay en la habitación.
</div>

<h2 id="tabla">Comparativa directa</h2>
<table>
<thead><tr><th></th><th>Dinámico</th><th>Condensador</th></tr></thead>
<tbody>
<tr><td>Sensibilidad</td><td>Baja</td><td>Alta</td></tr>
<tr><td>Ruido de cuarto que deja entrar</td><td>Poco</td><td>Mucho</td></tr>
<tr><td>Detalle en agudos</td><td>Contenido</td><td>Extendido</td></tr>
<tr><td>Alimentación phantom</td><td>No necesita</td><td>Obligatoria (XLR)</td></tr>
<tr><td>Ganancia que pide</td><td>Bastante</td><td>Poca</td></tr>
<tr><td>Aguanta golpes y gritos</td><td>Muy bien</td><td>Regular</td></tr>
<tr><td>Distancia de trabajo</td><td>2-10 cm</td><td>10-25 cm</td></tr>
<tr><td>Uso típico</td><td>Directo, radio, podcast en casa</td><td>Estudio, voz en off, canto</td></tr>
</tbody></table>

<h2 id="test">El test de los tres aplausos</h2>
<p>No hace falta medir nada. Ponte en el centro de la habitación donde vas a grabar,
con las ventanas cerradas, y da tres palmadas secas y fuertes.</p>
<ul class="checks">
<li><strong>Si oyes una cola, un «chas» que rebota:</strong> tu cuarto es reverberante.
Dinámico.</li>
<li><strong>Si el sonido muere seco, casi sin cola:</strong> el cuarto absorbe.
Puedes plantearte un condensador.</li>
<li><strong>Si además oyes tráfico, nevera o aire acondicionado al callarte:</strong>
dinámico, sin dudarlo.</li>
</ul>
<p>Es tosco, pero acierta más que cualquier especificación de la caja.</p>

<h2 id="mitos">Cuatro mitos</h2>

<h3>«El condensador suena más profesional»</h3>
<p>Suena más <em>detallado</em>, que no es lo mismo. En un cuarto sin tratar, ese
detalle incluye la pared de enfrente, y el resultado suena a habitación, no a estudio.</p>

<h3>«El dinámico es para principiantes»</h3>
<p>Los micrófonos de difusión más usados en radio y en los grandes canales son
dinámicos. Es una elección técnica, no un escalón de entrada.</p>

<h3>«Con un condensador no necesito acercarme»</h3>
<p>Al revés: como capta más ambiente, la relación entre tu voz y el cuarto empeora
rápido con la distancia. Acercarte sigue siendo la mejor decisión con cualquier micro.</p>

<h3>«El phantom daña los dinámicos»</h3>
<p>En una interfaz moderna y con cable XLR balanceado en buen estado, no. El riesgo
real aparece con cables defectuosos o con micrófonos de cinta antiguos, que son otra
familia.</p>

<h2 id="veredicto">Veredicto por situación</h2>
<table>
<thead><tr><th>Tu situación</th><th>Elige</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Dormitorio, teclado mecánico, directo</td><td>Dinámico</td><td>Rechaza lo que no quieres</td></tr>
<tr><td>Piso con ruido de calle</td><td>Dinámico</td><td>El condensador amplificaría el tráfico</td></tr>
<tr><td>Cuarto tratado, voz en off</td><td>Condensador</td><td>Aprovechas el detalle</td></tr>
<tr><td>Grabas guitarra o canto</td><td>Condensador</td><td>Necesitas los agudos</td></tr>
<tr><td>Podcast con invitado presencial</td><td>Dos dinámicos</td><td>Cada micro capta solo a su persona</td></tr>
<tr><td>No estás seguro</td><td>Dinámico</td><td>Perdona muchos más errores</td></tr>
</tbody></table>
<p>Si ya lo tienes claro, pasa a la
<a href="../mejores-micros-streaming/">comparativa por presupuesto</a>. Si te inclinas
por el condensador, lee antes <a href="../microfono-condensador/">cómo elegirlo</a>.</p>
""",
    }

    # ------------------------------------------------------------------
    PAGES["mejores-microfonos-podcast/"] = {
        "title": "Mejores micrófonos para podcast: guía por número de voces",
        "desc": ("Qué micrófono para podcast elegir según grabes solo, con invitado "
                 "presencial o en remoto. Montajes completos y errores que arruinan "
                 "el episodio."),
        "h1": "Mejores micrófonos para podcast: empieza por cuántas voces",
        "crumb": "Micrófonos para podcast",
        "article": True,
        "lede": ("El número de personas que hablan en la misma habitación decide tu "
                 "montaje entero. Mucho más que la marca del micrófono."),
        "toc": [
            ("voces", "Cuántas voces cambia todo"),
            ("solo", "Podcast en solitario"),
            ("invitado", "Con invitado presencial"),
            ("remoto", "Invitados en remoto"),
            ("errores", "Errores que arruinan un episodio"),
        ],
        "faq": [
            ("¿Qué micrófono usan los podcasts profesionales?",
             "Casi siempre dinámicos de difusión con conexión XLR, uno por persona, "
             "sobre brazo articulado y conectados a una interfaz o mezclador con "
             "varias entradas. Se eligen porque rechazan el ambiente y porque aguantan "
             "años de uso diario."),
            ("¿Puedo grabar un podcast con dos personas y un solo micrófono?",
             "Se puede, pero es la decisión que más lamenta la gente. Con un micrófono "
             "compartido no puedes corregir después el volumen de cada voz por separado, "
             "ni quitar la tos de uno sin tocar la frase del otro. Dos micrófonos y dos "
             "pistas cuestan poco más y te salvan la edición."),
            ("¿Es mejor grabar el podcast en pistas separadas?",
             "Sí, siempre que puedas. Una pista por voz te permite nivelar, comprimir y "
             "limpiar cada una por separado. Es la diferencia entre un episodio editable "
             "y uno que tienes que dar por bueno como salió."),
            ("¿Sirve un micrófono USB para podcast?",
             "Para un podcast de una sola voz, perfectamente. El problema aparece al "
             "juntar dos micros USB en el mismo ordenador: cada uno lleva su propio reloj "
             "y en grabaciones largas se desincronizan. Para dos o más voces, interfaz "
             "XLR."),
        ],
        "body": """
<h2 id="voces">Cuántas voces cambia todo</h2>
<p>Antes de mirar modelos, responde a una sola pregunta: <strong>¿cuánta gente va a
hablar dentro de la misma habitación?</strong> De ahí sale el resto.</p>
<table>
<thead><tr><th>Formato</th><th>Micrófonos</th><th>Qué necesitas además</th></tr></thead>
<tbody>
<tr><td>Solo, en casa</td><td>1 dinámico</td><td>Brazo y antipop</td></tr>
<tr><td>Dos en la misma sala</td><td>2 dinámicos</td><td>Interfaz de 2 entradas</td></tr>
<tr><td>Tres o cuatro en sala</td><td>1 por persona</td><td>Interfaz o mezclador de 4</td></tr>
<tr><td>Tú en casa, invitado remoto</td><td>1 dinámico</td><td>Plataforma que grabe local</td></tr>
</tbody></table>
<div class="note">
<strong>Un micrófono por boca.</strong> Es la regla que más diferencia marca entre un
podcast que se puede editar y uno que no.
</div>

<h2 id="solo">Podcast en solitario</h2>
<p>Es el caso más fácil y donde menos hay que gastar. Un <strong>dinámico cardioide</strong>
a 5-10 cm de la boca, sobre brazo, con antipop. Si tu cuarto no está tratado, esto supera
a cualquier condensador caro.</p>
<ul class="checks">
<li><strong>Ruta sencilla:</strong> dinámico con salida USB. Enchufas y grabas.</li>
<li><strong>Ruta que escala:</strong> dinámico XLR más interfaz de dos entradas. La
segunda entrada te espera para cuando llegue el primer invitado.</li>
<li><strong>Atajo que no recomiendo:</strong> grabar con el micro del portátil «de
momento». Ese «de momento» dura veinte episodios que luego no querrás tener publicados.</li>
</ul>

<h2 id="invitado">Con invitado presencial</h2>
<p>Aquí aparece el problema que no existía antes: el micrófono de cada uno capta también
al otro. A eso se le llama <em>sangrado</em>, y es lo que hace que un podcast casero
suene a cueva.</p>
<ol>
<li><strong>Dos dinámicos cardioides</strong>, nunca condensadores.</li>
<li><strong>Colocados en ángulo</strong>, no enfrentados: el lado sordo de cada micro
debe apuntar hacia la otra persona.</li>
<li><strong>Grabación en dos pistas separadas.</strong> Innegociable.</li>
<li><strong>Auriculares cerrados para los dos.</strong> Con altavoces abiertos, cada
micro graba también lo que suena por ellos.</li>
<li><strong>Algo blando en la mesa</strong> entre los dos: un mantel, una toalla. Evita
el rebote directo.</li>
</ol>

<h2 id="remoto">Invitados en remoto</h2>
<p>El error clásico es grabar lo que sale de la videollamada. Esa señal ya viene
comprimida, con supresión de ruido y con cortes: no hay edición que la arregle.</p>
<ul class="checks">
<li><strong>Grabación local en ambos extremos.</strong> Cada uno graba su propia voz en
su equipo, y luego se juntan las pistas.</li>
<li><strong>Manda un micrófono al invitado si el episodio importa.</strong> Un dinámico
USB barato en su casa mejora más el resultado que cualquier cosa que hagas en el tuyo.</li>
<li><strong>Pide auriculares siempre.</strong> Sin ellos, tu voz vuelve a entrar por su
micrófono con retardo.</li>
<li><strong>Una claqueta al empezar:</strong> que los dos den una palmada. Te sirve para
alinear las pistas después.</li>
</ul>

<h2 id="errores">Errores que arruinan un episodio</h2>
<ul class="checks">
<li><strong>No hacer una prueba de 30 segundos</strong> antes de empezar. Grábala,
escúchala, y solo entonces arranca.</li>
<li><strong>Ganancia al máximo.</strong> Picos en torno a -12 dB, no rozando el 0.</li>
<li><strong>El micrófono en la mesa.</strong> Cada golpe de codo queda grabado.</li>
<li><strong>Puerta de ruido agresiva.</strong> Te corta el final de las palabras y suena
a llamada de teléfono.</li>
<li><strong>Grabar en mono todo junto</strong> cuando había dos voces.</li>
</ul>
<p>¿Aún no tienes micro? Empieza por la
<a href="../mejores-micros-streaming/">comparativa por presupuesto</a> o por
<a href="../dinamico-vs-condensador/">dinámico vs condensador</a>. Para colocarlo bien,
<a href="../brazo-y-arana-antivibracion/">brazo y araña</a>.</p>
""",
    }

    # ------------------------------------------------------------------
    PAGES["microfono-para-youtube/"] = {
        "title": "Micrófono para grabar vídeos de YouTube: cuál según tu formato",
        "desc": ("Qué micrófono para YouTube elegir según grabes hablando a cámara, "
                 "en escritorio, en exteriores o en formato largo. Sincronía, "
                 "solapa y cañón."),
        "h1": "Micrófono para YouTube: elige por formato, no por precio",
        "crumb": "Micrófono para YouTube",
        "article": True,
        "lede": ("La gente abandona un vídeo por el audio mucho antes que por la "
                 "imagen. Y el audio bueno en vídeo depende de dónde puedes poner "
                 "el micrófono sin que salga en plano."),
        "toc": [
            ("regla", "La regla del encuadre"),
            ("formatos", "Qué micro según el formato"),
            ("largo", "Formato largo: lo que cambia"),
            ("sincronia", "Sincronía y doble sistema"),
            ("ajustes", "Ajustes que salvan un vídeo"),
        ],
        "faq": [
            ("¿Qué micrófono es mejor para grabar vídeos de YouTube?",
             "Depende de si el micrófono puede salir en plano. Si puede, un dinámico "
             "sobre brazo da el mejor resultado. Si no puede, un micrófono de solapa "
             "bien colocado bajo la ropa gana a cualquier cañón situado lejos, porque "
             "lo que manda es la distancia a la boca."),
            ("¿Es mejor un micrófono de solapa o uno de cañón para YouTube?",
             "El de solapa está a 20 cm de la boca y el de cañón suele estar a un metro "
             "o más, así que el solapa deja entrar mucho menos ambiente. El cañón gana "
             "cuando no puedes poner nada encima del sujeto o grabas a varias personas "
             "en movimiento."),
            ("¿Puedo grabar el audio con el móvil y el vídeo con la cámara?",
             "Sí, es el llamado doble sistema y es lo que hace casi todo el mundo que "
             "cuida el audio. Graba también una pista de referencia con la cámara y da "
             "una palmada al empezar: el editor alinea las dos por esa forma de onda."),
        ],
        "body": """
<h2 id="regla">La regla del encuadre</h2>
<p>En streaming el micrófono puede salir en pantalla y no pasa nada; de hecho forma
parte de la estética. En vídeo, muchas veces no puede. Y esa restricción decide la
compra entera.</p>
<div class="note">
<strong>Lo que manda es la distancia a la boca.</strong> Un micrófono modesto a 20 cm
suena mejor que uno excelente a un metro y medio. Siempre.
</div>

<h2 id="formatos">Qué micro según el formato</h2>
<table>
<thead><tr><th>Formato</th><th>¿Sale el micro en plano?</th><th>Opción</th></tr></thead>
<tbody>
<tr><td>Hablando a cámara sentado</td><td>Puede salir</td><td>Dinámico sobre brazo</td></tr>
<tr><td>Hablando a cámara, plano limpio</td><td>No</td><td>Solapa bajo la ropa</td></tr>
<tr><td>Tutorial de escritorio</td><td>Puede salir</td><td>Dinámico o condensador USB</td></tr>
<tr><td>En movimiento por casa o calle</td><td>No</td><td>Solapa inalámbrico</td></tr>
<tr><td>Entrevista a dos</td><td>No</td><td>Dos solapas o dos transmisores</td></tr>
<tr><td>Exterior con viento</td><td>Da igual</td><td>Lo que sea, con paravientos peludo</td></tr>
</tbody></table>

<h2 id="largo">Formato largo: lo que cambia</h2>
<p>Un vídeo de veinte o cuarenta minutos castiga cosas que en un clip de dos minutos ni
se notan:</p>
<ul class="checks">
<li><strong>La fatiga de escucha.</strong> Un micrófono con agudos agresivos se soporta
tres minutos, no cuarenta. Aquí los dinámicos, más cálidos, juegan a favor.</li>
<li><strong>El ruido de fondo constante.</strong> Un siseo leve que no molesta al
principio se vuelve agotador al cuarto de hora.</li>
<li><strong>La deriva de la batería.</strong> Los inalámbricos que aguantan «5 horas»
rara vez lo hacen grabando. Lleva repuesto.</li>
<li><strong>La sincronía.</strong> Cuanto más largo el archivo, más se nota cualquier
desfase entre audio y vídeo.</li>
<li><strong>Tu propia técnica.</strong> A los treinta minutos te mueves, te reclinas y
te alejas del micro sin darte cuenta. El solapa no tiene ese problema; el de escritorio
sí.</li>
</ul>

<h2 id="sincronia">Sincronía y doble sistema</h2>
<p>Si grabas el audio en un aparato distinto de la cámara, estás haciendo
<strong>doble sistema</strong>. Funciona muy bien con dos precauciones:</p>
<ol>
<li><strong>Graba siempre una pista de referencia</strong> con el micrófono de la cámara,
aunque suene mal. Es la que usarás para alinear.</li>
<li><strong>Da una palmada al principio de cada toma.</strong> Es una claqueta gratis:
el pico aparece igual en las dos formas de onda.</li>
<li><strong>Comprueba la deriva</strong> en tomas de más de veinte minutos. Si al final
del archivo los labios van desfasados, tu editor tiene una función de estirar el audio
para corregirlo.</li>
<li><strong>Nombra los archivos al terminar cada bloque.</strong> Encontrar la pista
buena tres días después es media hora perdida.</li>
</ol>

<h2 id="ajustes">Ajustes que salvan un vídeo</h2>
<ul class="checks">
<li><strong>Desactiva el control automático de ganancia</strong> de la cámara si te deja.
Sube el ruido en los silencios.</li>
<li><strong>Paravientos peludo en exteriores.</strong> La espuma sola no basta con nada
de brisa.</li>
<li><strong>Pasa el cable del solapa por dentro de la ropa</strong> y fíjalo: el roce de
la tela es el fallo número uno.</li>
<li><strong>Apaga la nevera, el aire y las notificaciones</strong> antes de empezar.</li>
<li><strong>Filtro paso alto a 80 Hz</strong> en el montaje: quita retumbe sin tocar la voz.</li>
</ul>
<p>Si grabas desde el teléfono, tienes los detalles de conectores en
<a href="../microfono-para-telefono/">micrófono para teléfono</a>. Y para limpiar lo que
ya está grabado, <a href="../quitar-ruido-de-fondo/">cómo quitar el ruido de fondo</a>.</p>
""",
    }

    # ------------------------------------------------------------------
    PAGES["configurar-microfono-obs/"] = {
        "title": "Cómo configurar el micrófono en OBS paso a paso",
        "desc": ("Configurar el micrófono en OBS: ganancia, filtro paso alto, "
                 "compresor, puerta de ruido y orden correcto de los filtros, "
                 "explicado sin jerga."),
        "h1": "Configurar el micrófono en OBS: el orden importa más que los valores",
        "crumb": "Configurar el micrófono en OBS",
        "article": True,
        "lede": ("Cinco filtros bien puestos en el orden correcto suenan mejor que "
                 "quince mal encadenados. Esta es la cadena que funciona y el "
                 "motivo de cada eslabón."),
        "toc": [
            ("antes", "Antes de tocar OBS"),
            ("anadir", "Añadir el micrófono"),
            ("cadena", "La cadena de filtros, en orden"),
            ("valores", "Valores de partida"),
            ("problemas", "Problemas frecuentes"),
        ],
        "faq": [
            ("¿En qué orden hay que poner los filtros del micrófono en OBS?",
             "Filtro paso alto, después puerta de ruido, después compresor y por último "
             "ganancia o limitador. El orden importa porque cada filtro trabaja sobre lo "
             "que le entrega el anterior: si comprimes antes de limpiar, amplificas el "
             "ruido que luego querrás quitar."),
            ("¿Por qué se oye ruido de fondo en OBS aunque el micrófono sea bueno?",
             "Lo habitual es tener demasiada ganancia para compensar que hablas lejos "
             "del micrófono. Al subir la ganancia subes tu voz y el ruido por igual. La "
             "solución es acercarte y bajar la ganancia, no añadir más filtros."),
            ("¿Qué valores debe tener el compresor en OBS?",
             "Un punto de partida razonable es ratio 3:1, umbral en torno a -18 dB, "
             "ataque de 6 ms y liberación de 60 ms, ajustando hasta ver unos 6 dB de "
             "reducción en los picos. Si el medidor marca reducción constante, el umbral "
             "está demasiado bajo."),
            ("¿Debo usar la supresión de ruido de OBS?",
             "Con moderación. El método RNNoise limpia bastante pero deja la voz algo "
             "metálica y se come las respiraciones. Si tu cuarto está razonablemente "
             "silencioso, una puerta de ruido suave da un resultado más natural."),
        ],
        "body": """
<h2 id="antes">Antes de tocar OBS</h2>
<p>Ningún filtro arregla una señal mal capturada. Estos tres minutos ahorran una hora de
ajustes:</p>
<ul class="checks">
<li><strong>Acércate a 5-10 cm</strong> del micrófono si es dinámico, 10-20 cm si es
condensador.</li>
<li><strong>Apúntalo ligeramente fuera de eje</strong>, hacia la comisura de la boca.</li>
<li><strong>Sube la ganancia en la interfaz o en el propio micro</strong>, no en OBS,
hasta que tus picos normales lleguen a unos -12 dB.</li>
<li><strong>Apaga lo que zumbe</strong>: ventilador, aire, torre del PC si la tienes al
lado.</li>
</ul>
<div class="note">
<strong>Si el ruido de fondo ya se oye en crudo, no sigas.</strong> Arréglalo antes: es
mucho más barato mover el ventilador que perseguirlo con filtros.
</div>

<h2 id="anadir">Añadir el micrófono</h2>
<ol>
<li>En <strong>Fuentes</strong>, pulsa <code>+</code> y elige <em>Captura de entrada de
audio</em>.</li>
<li>Selecciona tu micrófono por su nombre, no «Dispositivo predeterminado»: si algún día
conectas unos auriculares, el predeterminado cambia sin avisar.</li>
<li>Desactiva el micrófono de <strong>Mezclador de audio → Mic/Aux</strong> si te quedan
dos entradas duplicadas.</li>
<li>Haz clic derecho sobre la fuente → <strong>Filtros</strong>. Aquí se construye todo.</li>
</ol>

<h2 id="cadena">La cadena de filtros, en orden</h2>
<p>El orden no es decorativo: cada filtro procesa lo que le pasa el anterior.</p>
<table>
<thead><tr><th>#</th><th>Filtro</th><th>Qué hace</th><th>Por qué va ahí</th></tr></thead>
<tbody>
<tr><td>1</td><td>Filtro paso alto</td><td>Corta graves por debajo de 80 Hz</td><td>Quita retumbe antes de que nada lo amplifique</td></tr>
<tr><td>2</td><td>Puerta de ruido</td><td>Silencia cuando no hablas</td><td>Actúa sobre señal ya limpia de graves</td></tr>
<tr><td>3</td><td>Compresor</td><td>Iguala volumen alto y bajo</td><td>Si fuera antes, subiría el ruido que la puerta iba a cortar</td></tr>
<tr><td>4</td><td>Ganancia</td><td>Ajusta el nivel final</td><td>Al final, cuando ya sabes con qué señal trabajas</td></tr>
<tr><td>5</td><td>Limitador</td><td>Impide saturar</td><td>Red de seguridad, siempre el último</td></tr>
</tbody></table>

<h2 id="valores">Valores de partida</h2>
<p>No son dogma: son un sitio del que salir. Ajusta escuchándote, no mirando números.</p>
<table>
<thead><tr><th>Filtro</th><th>Parámetro</th><th>Valor inicial</th></tr></thead>
<tbody>
<tr><td>Paso alto</td><td>Frecuencia</td><td>80 Hz</td></tr>
<tr><td>Puerta de ruido</td><td>Umbral de cierre</td><td>-45 dB</td></tr>
<tr><td>Puerta de ruido</td><td>Umbral de apertura</td><td>-35 dB</td></tr>
<tr><td>Compresor</td><td>Ratio</td><td>3:1</td></tr>
<tr><td>Compresor</td><td>Umbral</td><td>-18 dB</td></tr>
<tr><td>Compresor</td><td>Ataque / liberación</td><td>6 ms / 60 ms</td></tr>
<tr><td>Limitador</td><td>Umbral</td><td>-3 dB</td></tr>
</tbody></table>
<p>Deja siempre <strong>10 dB de diferencia</strong> entre los dos umbrales de la puerta.
Si los pegas, la puerta parpadea y te corta las sílabas.</p>

<h2 id="problemas">Problemas frecuentes</h2>
<table>
<thead><tr><th>Síntoma</th><th>Causa probable</th><th>Solución</th></tr></thead>
<tbody>
<tr><td>Se cortan los finales de palabra</td><td>Puerta demasiado agresiva</td><td>Baja el umbral de cierre y sube la liberación</td></tr>
<tr><td>Ruido que sube al callar</td><td>Compresor con umbral muy bajo</td><td>Sube el umbral; comprime menos</td></tr>
<tr><td>Voz metálica</td><td>Supresión de ruido excesiva</td><td>Quita RNNoise y usa puerta</td></tr>
<tr><td>Se oye eco de mis altavoces</td><td>Grabas sin auriculares</td><td>Usa auriculares cerrados</td></tr>
<tr><td>El micro no aparece</td><td>Lo usa otra aplicación en exclusiva</td><td>Cierra esa aplicación y reinicia OBS</td></tr>
<tr><td>Volumen muy bajo aun a tope</td><td>Dinámico con interfaz de poca ganancia</td><td>Acércate; valora un preamplificador</td></tr>
</tbody></table>
<p>Si el problema es el cuarto y no los ajustes, lee
<a href="../quitar-ruido-de-fondo/">cómo quitar el ruido de fondo</a>. Y si el micro
recoge los golpes de la mesa, el arreglo es mecánico:
<a href="../brazo-y-arana-antivibracion/">brazo y araña antivibración</a>.</p>
""",
    }

    # ------------------------------------------------------------------
    PAGES["quitar-ruido-de-fondo/"] = {
        "title": "Cómo quitar el ruido de fondo del micrófono, de verdad",
        "desc": ("Cómo quitar el ruido de fondo del micrófono: qué se arregla en la "
                 "habitación, qué con la colocación y qué con software. En ese orden."),
        "h1": "Quitar el ruido de fondo: en este orden, no en otro",
        "crumb": "Quitar el ruido de fondo",
        "article": True,
        "lede": ("El software es el último recurso, no el primero. Todo lo que "
                 "elimines antes de grabar no deja rastro; todo lo que quites "
                 "después se lleva por delante un trozo de tu voz."),
        "toc": [
            ("identificar", "Primero, identifica el ruido"),
            ("fuente", "Nivel 1: apagar la fuente"),
            ("colocacion", "Nivel 2: colocación"),
            ("cuarto", "Nivel 3: el cuarto"),
            ("software", "Nivel 4: software"),
        ],
        "faq": [
            ("¿Cómo quito el ruido de fondo del micrófono?",
             "Por orden de eficacia: apaga o aleja la fuente del ruido, acércate al "
             "micrófono, añade absorción a la habitación y solo al final aplica filtros. "
             "Cada paso hacia abajo en esa lista da menos resultado y cuesta más calidad "
             "de voz."),
            ("¿Por qué mi micrófono capta tanto ruido de fondo?",
             "Casi siempre por una de dos razones: estás demasiado lejos del micrófono y "
             "compensas subiendo la ganancia, o usas un condensador en una habitación "
             "que pide un dinámico. La distancia es la causa más frecuente y la más "
             "fácil de corregir."),
            ("¿La supresión de ruido estropea la voz?",
             "Sí, en cierta medida siempre. Los algoritmos distinguen voz de ruido de "
             "forma aproximada, así que al quitar el ruido se llevan armónicos y "
             "respiraciones. Cuanto más agresiva la supresión, más metálica suena la "
             "voz resultante."),
            ("¿Sirve poner el micrófono dentro de una caja con espuma?",
             "Los reflectores y cajas de aislamiento reducen algo de reverberación por "
             "detrás del micrófono, pero no bloquean el ruido aéreo: el tráfico y el aire "
             "acondicionado siguen entrando. Ayudan al eco, no al ruido."),
        ],
        "body": """
<h2 id="identificar">Primero, identifica el ruido</h2>
<p>«Ruido de fondo» son tres problemas distintos con soluciones distintas. Graba treinta
segundos de silencio, súbelo de volumen y escucha:</p>
<table>
<thead><tr><th>Lo que oyes</th><th>Qué es</th><th>Dónde se arregla</th></tr></thead>
<tbody>
<tr><td>Zumbido grave constante</td><td>Nevera, aire, torre del PC</td><td>Apagando o alejando</td></tr>
<tr><td>Siseo agudo constante</td><td>Ruido de la electrónica</td><td>Bajando ganancia, acercándote</td></tr>
<tr><td>Cola al hablar, sonido a cueva</td><td>Reverberación del cuarto</td><td>Absorción</td></tr>
<tr><td>Zumbido de 50 Hz</td><td>Problema eléctrico o de masa</td><td>Cambiando de enchufe o cable</td></tr>
<tr><td>Golpes sordos</td><td>Vibración por la mesa</td><td>Araña y brazo</td></tr>
</tbody></table>
<div class="note">
<strong>No apliques filtros hasta saber cuál de los cinco tienes.</strong> Cada uno se
cura en un sitio diferente, y solo uno se cura con software.
</div>

<h2 id="fuente">Nivel 1: apagar la fuente</h2>
<p>Gratis, instantáneo y más eficaz que cualquier plugin.</p>
<ul class="checks">
<li>Apaga el aire acondicionado durante la grabación. Diez minutos no calientan la sala.</li>
<li>Gira la torre del PC para que los ventiladores no apunten al micrófono.</li>
<li>Cierra ventanas y, si puedes, graba a horas de menos tráfico.</li>
<li>Silencia el móvil. En modo vibración, sobre una mesa, es peor que con sonido.</li>
<li>Desenchufa transformadores baratos que zumben cerca del micro.</li>
</ul>

<h2 id="colocacion">Nivel 2: colocación</h2>
<p>Aquí está la palanca grande. Lo que importa no es cuánto ruido hay, sino cuánta voz
hay <em>comparada</em> con ese ruido. Acercarte sube tu voz sin subir el ruido.</p>
<ul class="checks">
<li><strong>De 40 cm a 10 cm</strong> mejora esa relación de forma drástica. Es la
medida más rentable que existe.</li>
<li><strong>Baja la ganancia</strong> en cuanto te acerques. Si no, solo has subido todo.</li>
<li><strong>Pon el lado sordo del micro hacia el ruido.</strong> Un cardioide rechaza por
detrás: gíralo para que su espalda mire al ventilador.</li>
<li><strong>Aléjalo de superficies duras</strong> y de la pantalla, que refleja tu voz de
vuelta.</li>
</ul>

<h2 id="cuarto">Nivel 3: el cuarto</h2>
<p>Esto ataca la cola y el sonido a cueva, no el zumbido. Y no hace falta comprar paneles
para notarlo:</p>
<ul class="checks">
<li>Una <strong>cortina gruesa</strong> en la pared que tienes enfrente.</li>
<li>Una <strong>estantería llena de libros</strong> desordenados: difunde muy bien.</li>
<li><strong>Alfombra</strong> si el suelo es duro.</li>
<li>Grabar en un <strong>armario con ropa</strong> si buscas el mejor resultado por cero
euros. Suena a broma y es lo que hacen muchos locutores.</li>
<li>Evita el centro geométrico de la habitación y las esquinas.</li>
</ul>

<h2 id="software">Nivel 4: software</h2>
<p>Lo último, sobre lo que ya no se puede arreglar de otra forma. Dos herramientas y una
regla.</p>
<h3>Puerta de ruido</h3>
<p>Silencia cuando no hablas. No limpia el ruido <em>mientras</em> hablas, solo lo
esconde en las pausas. Es sutil y natural si dejas 10 dB entre umbral de apertura y de
cierre.</p>
<h3>Supresión de ruido</h3>
<p>Analiza y resta el ruido constante también mientras hablas. Es más potente y más
destructiva: a partir de cierto punto tu voz suena a walkie-talkie.</p>
<div class="note">
<strong>La regla:</strong> aplica la mínima cantidad que resuelva el problema, y
escúchate con auriculares antes de darlo por bueno. Lo que en altavoces parece limpio,
en auriculares suena procesado.
</div>
<p>Los valores concretos y el orden de los filtros están en
<a href="../configurar-microfono-obs/">configurar el micrófono en OBS</a>. Si el ruido
son golpes de mesa, el arreglo no es software:
<a href="../brazo-y-arana-antivibracion/">brazo y araña</a>. Y si el cuarto es
irrecuperable, quizá el micrófono sea el equivocado:
<a href="../dinamico-vs-condensador/">dinámico vs condensador</a>.</p>
""",
    }

    # ------------------------------------------------------------------
    PAGES["brazo-y-arana-antivibracion/"] = {
        "title": "Brazo de micrófono y araña antivibración: qué comprar y por qué",
        "desc": ("Guía de brazo articulado y araña antivibración: capacidad de peso, "
                 "tipos de anclaje, roscas, y por qué el soporte importa tanto como "
                 "el micrófono."),
        "h1": "Brazo y araña: el accesorio que más mejora tu sonido",
        "crumb": "Brazo y araña",
        "article": True,
        "lede": ("Nadie presume de su brazo de micrófono, y sin embargo es lo que te "
                 "permite hablar cerca sin grabar cada tecla que pulsas."),
        "toc": [
            ("por-que", "Por qué importa tanto"),
            ("brazo", "Elegir brazo"),
            ("arana", "Elegir araña"),
            ("roscas", "Roscas y adaptadores"),
            ("montaje", "Montaje que no se vence"),
        ],
        "faq": [
            ("¿Para qué sirve una araña antivibración?",
             "Suspende el micrófono con gomas o elásticos para que las vibraciones que "
             "viajan por la mesa y por el soporte no lleguen a la cápsula. Sin ella, "
             "cada golpe de teclado o de codo se graba como un golpe sordo."),
            ("¿Qué capacidad de peso necesita mi brazo de micrófono?",
             "Suma el peso del micrófono, la araña y el filtro antipop, y busca un brazo "
             "cuyo rango de carga incluya ese total con margen. Un brazo trabajando al "
             "límite de su muelle se vence poco a poco durante la emisión."),
            ("¿Qué rosca usan los micrófonos y los brazos?",
             "Conviven dos medidas: 3/8 de pulgada, habitual en soportes europeos, y 5/8 "
             "de pulgada, estándar en micrófonos. Casi todos los kits traen un adaptador "
             "metálico pequeño que convierte una en otra; guárdalo, porque perderlo "
             "bloquea el montaje entero."),
            ("¿Vale la pena un brazo caro?",
             "El salto de calidad que se nota está en el paso de un brazo flojo a uno "
             "sólido, no de uno sólido a uno de lujo. Lo que pagas de más son muelles "
             "internos silenciosos, canalización del cable y acabados; útil si mueves el "
             "micro en directo, prescindible si lo dejas fijo."),
        ],
        "body": """
<h2 id="por-que">Por qué importa tanto</h2>
<p>Todo lo que has leído sobre acercarte al micrófono depende de poder sostenerlo cerca
de la boca sin que esté apoyado en la mesa. Eso es el brazo. Y todo lo que golpea la
mesa viaja por la madera hasta la cápsula. Eso lo corta la araña.</p>
<table>
<thead><tr><th>Problema</th><th>Lo resuelve</th></tr></thead>
<tbody>
<tr><td>Hablas lejos porque el micro está en la mesa</td><td>Brazo</td></tr>
<tr><td>Se graban las teclas y los golpes de codo</td><td>Araña</td></tr>
<tr><td>El micrófono ocupa medio escritorio</td><td>Brazo</td></tr>
<tr><td>Las «p» explotan</td><td>Filtro antipop</td></tr>
<tr><td>Zumbido grave del edificio</td><td>Araña + filtro paso alto</td></tr>
</tbody></table>
<div class="note">
<strong>Orden de compra:</strong> micrófono, brazo, antipop, araña. Si el presupuesto
llega justo, la araña puede esperar; el brazo no.
</div>

<h2 id="brazo">Elegir brazo</h2>
<ul class="checks">
<li><strong>Capacidad de peso.</strong> El dato que más se ignora y el que más
devoluciones causa. Suma micro + araña + antipop.</li>
<li><strong>Tipo de anclaje.</strong> La pinza de sobremesa exige un canto libre de
hasta unos 5 cm; el pasante necesita un agujero en la mesa pero aguanta mucho más.</li>
<li><strong>Muelles internos o externos.</strong> Los internos no enganchan cables ni
pellizcan dedos, y hacen menos ruido al moverlos en directo.</li>
<li><strong>Canalización del cable.</strong> Un cable suelto golpeando el tubo se oye.</li>
<li><strong>Alcance.</strong> Mide de verdad la distancia entre el canto de tu mesa y tu
boca antes de comprar.</li>
</ul>
<p><strong>Señal de alarma:</strong> si un brazo no publica su rango de peso, es porque
no aguanta gran cosa.</p>

<h2 id="arana">Elegir araña</h2>
<p>La araña debe ser la del diámetro de tu micrófono. No es un accesorio universal.</p>
<ul class="checks">
<li><strong>Diámetro del cuerpo.</strong> Demasiado holgada y el micro se descuelga;
demasiado apretada y transmite la vibración igual que un soporte rígido.</li>
<li><strong>Elásticos de repuesto.</strong> Las gomas se dan de sí y acaban cediendo. Que
se puedan sustituir es lo que separa una araña de dos años de una de diez.</li>
<li><strong>Soporte rígido no es araña.</strong> Muchos micrófonos vienen con una pinza
fija que no aísla nada; la suspensión elástica casi siempre se compra aparte.</li>
<li><strong>Peso combinado.</strong> Súmalo al del micro para el cálculo del brazo.</li>
</ul>

<h2 id="roscas">Roscas y adaptadores</h2>
<p>El problema más tonto de todo el montaje, y el que más gente deja a medias un domingo
por la tarde.</p>
<table>
<thead><tr><th>Rosca</th><th>Dónde aparece</th><th>Nota</th></tr></thead>
<tbody>
<tr><td>3/8"</td><td>Pies y brazos, sobre todo europeos</td><td>La más común en soportes</td></tr>
<tr><td>5/8"</td><td>Micrófonos y arañas</td><td>Estándar de micrófono</td></tr>
<tr><td>1/4"</td><td>Cámaras y trípodes de foto</td><td>Necesita adaptador aparte</td></tr>
</tbody></table>
<p>El conversor es una pieza metálica pequeña que suele venir dentro de la bolsa del
brazo o pegada con cinta a la araña. <strong>Guárdalo en su sitio.</strong> Perderlo
significa no poder montar nada hasta que compres otro.</p>

<h2 id="montaje">Montaje que no se vence</h2>
<ol>
<li><strong>Aprieta la pinza a fondo</strong> y comprueba que el canto de la mesa no se
marque; si se marca, pon un trozo de fieltro.</li>
<li><strong>Tensa los muelles</strong> hasta que el brazo se quede donde lo dejas sin
caer poco a poco.</li>
<li><strong>Deja holgura en el cable</strong> en cada articulación, para que no tire al
mover el brazo.</li>
<li><strong>Coloca el antipop a un palmo</strong> de la cápsula, no pegado.</li>
<li><strong>Prueba el golpe:</strong> da un puñetazo suave a la mesa mientras grabas. Si
se oye un golpe seco, la araña o la pinza no están haciendo su trabajo.</li>
<li><strong>Revisa la tensión al mes.</strong> Los muelles se relajan y el brazo empieza
a vencerse hacia la mesa.</li>
</ol>
<p>Con el micro bien colocado, ajusta la cadena de sonido en
<a href="../configurar-microfono-obs/">OBS</a>. Y si sigues oyendo el cuarto, el problema
está en otro sitio: <a href="../quitar-ruido-de-fondo/">quitar el ruido de fondo</a>.</p>
""",
    }
