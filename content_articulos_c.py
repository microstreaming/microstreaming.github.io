# -*- coding: utf-8 -*-
"""Bloque C: tecnica, procesado, problemas y acustica.

Paginas informacionales. Son las que captan busquedas de problema y
alimentan con enlaces internos a las fichas comerciales.
"""


def add_pages(PAGES, SITE):

    PAGES["phantom-48v/"] = {
        "title": "Alimentación phantom 48 V: qué es y cuándo hace falta",
        "desc": ("Qué es la alimentación phantom de 48 V, qué micrófonos la "
                 "necesitan, en qué orden encenderla y si puede dañar un micrófono "
                 "dinámico."),
        "h1": "Phantom 48 V: el botón que explica la mitad de los «no se oye nada»",
        "crumb": "Phantom 48 V",
        "article": True, "kind": "Guía",
        "lede": ("Un interruptor pequeño que decide si tu condensador funciona o no. "
                 "Y la causa número uno de micrófonos nuevos que parecen defectuosos."),
        "toc": [
            ("que-es", "Qué es"),
            ("quien", "Quién la necesita"),
            ("orden", "El orden correcto"),
            ("dinamicos", "¿Daña a los dinámicos?"),
        ],
        "faq": [
            ("¿Qué es la alimentación phantom de 48 V?",
             "Es una tensión continua que la interfaz o el mezclador envía por el propio "
             "cable XLR para alimentar la electrónica interna de un micrófono de "
             "condensador. Se llama fantasma porque viaja por los mismos conductores que "
             "la señal de audio, sin cable adicional."),
            ("¿Todos los micrófonos necesitan phantom?",
             "No. Solo los condensadores con salida XLR. Los dinámicos generan su propia "
             "señal y no la necesitan, y los micrófonos USB se alimentan por el puerto."),
            ("¿El phantom de 48 V puede dañar un micrófono dinámico?",
             "Con una interfaz moderna y un cable XLR balanceado en buen estado, no. El "
             "riesgo real aparece con cables defectuosos, con conexiones no balanceadas o "
             "con micrófonos de cinta antiguos, que sí pueden sufrir daños."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>Un micrófono de condensador lleva electrónica dentro y esa electrónica necesita
corriente. En lugar de añadir un cable de alimentación, se aprovechan los mismos
conductores del cable XLR para enviar una tensión continua de 48 voltios.</p>
<p>Ese es todo el misterio. Se llama «fantasma» porque el audio y la alimentación viajan
juntos sin estorbarse.</p>
<div class="note">
<strong>Si tu condensador nuevo «no suena» o suena bajísimo con ruido, revisa este botón
antes de pensar en una devolución.</strong> Suele estar marcado como <code>+48V</code> o
<code>P48</code>.
</div>

<h2 id="quien">Quién la necesita</h2>
<table>
<thead><tr><th>Tipo de micrófono</th><th>¿Phantom?</th><th>Nota</th></tr></thead>
<tbody>
<tr><td>Condensador XLR</td><td>Sí, obligatoria</td><td>Sin ella no funciona</td></tr>
<tr><td>Dinámico XLR</td><td>No</td><td>No le aporta nada</td></tr>
<tr><td>Micrófono USB</td><td>No</td><td>Se alimenta por el puerto</td></tr>
<tr><td>Electret de solapa</td><td>No, usa plug-in power</td><td>Tensión mucho menor</td></tr>
<tr><td>Micrófono de cinta</td><td>No, y con cuidado</td><td>Puede dañarse</td></tr>
<tr><td>Preamplificador en línea</td><td>Sí</td><td>Se alimenta del phantom</td></tr>
</tbody></table>

<h2 id="orden">El orden correcto</h2>
<ol>
<li><strong>Baja el volumen</strong> de auriculares y monitores.</li>
<li><strong>Conecta el cable XLR</strong> al micrófono y a la interfaz.</li>
<li><strong>Activa el phantom.</strong></li>
<li><strong>Espera unos segundos</strong> a que el micrófono se estabilice.</li>
<li><strong>Sube la ganancia.</strong></li>
</ol>
<p>Y al terminar, exactamente al revés: baja volumen, apaga phantom, espera, desconecta.
Conectar o desconectar con el phantom activo produce un golpe fuerte que puede dañar
altavoces y oídos.</p>

<h2 id="dinamicos">¿Daña a los dinámicos?</h2>
<p>Es la duda clásica. Con equipo moderno y cables en condiciones, no: un dinámico
balanceado recibe la misma tensión en los dos conductores de señal y no circula corriente
por su bobina.</p>
<p>Los casos en los que sí hay riesgo real:</p>
<ul class="checks">
<li><strong>Cables con un conductor roto</strong> o mal soldados.</li>
<li><strong>Conexiones no balanceadas</strong> o adaptadores raros.</li>
<li><strong>Micrófonos de cinta vintage</strong>, que son otra familia y sí se dañan.</li>
<li><strong>Conectar en caliente</strong> con el phantom encendido, de forma repetida.</li>
</ul>
<p>Si tu micro es condensador, lee también
<a href="../microfono-condensador/">cómo elegirlo</a>. Y para la interfaz,
<a href="../interfaz-de-audio/">qué mirar antes de comprar</a>.</p>
""",
    }

    PAGES["efecto-proximidad/"] = {
        "title": "Efecto de proximidad: por qué tu voz suena más grave de cerca",
        "desc": ("Qué es el efecto de proximidad en un micrófono, qué patrones lo "
                 "tienen, cómo usarlo a tu favor y cómo corregirlo cuando enturbia "
                 "la voz."),
        "h1": "Efecto de proximidad: la herramienta que casi todos sufren sin saberlo",
        "crumb": "Efecto de proximidad",
        "article": True, "kind": "Guía",
        "lede": ("Ese cuerpo grave y cálido de la voz de radio no viene del "
                 "micrófono: viene de la distancia. Y se puede dosificar."),
        "toc": [
            ("que-es", "Qué es"),
            ("quien", "Qué micrófonos lo tienen"),
            ("favor", "Usarlo a tu favor"),
            ("corregir", "Cuando estorba"),
        ],
        "faq": [
            ("¿Qué es el efecto de proximidad en un micrófono?",
             "Es el aumento de las frecuencias graves que se produce al acercarse mucho a "
             "un micrófono direccional. Cuanto más cerca hablas, más cuerpo grave suma la "
             "voz, hasta volverse turbia si te pegas demasiado."),
            ("¿Qué micrófonos tienen efecto de proximidad?",
             "Los direccionales: cardioide, supercardioide y bidireccional. Los "
             "omnidireccionales no lo presentan, porque no funcionan por diferencia de "
             "presión entre las dos caras del diafragma."),
            ("¿Cómo se quita el efecto de proximidad?",
             "Alejándote unos centímetros, activando el filtro de graves del micrófono si "
             "lo tiene, o aplicando un filtro paso alto en torno a 80-100 Hz al grabar. "
             "La distancia es siempre la solución más natural."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>Los micrófonos direccionales consiguen su direccionalidad comparando la presión que
llega por delante y por detrás del diafragma. Esa comparación funciona bien a distancias
normales, pero muy de cerca la diferencia de presión entre ambas caras se dispara en las
frecuencias graves.</p>
<p>El resultado audible: <strong>a 2 cm tu voz suena enorme y grave; a 30 cm suena
natural; a un metro suena delgada y con cuarto</strong>.</p>

<h2 id="quien">Qué micrófonos lo tienen</h2>
<table>
<thead><tr><th>Patrón</th><th>Efecto de proximidad</th></tr></thead>
<tbody>
<tr><td>Cardioide</td><td>Sí, moderado</td></tr>
<tr><td>Supercardioide</td><td>Sí, algo mayor</td></tr>
<tr><td>Bidireccional</td><td>Sí, el más marcado</td></tr>
<tr><td>Omnidireccional</td><td>No</td></tr>
</tbody></table>
<div class="note">
<strong>Dato útil:</strong> si usas un micro multipatrón y te molesta el grave al
acercarte, cambiar a omnidireccional lo elimina. A cambio, entra más cuarto.
</div>

<h2 id="favor">Usarlo a tu favor</h2>
<ul class="checks">
<li><strong>Voz delgada o aguda:</strong> acércate. Ganarás cuerpo sin tocar un
ecualizador.</li>
<li><strong>Tono íntimo</strong> para narración: el acercamiento es la forma natural de
conseguirlo.</li>
<li><strong>Cuarto ruidoso:</strong> acercarte sube tu voz sobre el ruido y además te da
cuerpo. Dos beneficios de un solo gesto.</li>
<li><strong>Control dinámico en directo:</strong> los cantantes lo usan constantemente,
acercando el micro en los susurros y alejándolo en los gritos.</li>
</ul>

<h2 id="corregir">Cuando estorba</h2>
<p>Síntoma típico: tu voz suena retumbante, embarullada, cuesta entender las palabras
aunque el volumen sea correcto.</p>
<ol>
<li><strong>Aléjate 5 cm</strong> y vuelve a escuchar. Suele bastar.</li>
<li><strong>Activa el filtro de graves</strong> del micrófono si lo tiene.</li>
<li><strong>Filtro paso alto a 80-100 Hz</strong> en la cadena de proceso.</li>
<li><strong>Habla fuera de eje</strong>: reduce algo el efecto y de paso las explosivas.</li>
</ol>
<p>Cuidado con pasarse: recortar graves de más deja la voz fina y telefónica. El objetivo
es quitar el barro, no el cuerpo.</p>
<p>Relacionado: <a href="../ecualizar-la-voz/">cómo ecualizar la voz</a> y
<a href="../ganancia-del-microfono/">ajustar la ganancia</a>.</p>
""",
    }

    PAGES["ganancia-del-microfono/"] = {
        "title": "Cómo ajustar la ganancia del micrófono correctamente",
        "desc": ("Cómo ajustar la ganancia del micrófono: qué nivel buscar, por qué "
                 "no debe llegar a 0 dB, diferencia entre ganancia y volumen y cómo "
                 "evitar el ruido."),
        "h1": "Ganancia del micrófono: ni al máximo ni al mínimo",
        "crumb": "Ganancia",
        "article": True, "kind": "Guía",
        "lede": ("La mitad de los problemas de ruido que la gente intenta resolver "
                 "con plugins son en realidad un mando de ganancia mal puesto."),
        "toc": [
            ("que-es", "Ganancia no es volumen"),
            ("nivel", "Qué nivel buscar"),
            ("ajustar", "Cómo ajustarla en tres minutos"),
            ("sintomas", "Diagnóstico por síntoma"),
        ],
        "faq": [
            ("¿Cuál es el nivel correcto de ganancia del micrófono?",
             "El que haga que tus picos normales al hablar lleguen a unos -12 dB, dejando "
             "margen por encima. Llegar a 0 dB significa saturar, y eso no se arregla "
             "después."),
            ("¿Qué diferencia hay entre ganancia y volumen?",
             "La ganancia amplifica la señal al entrar, antes de grabarla; el volumen "
             "ajusta lo que escuchas a la salida. Subir el volumen no mejora una señal "
             "grabada con poca ganancia, y subir la ganancia de más arruina la grabación."),
            ("¿Por qué se oye ruido de fondo al subir la ganancia?",
             "Porque la ganancia amplifica todo por igual: tu voz y el ruido de la sala y "
             "del preamplificador. Si necesitas mucha ganancia es señal de que estás "
             "demasiado lejos del micrófono."),
        ],
        "body": """
<h2 id="que-es">Ganancia no es volumen</h2>
<p>Es la confusión que está detrás de casi todos los problemas.</p>
<table>
<thead><tr><th></th><th>Ganancia</th><th>Volumen</th></tr></thead>
<tbody>
<tr><td>Dónde actúa</td><td>A la entrada</td><td>A la salida</td></tr>
<tr><td>Afecta a lo grabado</td><td>Sí</td><td>No</td></tr>
<tr><td>Si te pasas</td><td>Satura, irreversible</td><td>Solo molesta al oído</td></tr>
<tr><td>Si te quedas corto</td><td>Ruido al amplificar después</td><td>Sin consecuencia</td></tr>
</tbody></table>
<div class="note">
<strong>La ganancia se decide antes de grabar y no tiene vuelta atrás.</strong> El
volumen se puede cambiar mil veces.
</div>

<h2 id="nivel">Qué nivel buscar</h2>
<ul class="checks">
<li><strong>Picos normales en torno a -12 dB.</strong> Ese es el objetivo.</li>
<li><strong>Nunca tocar 0 dB.</strong> Ahí empieza la distorsión digital.</li>
<li><strong>Deja margen para los gritos.</strong> Ajusta hablando a tu volumen más alto,
no al normal.</li>
<li><strong>El ruido de fondo, muy por debajo</strong>, idealmente bajo -60 dB.</li>
</ul>

<h2 id="ajustar">Cómo ajustarla en tres minutos</h2>
<ol>
<li><strong>Colócate donde vas a hablar de verdad</strong>, a la distancia real.</li>
<li><strong>Ganancia al mínimo</strong> para empezar.</li>
<li><strong>Habla a tu volumen más alto</strong>, no al de prueba. Mucha gente ajusta
susurrando y luego satura.</li>
<li><strong>Sube la ganancia poco a poco</strong> hasta que esos picos lleguen a -12 dB.</li>
<li><strong>Calla y mira el medidor.</strong> Si el silencio se mueve mucho, tienes
demasiada ganancia o demasiado ruido.</li>
<li><strong>Graba treinta segundos y escúchalos</strong> con auriculares.</li>
</ol>

<h2 id="sintomas">Diagnóstico por síntoma</h2>
<table>
<thead><tr><th>Síntoma</th><th>Causa</th><th>Arreglo</th></tr></thead>
<tbody>
<tr><td>Distorsión en las palabras fuertes</td><td>Ganancia alta</td><td>Bajar y repetir la prueba de grito</td></tr>
<tr><td>Siseo constante</td><td>Ganancia alta por estar lejos</td><td>Acercarse y bajar ganancia</td></tr>
<tr><td>Voz muy baja aun al máximo</td><td>Dinámico con interfaz floja</td><td>Acercarse; valorar preamplificador</td></tr>
<tr><td>Volumen que sube y baja solo</td><td>Control automático activado</td><td>Desactivarlo en el sistema</td></tr>
<tr><td>Ruido que sube al callar</td><td>Compresor mal ajustado</td><td>Subir su umbral</td></tr>
</tbody></table>
<p>Para la cadena completa, <a href="../configurar-microfono-obs/">configurar el
micrófono en OBS</a>.</p>
""",
    }

    PAGES["compresor-de-voz/"] = {
        "title": "Compresor para voz: qué hace y cómo ajustarlo sin estropearla",
        "desc": ("Compresor de voz explicado sin jerga: umbral, ratio, ataque y "
                 "liberación, con valores de partida para locución, podcast y "
                 "directo."),
        "h1": "Compresor para voz: iguala, no engorda",
        "crumb": "Compresor de voz",
        "article": True, "kind": "Guía",
        "lede": ("Es el proceso que hace que una voz suene profesional y constante. "
                 "También el que más fácil es pasarse de rosca."),
        "toc": [
            ("que-hace", "Qué hace realmente"),
            ("controles", "Los cuatro controles"),
            ("valores", "Valores de partida"),
            ("errores", "Señales de que te pasaste"),
        ],
        "faq": [
            ("¿Qué hace un compresor de voz?",
             "Reduce la diferencia entre las partes más fuertes y las más suaves de tu "
             "voz. El resultado es un nivel más constante, que se entiende mejor y no "
             "obliga al oyente a tocar el volumen."),
            ("¿Qué valores de compresor debo usar para voz hablada?",
             "Un punto de partida razonable es ratio 3:1, umbral que produzca unos 6 dB "
             "de reducción en los picos, ataque de unos 5-10 ms y liberación de 60-100 "
             "ms. A partir de ahí se ajusta escuchando."),
            ("¿El compresor sube el ruido de fondo?",
             "Sí, indirectamente. Al bajar los picos y recuperar nivel después, el ruido "
             "de las partes silenciosas sube con él. Por eso conviene limpiar antes de "
             "comprimir, no al revés."),
        ],
        "body": """
<h2 id="que-hace">Qué hace realmente</h2>
<p>Imagina que alguien baja el volumen justo cuando gritas y lo vuelve a subir cuando
hablas bajo. Eso es un compresor, hecho automáticamente y en milisegundos.</p>
<p>El objetivo no es que suene más fuerte, sino <strong>más constante</strong>. Lo de
sonar más fuerte viene después, al recuperar nivel.</p>
<div class="note">
<strong>Orden importa:</strong> limpia primero, comprime después. Comprimir antes de
limpiar amplifica el ruido que ibas a quitar.
</div>

<h2 id="controles">Los cuatro controles</h2>
<table>
<thead><tr><th>Control</th><th>Qué decide</th><th>Si te pasas</th></tr></thead>
<tbody>
<tr><td>Umbral</td><td>A partir de qué nivel actúa</td><td>Comprime todo, incluido el ruido</td></tr>
<tr><td>Ratio</td><td>Cuánto reduce lo que pasa el umbral</td><td>Voz aplastada, sin vida</td></tr>
<tr><td>Ataque</td><td>Cuánto tarda en reaccionar</td><td>Muy rápido: mata las consonantes</td></tr>
<tr><td>Liberación</td><td>Cuánto tarda en soltar</td><td>Muy lenta: la voz «respira» raro</td></tr>
</tbody></table>
<p>Hay un quinto, la <strong>ganancia de compensación</strong>, que recupera el volumen
perdido. Súbela solo lo justo para igualar con el sonido sin comprimir.</p>

<h2 id="valores">Valores de partida</h2>
<table>
<thead><tr><th>Uso</th><th>Ratio</th><th>Reducción objetivo</th><th>Ataque / Liberación</th></tr></thead>
<tbody>
<tr><td>Locución y voz en off</td><td>3:1</td><td>4-6 dB</td><td>10 ms / 100 ms</td></tr>
<tr><td>Podcast conversacional</td><td>3:1</td><td>6 dB</td><td>6 ms / 80 ms</td></tr>
<tr><td>Directo y gaming</td><td>4:1</td><td>6-9 dB</td><td>5 ms / 60 ms</td></tr>
<tr><td>Voz muy dinámica</td><td>4:1 o dos compresores suaves</td><td>8 dB</td><td>5 ms / 70 ms</td></tr>
</tbody></table>
<p>Fíjate en que el ratio apenas cambia. Lo que de verdad ajustas es el umbral, mirando
cuántos decibelios de reducción marca el medidor.</p>

<h2 id="errores">Señales de que te pasaste</h2>
<ul class="checks">
<li><strong>El medidor de reducción nunca vuelve a cero.</strong> Estás comprimiendo
también el silencio.</li>
<li><strong>Se oye el ruido de fondo subir y bajar</strong> entre frases.</li>
<li><strong>Las consonantes suenan apagadas</strong>: ataque demasiado rápido.</li>
<li><strong>La voz cansa</strong> a los diez minutos. Es el síntoma más fiable.</li>
<li><strong>Todo suena igual de fuerte</strong>, sin matiz ni intención.</li>
</ul>
<p>Antes del compresor, asegúrate de que la
<a href="../ganancia-del-microfono/">ganancia</a> está bien. Después,
<a href="../ecualizar-la-voz/">la ecualización</a>.</p>
""",
    }

    PAGES["ecualizar-la-voz/"] = {
        "title": "Cómo ecualizar la voz: las cuatro zonas que importan",
        "desc": ("Guía práctica para ecualizar la voz en OBS o en tu editor: qué "
                 "hace cada banda de frecuencia, qué recortar y qué no tocar nunca."),
        "h1": "Ecualizar la voz: quitar estorba menos que añadir",
        "crumb": "Ecualizar la voz",
        "article": True, "kind": "Guía",
        "lede": ("Un ecualizador no mejora una toma mala, pero sí puede arruinar una "
                 "buena. La regla que funciona: recorta lo que sobra antes de "
                 "realzar nada."),
        "toc": [
            ("principio", "El principio básico"),
            ("zonas", "Las cuatro zonas"),
            ("recetas", "Recetas por problema"),
            ("no-hacer", "Lo que no hay que hacer"),
        ],
        "faq": [
            ("¿Cómo se ecualiza una voz para que suene profesional?",
             "Empieza recortando: un filtro paso alto en torno a 80 Hz para quitar "
             "retumbe, y una reducción suave en la zona de 200-400 Hz si la voz suena "
             "embarullada. Solo después, si hace falta, realza ligeramente la zona de "
             "presencia alrededor de 3-5 kHz."),
            ("¿Qué frecuencia hay que cortar en la voz?",
             "Por debajo de 80 Hz casi nunca hay información útil de voz hablada, así que "
             "ese corte es seguro. El resto depende de cada voz: no existe una receta "
             "universal, hay que escuchar."),
            ("¿Es mejor ecualizar antes o después de comprimir?",
             "Lo habitual es recortar lo problemático antes del compresor, para que este "
             "no reaccione a frecuencias que vas a eliminar, y dejar los realces "
             "estéticos para después."),
        ],
        "body": """
<h2 id="principio">El principio básico</h2>
<div class="note">
<strong>Recortar suena natural; realzar suena artificial.</strong> Si una voz te parece
poco brillante, antes de subir agudos prueba a bajar los medios graves: el brillo
aparece solo.
</div>
<p>Y una condición previa: si la toma tiene eco de sala, ningún ecualizador lo va a
quitar. Eso se arregla antes de grabar, no después.</p>

<h2 id="zonas">Las cuatro zonas</h2>
<table>
<thead><tr><th>Zona</th><th>Qué aporta</th><th>Qué pasa si sobra</th></tr></thead>
<tbody>
<tr><td>Por debajo de 80 Hz</td><td>Nada útil en voz</td><td>Retumbe, golpes, tráfico</td></tr>
<tr><td>100-250 Hz</td><td>Cuerpo y calidez</td><td>Voz hinchada</td></tr>
<tr><td>250-500 Hz</td><td>Transición</td><td>Sonido a caja, embarullado</td></tr>
<tr><td>3-6 kHz</td><td>Presencia, claridad</td><td>Cansancio, dureza</td></tr>
<tr><td>6-9 kHz</td><td>Aire y detalle</td><td>Sibilancia insoportable</td></tr>
</tbody></table>

<h2 id="recetas">Recetas por problema</h2>
<ul class="checks">
<li><strong>Suena a bidón o a caja:</strong> baja 2-3 dB con una campana ancha entre 250
y 400 Hz.</li>
<li><strong>Suena turbia estando cerca del micro:</strong> es
<a href="../efecto-proximidad/">efecto de proximidad</a>. Aléjate o aplica paso alto más
arriba, hasta 100-120 Hz.</li>
<li><strong>Las eses silban:</strong> no uses ecualizador fijo; usa un de-esser, que
actúa solo cuando aparece la sibilancia.</li>
<li><strong>Falta claridad:</strong> prueba primero a recortar 300 Hz. Si no basta,
realza 1-2 dB alrededor de 4 kHz, no más.</li>
<li><strong>Voz muy delgada:</strong> acércate al micrófono antes de tocar nada.</li>
</ul>

<h2 id="no-hacer">Lo que no hay que hacer</h2>
<ol>
<li><strong>Copiar los ajustes de otra persona.</strong> Cada voz y cada micro son
distintos.</li>
<li><strong>Realces grandes.</strong> Más de 3 dB en voz casi siempre suena mal.</li>
<li><strong>Usar la curva «sonrisa»</strong> de graves y agudos arriba: para voz es
desastrosa.</li>
<li><strong>Ecualizar sin referencia.</strong> Compara constantemente con el sonido sin
procesar.</li>
<li><strong>Ajustar con los altavoces del portátil.</strong> Usa auriculares.</li>
<li><strong>Intentar arreglar con EQ</strong> lo que es ruido o reverberación.</li>
</ol>
<p>Antes: <a href="../ganancia-del-microfono/">ganancia</a> y
<a href="../compresor-de-voz/">compresor</a>. Si el problema es el cuarto,
<a href="../tratamiento-acustico-casero/">tratamiento acústico</a>.</p>
""",
    }

    PAGES["microfono-no-funciona-windows/"] = {
        "title": "El micrófono no funciona en Windows: diagnóstico ordenado",
        "desc": ("El micrófono no funciona o no se oye en Windows: permisos, "
                 "dispositivo predeterminado, uso exclusivo, controladores y "
                 "soluciones por síntoma."),
        "h1": "El micrófono no funciona en Windows: empieza por el final",
        "crumb": "No funciona en Windows",
        "article": True, "kind": "Guía",
        "lede": ("Casi nadie tiene un micrófono averiado. Casi todo el mundo tiene un "
                 "permiso desactivado, un dispositivo equivocado o una aplicación que "
                 "se lo ha quedado."),
        "toc": [
            ("orden", "El orden de diagnóstico"),
            ("permisos", "Permisos del sistema"),
            ("dispositivo", "Dispositivo equivocado"),
            ("exclusivo", "Otra aplicación lo tiene"),
            ("tabla", "Soluciones por síntoma"),
        ],
        "faq": [
            ("¿Por qué Windows no detecta mi micrófono?",
             "Las causas más frecuentes son que el acceso al micrófono esté desactivado "
             "en la configuración de privacidad, que el dispositivo esté deshabilitado en "
             "el panel de sonido, o que otra aplicación lo tenga en uso exclusivo."),
            ("¿Por qué mi micrófono se oye muy bajo en Windows?",
             "Normalmente porque el nivel de entrada está bajo en las propiedades del "
             "dispositivo, o porque el micrófono es dinámico y la entrada no tiene "
             "ganancia suficiente. Revisa también que no esté activo un refuerzo que "
             "distorsione."),
            ("¿Qué es el modo exclusivo de un micrófono en Windows?",
             "Es una opción que permite a una aplicación tomar el control total del "
             "dispositivo, impidiendo que otras lo usen al mismo tiempo. Si una "
             "aplicación lo activa, el resto deja de oír el micrófono."),
        ],
        "body": """
<h2 id="orden">El orden de diagnóstico</h2>
<p>Empieza por lo más probable y lo más barato, no por reinstalar controladores.</p>
<ol>
<li><strong>¿Está conectado y encendido?</strong> Parece obvio; con interfaces y micros
USB con interruptor, no lo es.</li>
<li><strong>¿Tiene permiso el sistema?</strong></li>
<li><strong>¿Es el dispositivo correcto</strong> el seleccionado?</li>
<li><strong>¿Lo tiene otra aplicación?</strong></li>
<li><strong>¿El nivel está a cero?</strong></li>
<li>Y solo entonces: controladores.</li>
</ol>
<div class="note">
<strong>Prueba de oro antes de nada:</strong> abre la Grabadora de voz de Windows y graba
diez segundos. Si ahí se oye, el micrófono funciona y el problema está en la otra
aplicación.
</div>

<h2 id="permisos">Permisos del sistema</h2>
<p>En <strong>Configuración → Privacidad y seguridad → Micrófono</strong> hay tres
interruptores que deben estar activos, y fallar en cualquiera produce el mismo síntoma:</p>
<ul class="checks">
<li>Acceso al micrófono, a nivel de equipo.</li>
<li>Permitir que las aplicaciones accedan al micrófono.</li>
<li>Permitir que las <strong>aplicaciones de escritorio</strong> accedan. Este es el que
más se pasa por alto, y es el que afecta a programas como OBS.</li>
</ul>

<h2 id="dispositivo">Dispositivo equivocado</h2>
<p>Windows cambia el «dispositivo predeterminado» cuando conectas algo nuevo. Si tu
aplicación está puesta en «Predeterminado», un día deja de usar tu micro sin que hayas
tocado nada.</p>
<ul class="checks">
<li>En la aplicación, <strong>selecciona tu micrófono por su nombre</strong>, nunca
«Predeterminado».</li>
<li>En <strong>Panel de control de sonido → Grabación</strong>, comprueba que el
dispositivo no esté deshabilitado. Haz clic derecho y activa «Mostrar dispositivos
deshabilitados».</li>
<li>Comprueba el <strong>nivel</strong> en Propiedades → Niveles.</li>
</ul>

<h2 id="exclusivo">Otra aplicación lo tiene</h2>
<p>En <strong>Propiedades del micrófono → Opciones avanzadas</strong> existe «Permitir
que las aplicaciones tomen control exclusivo de este dispositivo». Desactívalo si varias
aplicaciones necesitan el micro a la vez.</p>
<p>Y cierra del todo lo que pueda estar reteniéndolo: clientes de videollamada que siguen
en segundo plano son los sospechosos habituales.</p>

<h2 id="tabla">Soluciones por síntoma</h2>
<table>
<thead><tr><th>Síntoma</th><th>Causa probable</th><th>Qué hacer</th></tr></thead>
<tbody>
<tr><td>No aparece en la lista</td><td>Deshabilitado o sin permiso</td><td>Mostrar deshabilitados; revisar privacidad</td></tr>
<tr><td>Aparece pero no capta</td><td>Nivel a cero o silenciado</td><td>Propiedades → Niveles</td></tr>
<tr><td>Funciona en una app y no en otra</td><td>Control exclusivo</td><td>Desactivar en Opciones avanzadas</td></tr>
<tr><td>Se oye muy bajo</td><td>Dinámico con poca ganancia</td><td>Acercarse; preamplificador</td></tr>
<tr><td>Se oye con eco metálico</td><td>Efectos del sistema activos</td><td>Desactivar mejoras de audio</td></tr>
<tr><td>Deja de ir tras actualizar</td><td>Controlador sustituido</td><td>Reinstalar el del fabricante</td></tr>
</tbody></table>
<p>Si el micro funciona pero suena mal, el problema es otro:
<a href="../quitar-ruido-de-fondo/">ruido de fondo</a> o
<a href="../ganancia-del-microfono/">ganancia</a>.</p>
""",
    }

    PAGES["latencia-del-microfono/"] = {
        "title": "Latencia del micrófono: por qué te oyes con retardo y cómo quitarlo",
        "desc": ("Qué causa la latencia al monitorizar el micrófono, qué es el "
                 "tamaño de búfer, cómo usar el monitoreo directo y qué latencia es "
                 "aceptable."),
        "h1": "Latencia del micrófono: oírte con retardo tiene arreglo",
        "crumb": "Latencia",
        "article": True, "kind": "Guía",
        "lede": ("Escucharte a ti mismo con unos milisegundos de retraso resulta "
                 "insoportable y te hace tropezar al hablar. No es cosa tuya: es "
                 "física y configuración."),
        "toc": [
            ("por-que", "Por qué ocurre"),
            ("directo", "Monitoreo directo: la solución real"),
            ("bufer", "El tamaño de búfer"),
            ("aceptable", "Cuánta latencia es aceptable"),
        ],
        "faq": [
            ("¿Por qué me oigo con retardo en el micrófono?",
             "Porque la señal tiene que entrar al ordenador, pasar por el procesado y "
             "volver a salir a los auriculares. Ese viaje lleva tiempo, y cuanto mayor es "
             "el búfer de audio, más retardo se acumula."),
            ("¿Qué es el monitoreo directo?",
             "Es una función de las interfaces que envía la señal del micrófono "
             "directamente a los auriculares sin pasar por el ordenador. Al no hacer el "
             "viaje de ida y vuelta, el retardo es prácticamente nulo."),
            ("¿Qué tamaño de búfer debo usar?",
             "Para hablar y monitorizarte, cuanto más bajo mejor, siempre que no aparezcan "
             "cortes. Para mezclar o editar, uno alto es preferible porque da estabilidad "
             "y la latencia ya no importa."),
        ],
        "body": """
<h2 id="por-que">Por qué ocurre</h2>
<p>Cuando te escuchas a través del ordenador, tu voz recorre este camino:</p>
<ol>
<li>Micrófono → conversión a digital.</li>
<li>Entrada al sistema y espera en el <strong>búfer</strong>.</li>
<li>Procesado: filtros, compresor, lo que tengas puesto.</li>
<li>Salida, nueva espera en búfer.</li>
<li>Conversión a analógico → auriculares.</li>
</ol>
<p>Cada paso suma milisegundos. El búfer es el que más pesa, y existe por una razón: sin
él, el audio se cortaría constantemente.</p>
<div class="note">
<strong>El retardo no se elimina, se esquiva.</strong> La solución no es reducirlo a cero
en el ordenador, sino no pasar por el ordenador para escucharte.
</div>

<h2 id="directo">Monitoreo directo: la solución real</h2>
<p>Las interfaces llevan un mando o un botón que mezcla la señal del micrófono
directamente con lo que sale del ordenador, antes de digitalizarla. Lo oyes
instantáneamente.</p>
<ul class="checks">
<li><strong>Si tienes interfaz:</strong> busca «Direct Monitor» o un mando que diga
«Input / Playback». Esa es tu solución.</li>
<li><strong>Si tienes micro USB con salida de auriculares:</strong> muchos lo traen
integrado. Conecta los auriculares al micro, no al ordenador.</li>
<li><strong>Si no tienes ninguna de las dos:</strong> te tocará bajar el búfer, con sus
límites.</li>
</ul>
<p>Contrapartida: con monitoreo directo te oyes <em>sin</em> los efectos. Para hablar es
perfecto; para cantar con reverb de referencia, no.</p>

<h2 id="bufer">El tamaño de búfer</h2>
<table>
<thead><tr><th>Búfer</th><th>Latencia aprox.</th><th>Riesgo de cortes</th><th>Para qué</th></tr></thead>
<tbody>
<tr><td>64 muestras</td><td>Muy baja</td><td>Alto</td><td>Equipos potentes</td></tr>
<tr><td>128 muestras</td><td>Baja</td><td>Medio</td><td>Grabar hablando</td></tr>
<tr><td>256 muestras</td><td>Moderada</td><td>Bajo</td><td>Uso general</td></tr>
<tr><td>512 o más</td><td>Alta</td><td>Muy bajo</td><td>Mezcla y edición</td></tr>
</tbody></table>
<p>Baja el búfer hasta que empiecen los cortes y entonces sube un escalón. Ese es tu
punto.</p>

<h2 id="aceptable">Cuánta latencia es aceptable</h2>
<ul class="checks">
<li><strong>Por debajo de 10 ms:</strong> imperceptible para hablar.</li>
<li><strong>Entre 10 y 20 ms:</strong> se nota, se tolera.</li>
<li><strong>Por encima de 20 ms:</strong> molesta y te hace tropezar.</li>
<li><strong>Por encima de 40 ms:</strong> prácticamente imposible hablar escuchándote.</li>
</ul>
<p>Y un recordatorio: la latencia solo importa mientras te escuchas en directo. En la
grabación final no queda ni rastro.</p>
<p>Al elegir interfaz, comprueba que tenga monitoreo directo:
<a href="../interfaz-de-audio/">qué mirar antes de comprar</a>.</p>
""",
    }

    PAGES["tratamiento-acustico-casero/"] = {
        "title": "Tratamiento acústico casero: qué funciona y qué es tirar el dinero",
        "desc": ("Tratamiento acústico casero y barato: diferencia entre insonorizar "
                 "y acondicionar, qué materiales sirven, dónde colocarlos y qué no "
                 "hace nada."),
        "h1": "Tratamiento acústico casero: insonorizar y acondicionar no son lo mismo",
        "crumb": "Tratamiento acústico",
        "article": True, "kind": "Guía",
        "lede": ("La confusión entre esas dos palabras hace que mucha gente compre "
                 "espuma esperando no oír a los vecinos. No funciona así, y conviene "
                 "saberlo antes de gastar."),
        "toc": [
            ("diferencia", "La diferencia que lo cambia todo"),
            ("funciona", "Lo que sí funciona"),
            ("no-funciona", "Lo que no hace nada"),
            ("donde", "Dónde colocarlo"),
            ("plan", "Plan por presupuesto"),
        ],
        "faq": [
            ("¿La espuma acústica insonoriza una habitación?",
             "No. La espuma absorbe reflexiones dentro de la sala, lo que reduce el eco, "
             "pero no impide que el sonido entre o salga. Insonorizar requiere masa y "
             "hermeticidad: tabiques, puertas pesadas y sellado, no espuma."),
            ("¿Qué puedo usar para tratar mi cuarto sin gastar mucho?",
             "Mantas gruesas colgadas, cortinas pesadas con pliegues, una estantería llena "
             "de libros desordenados, alfombra y un sofá. Todo eso absorbe y difunde de "
             "forma efectiva sin comprar nada específico."),
            ("¿Dónde se colocan los paneles acústicos para grabar voz?",
             "La prioridad es la pared que tienes enfrente al hablar, porque ahí rebota tu "
             "voz de vuelta al micrófono. Después, las paredes laterales en el punto de "
             "primera reflexión y, si es posible, el techo sobre el puesto."),
        ],
        "body": """
<h2 id="diferencia">La diferencia que lo cambia todo</h2>
<table>
<thead><tr><th></th><th>Insonorizar</th><th>Acondicionar</th></tr></thead>
<tbody>
<tr><td>Objetivo</td><td>Que no entre ni salga sonido</td><td>Que la sala no resuene</td></tr>
<tr><td>Requiere</td><td>Masa, hermetismo, desacoplo</td><td>Absorción y difusión</td></tr>
<tr><td>Coste</td><td>Muy alto, obra</td><td>Bajo o nulo</td></tr>
<tr><td>Lo que resuelve</td><td>Vecinos, tráfico</td><td>Eco, sonido a cueva</td></tr>
<tr><td>Lo que no resuelve</td><td>El eco interior</td><td>El ruido que entra de fuera</td></tr>
</tbody></table>
<div class="note">
<strong>Para grabar en casa, lo que necesitas casi siempre es acondicionar.</strong> Es
lo barato y lo que de verdad cambia tus grabaciones.
</div>

<h2 id="funciona">Lo que sí funciona</h2>
<ul class="checks">
<li><strong>Mantas gruesas colgadas</strong> en la pared de enfrente. Es lo más eficaz
por cero euros.</li>
<li><strong>Cortinas pesadas y con pliegues.</strong> Lisas y finas no hacen casi nada.</li>
<li><strong>Estantería llena de libros</strong> de distintos tamaños: absorbe y difunde
a la vez.</li>
<li><strong>Alfombra</strong> sobre suelo duro.</li>
<li><strong>Un sofá o una cama</strong> en la habitación.</li>
<li><strong>Paneles de lana mineral</strong> si vas a comprar algo: mucho más eficaces
que la espuma, sobre todo en graves.</li>
</ul>

<h2 id="no-funciona">Lo que no hace nada</h2>
<ul class="checks">
<li><strong>Hueveras de cartón.</strong> El mito más persistente. No absorben; apenas
difunden, y son inflamables.</li>
<li><strong>Espuma fina de 2 cm</strong> repartida sin criterio: solo toca agudos y deja
el problema de medios intacto.</li>
<li><strong>Cuatro paneles sueltos</strong> en mitad de una pared grande.</li>
<li><strong>Cajas rígidas alrededor del micrófono:</strong> crean resonancias propias.</li>
<li><strong>Cualquier cosa</strong> con la esperanza de no oír a los vecinos.</li>
</ul>

<h2 id="donde">Dónde colocarlo</h2>
<ol>
<li><strong>La pared que tienes delante al hablar.</strong> Prioridad absoluta: ahí
rebota tu voz de vuelta al micro.</li>
<li><strong>Detrás del micrófono</strong>, si hablas hacia una pared cercana.</li>
<li><strong>Primeras reflexiones laterales:</strong> el punto donde un espejo en la pared
te reflejaría desde tu posición.</li>
<li><strong>Techo</strong> sobre el puesto, si puedes.</li>
<li><strong>Esquinas</strong> para los graves, aunque eso ya es otro nivel.</li>
</ol>

<h2 id="plan">Plan por presupuesto</h2>
<table>
<thead><tr><th>Presupuesto</th><th>Qué hacer</th><th>Mejora esperable</th></tr></thead>
<tbody>
<tr><td>Cero</td><td>Manta delante, alfombra, grabar en armario</td><td>Grande</td></tr>
<tr><td>Bajo</td><td>Cortina gruesa y estantería con libros</td><td>Notable</td></tr>
<tr><td>Medio</td><td>Paneles de lana mineral en primeras reflexiones</td><td>Clara</td></tr>
<tr><td>Alto</td><td>Paneles + trampas de graves en esquinas</td><td>Sala de verdad</td></tr>
</tbody></table>
<p>Y recuerda el atajo: acercarte al micrófono reduce el peso del cuarto más que cualquier
panel. Está explicado en <a href="../quitar-ruido-de-fondo/">quitar el ruido de
fondo</a>.</p>
""",
    }
