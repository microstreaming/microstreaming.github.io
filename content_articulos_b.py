# -*- coding: utf-8 -*-
"""Bloque B: equipo de apoyo y casos de uso.

Mezcla de paginas comerciales (interfaz, antipop, solapa, inalambrico) y
de intencion por situacion (gaming, cantar, videollamadas, voz en off).
"""


def add_pages(PAGES, SITE):

    PAGES["interfaz-de-audio/"] = {
        "title": "Interfaz de audio para micrófono: qué mirar antes de comprar",
        "desc": ("Guía para elegir interfaz de audio: ganancia, phantom 48 V, "
                 "monitoreo directo, número de entradas y qué especificaciones "
                 "ignorar."),
        "h1": "Interfaz de audio: la pieza que decide si tu micrófono rinde",
        "crumb": "Interfaz de audio",
        "article": True, "kind": "Guía",
        "lede": ("Puedes comprar el mejor micrófono XLR del mundo y arruinarlo con "
                 "una interfaz sin ganancia. Es la pieza más ignorada y la que más "
                 "quejas provoca."),
        "toc": [
            ("que-hace", "Qué hace realmente"),
            ("ganancia", "Ganancia: el dato que importa"),
            ("entradas", "Cuántas entradas"),
            ("ignorar", "Especificaciones que puedes ignorar"),
            ("elegir", "Cómo elegir en tres preguntas"),
        ],
        "faq": [
            ("¿Qué interfaz de audio necesito para un micrófono dinámico?",
             "Una con ganancia abundante y silenciosa. Los dinámicos tienen poca "
             "sensibilidad y pueden pedir entre 50 y 60 dB para voz hablada. Si la "
             "interfaz llega justa, oirás el siseo del preamplificador antes que tu voz."),
            ("¿Necesito interfaz si mi micrófono es USB?",
             "No. Un micrófono USB ya lleva dentro el preamplificador y el conversor, "
             "que es justo lo que hace una interfaz. Añadir una no mejora nada."),
            ("¿Qué es el monitoreo directo de una interfaz?",
             "Es una función que te devuelve a los auriculares la señal analógica del "
             "micrófono antes de que entre al ordenador, así te oyes sin el retardo que "
             "introduce el procesado. Es imprescindible para grabar hablando cómodo."),
        ],
        "body": """
<h2 id="que-hace">Qué hace realmente</h2>
<p>Una interfaz de audio hace tres cosas, y conviene separarlas porque cada una se
estropea de forma distinta:</p>
<ol>
<li><strong>Preamplifica.</strong> La señal de un micrófono es diminuta; hay que
amplificarla antes de digitalizarla.</li>
<li><strong>Convierte.</strong> Transforma esa señal analógica en datos.</li>
<li><strong>Alimenta.</strong> Entrega los 48 V de phantom que necesitan los
condensadores.</li>
</ol>
<div class="note">
<strong>Casi todos los problemas vienen del primer punto.</strong> Los conversores de
hoy, incluso baratos, son buenos. Los preamplificadores baratos, no tanto.
</div>

<h2 id="ganancia">Ganancia: el dato que importa</h2>
<table>
<thead><tr><th>Tu micrófono</th><th>Ganancia que pide</th><th>Qué buscar</th></tr></thead>
<tbody>
<tr><td>Condensador</td><td>Poca (30-40 dB)</td><td>Cualquier interfaz cumple</td></tr>
<tr><td>Dinámico normal</td><td>Media (45-55 dB)</td><td>Interfaz de gama media</td></tr>
<tr><td>Dinámico de difusión</td><td>Alta (55-65 dB)</td><td>Ganancia alta o preamplificador extra</td></tr>
</tbody></table>
<p>Y ojo: el número publicado no lo dice todo. Importa que esa ganancia sea
<strong>silenciosa</strong>. Una interfaz que da 60 dB con un siseo audible a 50 dB no
te sirve de nada.</p>

<h2 id="entradas">Cuántas entradas</h2>
<ul class="checks">
<li><strong>Una entrada:</strong> solo si estás absolutamente seguro de que nunca
grabarás a nadie contigo. Es la limitación que más gente lamenta.</li>
<li><strong>Dos entradas:</strong> el punto dulce. Cubre invitado presencial, un
instrumento o un segundo micrófono de respaldo.</li>
<li><strong>Cuatro o más:</strong> solo si haces mesa redonda de forma habitual.</li>
</ul>

<h2 id="ignorar">Especificaciones que puedes ignorar</h2>
<ul class="checks">
<li><strong>192 kHz.</strong> Para voz hablada no aporta nada audible y multiplica el
tamaño de los archivos. 48 kHz es de sobra.</li>
<li><strong>32 bits float</strong> en grabación de voz casera: útil en campo, irrelevante
sentado frente al micro con los niveles bien puestos.</li>
<li><strong>Rango dinámico de catálogo.</strong> Medido en condiciones que no son las
tuyas.</li>
<li><strong>Software incluido.</strong> Casi nunca se usa; no pagues por él.</li>
</ul>

<h2 id="elegir">Cómo elegir en tres preguntas</h2>
<ol>
<li><strong>¿Tu micro es dinámico de difusión?</strong> Entonces la ganancia manda sobre
todo lo demás.</li>
<li><strong>¿Vas a tener invitados en la misma sala?</strong> Dos entradas, no una.</li>
<li><strong>¿Vas a hablar con auriculares puestos?</strong> Comprueba que tenga monitoreo
directo y salida de auriculares con volumen propio.</li>
</ol>
<p>Si todo esto te suena a complicación innecesaria, quizá tu camino sea
<a href="../usb-o-xlr/">USB en lugar de XLR</a>.</p>
""",
    }

    PAGES["filtro-antipop/"] = {
        "title": "Filtro antipop: para qué sirve y dónde colocarlo",
        "desc": ("Filtro antipop: qué problema resuelve, diferencias entre nailon y "
                 "metal, a qué distancia ponerlo y cuándo no hace falta."),
        "h1": "Filtro antipop: ocho dólares que arreglan un problema real",
        "crumb": "Filtro antipop",
        "article": True, "kind": "Guía",
        "lede": ("No mejora tu voz ni quita ruido. Resuelve exactamente un problema, "
                 "y lo resuelve del todo: el golpe de aire de las consonantes "
                 "explosivas."),
        "toc": [
            ("problema", "Qué problema resuelve"),
            ("tipos", "Nailon o metal"),
            ("colocacion", "Dónde colocarlo"),
            ("alternativas", "Cuándo no hace falta"),
        ],
        "faq": [
            ("¿Para qué sirve un filtro antipop?",
             "Para frenar la ráfaga de aire que producen las consonantes explosivas, "
             "sobre todo la p y la b. Ese golpe de aire mueve el diafragma de golpe y "
             "genera un estallido grave que no se puede arreglar bien después."),
            ("¿Es mejor un antipop de nailon o de metal?",
             "El de nailon frena algo más el aire y suele costar menos, pero atenúa "
             "ligeramente los agudos y acumula humedad. El metálico desvía el aire hacia "
             "los lados, no toca el sonido y se limpia fácil, aunque es algo menos "
             "eficaz en voces muy explosivas."),
            ("¿A qué distancia se pone el filtro antipop?",
             "Aproximadamente a un palmo del micrófono, unos 8 a 10 cm, no pegado a la "
             "rejilla. Si lo pones tocando el micro, el aire rebota contra él y vuelve a "
             "la cápsula."),
        ],
        "body": """
<h2 id="problema">Qué problema resuelve</h2>
<p>Cuando pronuncias una «p», tus labios sueltan una ráfaga de aire. Esa ráfaga no es
sonido: es viento. Al llegar al diafragma lo empuja de golpe y produce un estallido
grave que satura la señal.</p>
<div class="note">
<strong>Es el único problema de audio que no tiene arreglo decente en la edición.</strong>
Un filtro paso alto reduce el estallido, pero se lleva por delante parte del cuerpo de
tu voz. Evitarlo al grabar cuesta ocho dólares.
</div>

<h2 id="tipos">Nailon o metal</h2>
<table>
<thead><tr><th></th><th>Nailon</th><th>Metal</th></tr></thead>
<tbody>
<tr><td>Cómo funciona</td><td>Frena el aire</td><td>Lo desvía lateralmente</td></tr>
<tr><td>Eficacia</td><td>Mayor</td><td>Alta</td></tr>
<tr><td>Efecto en agudos</td><td>Los atenúa un poco</td><td>Ninguno apreciable</td></tr>
<tr><td>Higiene</td><td>Acumula humedad</td><td>Se limpia fácil</td></tr>
<tr><td>Durabilidad</td><td>Se destensa</td><td>Muy alta</td></tr>
<tr><td>Precio</td><td>Menor</td><td>Algo mayor</td></tr>
</tbody></table>

<h2 id="colocacion">Dónde colocarlo</h2>
<ol>
<li><strong>A un palmo del micrófono</strong>, no pegado a la rejilla.</li>
<li><strong>Entre tu boca y la cápsula</strong>, cubriendo toda la zona de ataque.</li>
<li><strong>Con la pinza bien apretada</strong> al brazo: un antipop que se descuelga a
media grabación es un ruido más.</li>
<li><strong>Combínalo con hablar fuera de eje</strong>: apunta el micro a la comisura de
la boca y las explosivas pasan de largo.</li>
</ol>

<h2 id="alternativas">Cuándo no hace falta</h2>
<ul class="checks">
<li><strong>Micrófonos de difusión con antipop interno</strong> y voces poco explosivas:
puede bastar con el interno.</li>
<li><strong>Micrófonos de solapa:</strong> están fuera del chorro de aire.</li>
<li><strong>Grabaciones a más de 30 cm:</strong> el aire se disipa antes de llegar.</li>
</ul>
<p>Y una confusión frecuente: el <strong>paravientos de espuma</strong> no es lo mismo.
Ese sirve para viento de exterior, y para explosivas es bastante peor que un antipop.
Para exteriores, el peludo.</p>
<p>Monta el conjunto con criterio: <a href="../brazo-y-arana-antivibracion/">brazo y
araña</a>.</p>
""",
    }

    PAGES["microfono-de-solapa/"] = {
        "title": "Micrófono de solapa: cómo elegirlo y cómo colocarlo bien",
        "desc": ("Micrófono de solapa o lavalier: conectores, cableado, dónde "
                 "prenderlo para evitar el roce de la ropa y cuándo supera a un "
                 "micro de escritorio."),
        "h1": "Micrófono de solapa: discreto, barato y casi siempre mal colocado",
        "crumb": "Micrófono de solapa",
        "article": True, "kind": "Guía",
        "lede": ("Cuesta poco y está a 20 cm de tu boca, que es lo que de verdad "
                 "importa. El 90 % de los problemas que le achacan son de "
                 "colocación."),
        "toc": [
            ("cuando", "Cuándo gana a un micro de escritorio"),
            ("conectores", "El lío de los conectores"),
            ("colocacion", "Dónde prenderlo exactamente"),
            ("errores", "Errores que lo arruinan"),
        ],
        "faq": [
            ("¿Un micrófono de solapa suena mejor que uno de escritorio?",
             "Depende de la distancia. Un solapa a 20 cm de la boca deja entrar mucho "
             "menos ambiente que un micro de escritorio a 60 cm. Si el de escritorio "
             "está bien colocado y cerca, ese gana en calidad tonal."),
            ("¿Por qué se oye el roce de la ropa en mi micrófono de solapa?",
             "Porque la cápsula toca la tela o el cable se mueve contra ella. La "
             "solución es pasar el cable por dentro de la ropa, dejar un bucle de "
             "seguridad y fijar la pinza a una prenda que no se mueva con la "
             "respiración."),
            ("¿Qué conector necesita un micrófono de solapa para el móvil?",
             "Una clavija TRRS de cuatro contactos, o un adaptador de TRS a TRRS si el "
             "micro viene con conector de cámara. Con una TRS de tres contactos el "
             "teléfono no detecta el micrófono y sigue usando el interno."),
        ],
        "body": """
<h2 id="cuando">Cuándo gana a un micro de escritorio</h2>
<p>La regla que lo explica todo: <strong>gana cuando el micro de escritorio tendría que
estar lejos</strong>.</p>
<table>
<thead><tr><th>Situación</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Hablas a cámara de pie</td><td>Solapa</td><td>Está cerca y no sale en plano</td></tr>
<tr><td>Te mueves por la casa</td><td>Solapa inalámbrico</td><td>Mantiene la distancia</td></tr>
<tr><td>Sentado al escritorio</td><td>Micro de escritorio</td><td>Cápsula mayor, mejor tono</td></tr>
<tr><td>Entrevista a dos</td><td>Dos solapas</td><td>Cada voz en su pista</td></tr>
<tr><td>Voz en off en estudio</td><td>Micro de escritorio</td><td>Calidad por encima de todo</td></tr>
</tbody></table>

<h2 id="conectores">El lío de los conectores</h2>
<table>
<thead><tr><th>Conector</th><th>Para qué equipo</th><th>Aviso</th></tr></thead>
<tbody>
<tr><td>TRRS 3,5 mm</td><td>Móviles con jack</td><td>Cuatro contactos</td></tr>
<tr><td>TRS 3,5 mm</td><td>Cámaras y grabadoras</td><td>No funciona en móvil sin adaptador</td></tr>
<tr><td>USB-C</td><td>Móviles y ordenadores modernos</td><td>Ocupa el puerto de carga</td></tr>
<tr><td>Lightning</td><td>iPhone antiguos</td><td>Accesorios específicos</td></tr>
<tr><td>XLR con pila</td><td>Equipo profesional</td><td>Necesita phantom o batería</td></tr>
</tbody></table>
<div class="note">
<strong>El fallo número uno:</strong> comprar un solapa de cámara (TRS) para usarlo con
el móvil (TRRS). Entra físicamente, pero el teléfono no lo detecta.
</div>

<h2 id="colocacion">Dónde prenderlo exactamente</h2>
<ol>
<li><strong>En el centro del pecho</strong>, unos 20 cm bajo la barbilla. Ni en el cuello
ni a un lado.</li>
<li><strong>En una prenda firme</strong>: solapa de camisa o borde del jersey. Nunca en
algo que se mueva al respirar.</li>
<li><strong>Cable por dentro de la ropa</strong>, con un bucle de seguridad en la pinza
para que un tirón no arranque la cápsula.</li>
<li><strong>Cápsula sin tocar la tela.</strong> Si roza, suena como papel arrugado.</li>
<li><strong>Si giras mucho la cabeza</strong>, céntralo bien para que el volumen no suba
y baje.</li>
</ol>

<h2 id="errores">Errores que lo arruinan</h2>
<ul class="checks">
<li>Prenderlo sobre un collar o una cremallera que tintinea.</li>
<li>Olvidar el paravientos peludo en exteriores. Sin él, cualquier brisa lo tapa todo.</li>
<li>Usar un alargador barato que introduce zumbido.</li>
<li>No hacer una prueba de diez segundos antes de la toma buena.</li>
</ul>
<p>Para móvil, los detalles están en
<a href="../microfono-para-telefono/">micrófono para teléfono</a>. Para vídeo,
<a href="../microfono-para-youtube/">micrófono para YouTube</a>.</p>
""",
    }

    PAGES["microfono-inalambrico/"] = {
        "title": "Micrófono inalámbrico para vídeo: qué mirar y qué falla",
        "desc": ("Micrófonos inalámbricos de solapa para creadores: bandas de "
                 "frecuencia, autonomía, alcance real, grabación de respaldo y "
                 "errores que arruinan una toma."),
        "h1": "Micrófono inalámbrico: libertad de movimiento, con letra pequeña",
        "crumb": "Micrófono inalámbrico",
        "article": True, "kind": "Guía",
        "lede": ("Resuelve un problema real y crea otros tres. Merece la pena "
                 "saberlo antes, no en mitad de una grabación que no se puede "
                 "repetir."),
        "toc": [
            ("cuando", "Cuándo lo necesitas de verdad"),
            ("bandas", "2,4 GHz o UHF"),
            ("mirar", "Qué mirar antes de comprar"),
            ("fallos", "Lo que sale mal"),
        ],
        "faq": [
            ("¿Qué alcance real tiene un micrófono inalámbrico de 2,4 GHz?",
             "Los fabricantes suelen indicar alcances en línea de visión y sin "
             "interferencias. En interiores con paredes y wifi saturado, cuenta con "
             "bastante menos. Lo que importa no es el máximo, sino que la distancia a la "
             "que vas a trabajar quede holgada."),
            ("¿Un micrófono inalámbrico graba por sí solo?",
             "Algunos transmisores incorporan grabación interna, y es la función más "
             "valiosa del producto: si la transmisión se corta, tienes el audio limpio "
             "guardado en el propio transmisor."),
            ("¿Por qué se corta mi micrófono inalámbrico?",
             "Las causas más comunes son interferencia en la banda de 2,4 GHz "
             "compartida con el wifi, el cuerpo de la persona bloqueando la señal, o "
             "distancia excesiva. Mover el receptor a línea de visión directa resuelve "
             "la mayoría de casos."),
        ],
        "body": """
<h2 id="cuando">Cuándo lo necesitas de verdad</h2>
<ul class="checks">
<li><strong>Te mueves mientras hablas:</strong> cocina, taller, calle, gimnasio.</li>
<li><strong>Grabas a otra persona</strong> y el cable sería un estorbo visible.</li>
<li><strong>La cámara está lejos</strong> del sujeto.</li>
</ul>
<p>Y cuándo no: si grabas sentado frente a un escritorio, un cable es más fiable, suena
igual o mejor y cuesta mucho menos. El inalámbrico no mejora el sonido; solo quita el
cable.</p>

<h2 id="bandas">2,4 GHz o UHF</h2>
<table>
<thead><tr><th></th><th>2,4 GHz</th><th>UHF</th></tr></thead>
<tbody>
<tr><td>Uso típico</td><td>Creadores, vídeo</td><td>Escenario, producción</td></tr>
<tr><td>Licencia</td><td>No necesita</td><td>Según país y banda</td></tr>
<tr><td>Interferencia</td><td>Comparte con wifi</td><td>Menor, si eliges bien</td></tr>
<tr><td>Tamaño</td><td>Muy compacto</td><td>Mayor</td></tr>
<tr><td>Canales simultáneos</td><td>Pocos</td><td>Muchos</td></tr>
<tr><td>Precio</td><td>Accesible</td><td>Alto</td></tr>
</tbody></table>
<div class="note">
<strong>Para un creador en solitario, 2,4 GHz es la respuesta.</strong> UHF tiene sentido
cuando necesitas varios canales a la vez o trabajas en entornos con mucha radio.
</div>

<h2 id="mirar">Qué mirar antes de comprar</h2>
<ol>
<li><strong>Grabación interna en el transmisor.</strong> Es tu seguro ante cortes. Si un
modelo la tiene y otro no, esa es la diferencia que importa.</li>
<li><strong>Autonomía real</strong>, no la del catálogo. Y si el estuche recarga.</li>
<li><strong>Salida del receptor:</strong> jack de cámara, USB-C o Lightning. Comprueba
que encaja con lo que ya tienes.</li>
<li><strong>Paravientos peludo incluido.</strong> En exteriores no es opcional.</li>
<li><strong>Control de ganancia en el receptor</strong>, para no depender del automático
de la cámara.</li>
</ol>

<h2 id="fallos">Lo que sale mal</h2>
<table>
<thead><tr><th>Síntoma</th><th>Causa habitual</th><th>Arreglo</th></tr></thead>
<tbody>
<tr><td>Cortes intermitentes</td><td>Wifi saturado o cuerpo bloqueando</td><td>Receptor en línea de visión</td></tr>
<tr><td>Audio saturado</td><td>Ganancia del transmisor alta</td><td>Bajar nivel en el receptor</td></tr>
<tr><td>Se apaga a mitad</td><td>Batería real menor que la anunciada</td><td>Cargar entre tomas</td></tr>
<tr><td>Ruido de roce</td><td>Pinza sobre tela que se mueve</td><td>Recolocar y fijar cable</td></tr>
<tr><td>Viento constante</td><td>Sin peludo</td><td>Ponerlo siempre en exterior</td></tr>
</tbody></table>
<p>Para colocarlo bien, lee <a href="../microfono-de-solapa/">micrófono de solapa</a>.</p>
""",
    }

    PAGES["microfono-para-gaming/"] = {
        "title": "Micrófono para gaming: que no se oiga tu teclado",
        "desc": ("Micrófono para gaming y Discord: por qué el teclado mecánico se "
                 "cuela, qué tipo de micro lo evita y cómo configurarlo sin cortar "
                 "la voz."),
        "h1": "Micrófono para gaming: el enemigo es tu propio teclado",
        "crumb": "Micrófono para gaming",
        "article": True, "kind": "Guía",
        "lede": ("Un jugador tiene un problema que un locutor no tiene: a medio metro "
                 "de su boca hay un teclado mecánico y un ventilador a plena carga."),
        "toc": [
            ("problema", "Tu situación es distinta"),
            ("tipo", "Qué tipo de micro elegir"),
            ("auriculares", "¿Y el micro de los auriculares?"),
            ("ajustes", "Ajustes para Discord y juego"),
        ],
        "faq": [
            ("¿Qué micrófono es mejor para gaming?",
             "Un dinámico cardioide sobre brazo, acercado a la boca. Al ser poco "
             "sensible y rechazar por detrás, deja fuera el teclado y los ventiladores, "
             "que es exactamente el problema de un setup de juego."),
            ("¿Se nota mucho el teclado mecánico en el micrófono?",
             "Mucho, sobre todo si el micrófono está apoyado en la misma mesa: el golpe "
             "viaja por la madera hasta la cápsula. Un brazo con araña elimina esa vía, "
             "y acercarse al micro reduce lo que entra por el aire."),
            ("¿El micrófono de los auriculares gaming es suficiente?",
             "Para jugar y coordinarte, sí. Para transmitir o grabar, no: la cápsula es "
             "diminuta, está en un brazo de plástico y suele aplicar procesado agresivo "
             "que adelgaza la voz."),
        ],
        "body": """
<h2 id="problema">Tu situación es distinta</h2>
<p>Las guías genéricas de micrófonos asumen un cuarto tranquilo y alguien quieto. Un
jugador tiene lo contrario:</p>
<ul class="checks">
<li>Un <strong>teclado mecánico</strong> a 40 cm de la boca.</li>
<li>Un <strong>equipo con ventiladores</strong> que suben de revoluciones en lo mejor de
la partida.</li>
<li><strong>Movimiento</strong>: te echas atrás, te acercas, gesticulas.</li>
<li>A veces <strong>gritos</strong>, que saturan cualquier ajuste cómodo.</li>
</ul>
<div class="note">
<strong>Conclusión directa:</strong> esto descarta los condensadores sensibles y señala a
un dinámico cercano. No es cuestión de presupuesto, es de contexto.
</div>

<h2 id="tipo">Qué tipo de micro elegir</h2>
<table>
<thead><tr><th>Opción</th><th>Teclado que deja pasar</th><th>Veredicto</th></tr></thead>
<tbody>
<tr><td>Dinámico en brazo, a 8 cm</td><td>Muy poco</td><td>La mejor opción</td></tr>
<tr><td>Condensador USB en brazo</td><td>Bastante</td><td>Solo si tecleas poco</td></tr>
<tr><td>Condensador en base de mesa</td><td>Mucho</td><td>Evitar</td></tr>
<tr><td>Micro de auriculares</td><td>Poco</td><td>Vale para jugar, no para emitir</td></tr>
<tr><td>Micro de la webcam</td><td>Todo</td><td>Evitar</td></tr>
</tbody></table>

<h2 id="auriculares">¿Y el micro de los auriculares?</h2>
<p>Tiene una ventaja objetiva que conviene reconocer: está pegado a tu boca, así que la
relación entre tu voz y el cuarto es buena. Por eso en una partida se te entiende bien.</p>
<p>Lo que no tiene es cápsula decente ni electrónica cuidada, y casi siempre lleva
procesado de supresión de ruido que deja la voz metálica. Para hablar con amigos, de
sobra. Para que te escuche una audiencia, no.</p>

<h2 id="ajustes">Ajustes para Discord y juego</h2>
<ol>
<li><strong>Desactiva la supresión de ruido de la aplicación</strong> si ya usas un
dinámico bien colocado: hace más daño que bien.</li>
<li><strong>Puerta de ruido suave</strong>, con 10 dB entre apertura y cierre, para que
no te corte el final de las frases.</li>
<li><strong>Compresor suave</strong>, que iguala el susurro y el grito.</li>
<li><strong>Limitador al final</strong>, tu red de seguridad cuando gritas.</li>
<li><strong>Brazo con araña</strong>, para que los golpes de mesa no viajen.</li>
<li><strong>Gira el micro</strong> de modo que su parte trasera apunte al ordenador.</li>
</ol>
<p>Los valores concretos están en
<a href="../configurar-microfono-obs/">configurar el micrófono en OBS</a>. Para elegir
modelo, <a href="../mejores-micros-streaming/">comparativa por presupuesto</a>.</p>
""",
    }

    PAGES["microfono-para-cantar/"] = {
        "title": "Micrófono para cantar en casa: qué necesitas de verdad",
        "desc": ("Micrófono para cantar en casa: condensador o dinámico, por qué el "
                 "cuarto importa más que el micro y qué cadena mínima necesitas."),
        "h1": "Micrófono para cantar en casa: el cuarto pesa más que el micro",
        "crumb": "Micrófono para cantar",
        "article": True, "kind": "Guía",
        "lede": ("Cantar expone el cuarto mucho más que hablar: más rango dinámico, "
                 "más agudos y más cola de reverberación. Ahí es donde se decide el "
                 "resultado."),
        "toc": [
            ("diferencia", "Por qué cantar es distinto"),
            ("tipo", "Condensador o dinámico"),
            ("cadena", "La cadena mínima"),
            ("cuarto", "Qué hacer con el cuarto"),
        ],
        "faq": [
            ("¿Qué micrófono es mejor para cantar en casa?",
             "En una habitación tratada, un condensador de diafragma grande, porque "
             "captura el detalle y el aire de la voz. En una habitación sin tratar, un "
             "dinámico de calidad da un resultado final más limpio aunque sobre el papel "
             "sea un micrófono menos capaz."),
            ("¿Necesito interfaz para cantar en casa?",
             "Si eliges un micrófono XLR, sí, y además con phantom de 48 V si es "
             "condensador. También necesitarás auriculares cerrados para escuchar la base "
             "sin que se cuele por el micrófono."),
            ("¿Por qué mi voz grabada suena con eco en casa?",
             "Porque el micrófono está captando los rebotes de las paredes además de tu "
             "voz. Cantar proyecta más energía que hablar, así que excita más la "
             "reverberación de la sala. Se corrige con absorción, no con ajustes."),
        ],
        "body": """
<h2 id="diferencia">Por qué cantar es distinto</h2>
<table>
<thead><tr><th></th><th>Hablar</th><th>Cantar</th></tr></thead>
<tbody>
<tr><td>Rango dinámico</td><td>Moderado</td><td>Muy amplio</td></tr>
<tr><td>Energía que proyectas</td><td>Baja</td><td>Alta</td></tr>
<tr><td>Agudos</td><td>Contenidos</td><td>Extendidos</td></tr>
<tr><td>Distancia típica</td><td>5-15 cm</td><td>15-30 cm</td></tr>
<tr><td>Cuánto delata el cuarto</td><td>Algo</td><td>Mucho</td></tr>
</tbody></table>
<div class="note">
<strong>Al alejarte para cantar, metes más cuarto en la grabación.</strong> Por eso una
sala que vale para un podcast puede no valer para una voz cantada.
</div>

<h2 id="tipo">Condensador o dinámico</h2>
<ul class="checks">
<li><strong>Cuarto tratado:</strong> condensador de diafragma grande, cardioide. Detalle
y aire.</li>
<li><strong>Cuarto normal:</strong> dinámico de calidad. Perderás algo de brillo y
ganarás una grabación sin cola de reverberación.</li>
<li><strong>Voz muy potente:</strong> dinámico, o condensador con atenuación.</li>
<li><strong>Voz muy sibilante:</strong> cualquiera de los dos más un de-esser suave.</li>
</ul>
<p>Más detalle en <a href="../dinamico-vs-condensador/">dinámico vs condensador</a>.</p>

<h2 id="cadena">La cadena mínima</h2>
<ol>
<li><strong>Micrófono</strong> acorde con tu cuarto.</li>
<li><strong>Interfaz con phantom</strong> si vas a condensador.</li>
<li><strong>Auriculares cerrados.</strong> Innegociable: con altavoces, la base se cuela
en la toma.</li>
<li><strong>Filtro antipop</strong> y pie o brazo estable.</li>
<li><strong>Monitoreo directo</strong> para cantar sin retardo.</li>
</ol>

<h2 id="cuarto">Qué hacer con el cuarto</h2>
<p>Por orden de rentabilidad, y sin comprar paneles caros:</p>
<ul class="checks">
<li><strong>Canta hacia la parte más absorbente de la habitación</strong>, no hacia una
pared desnuda.</li>
<li><strong>Cuelga una manta gruesa</strong> en la pared que tienes delante.</li>
<li><strong>Evita el centro del cuarto</strong> y las esquinas.</li>
<li><strong>Alfombra</strong> si el suelo es duro.</li>
<li><strong>Un armario con ropa</strong> es el mejor estudio gratuito que existe.</li>
</ul>
<p>Desarrollado en <a href="../tratamiento-acustico-casero/">tratamiento acústico
casero</a>.</p>
""",
    }

    PAGES["microfono-para-videollamadas/"] = {
        "title": "Micrófono para videollamadas y reuniones: qué cambia de verdad",
        "desc": ("Micrófono para Zoom, Meet y Teams: por qué suenas mal, qué opción "
                 "elegir según tu puesto y los ajustes que estropean la voz."),
        "h1": "Micrófono para videollamadas: se te entiende o no se te entiende",
        "crumb": "Micrófono para videollamadas",
        "article": True, "kind": "Guía",
        "lede": ("En una reunión nadie valora tu timbre: valoran si tienen que pedirte "
                 "que repitas. El objetivo aquí no es belleza, es inteligibilidad."),
        "toc": [
            ("objetivo", "El objetivo es otro"),
            ("opciones", "Las cuatro opciones"),
            ("ajustes", "Ajustes que te sabotean"),
            ("checklist", "Checklist de dos minutos"),
        ],
        "faq": [
            ("¿Qué micrófono es mejor para videollamadas?",
             "Para la mayoría de puestos de escritorio, unos auriculares con micrófono "
             "de brazo resuelven el 90 % del problema: el micro queda cerca de la boca y "
             "los auriculares evitan el eco. Un micro de escritorio dedicado suena mejor, "
             "pero aporta menos de lo que la gente espera en una llamada comprimida."),
            ("¿Por qué se oye eco en mis videollamadas?",
             "Porque usas altavoces en lugar de auriculares: tu micrófono vuelve a captar "
             "la voz de la otra persona y se la devuelve. La cancelación de eco ayuda, "
             "pero no sustituye a ponerse auriculares."),
            ("¿Debo activar la supresión de ruido de Zoom o Teams?",
             "En un entorno ruidoso, sí. En uno tranquilo conviene bajarla o desactivarla: "
             "adelgaza la voz, se come las respiraciones y puede cortar el inicio de las "
             "frases."),
        ],
        "body": """
<h2 id="objetivo">El objetivo es otro</h2>
<p>Una videollamada comprime el audio de forma agresiva y lo recorta a la banda de la
voz. Da igual lo buena que sea tu cápsula: al otro lado llega una versión reducida.</p>
<div class="note">
<strong>Lo que sí llega:</strong> si estás lejos del micro, si hay eco de sala y si el
ruido de fondo compite con tu voz. Esas tres cosas sobreviven a la compresión.
</div>

<h2 id="opciones">Las cuatro opciones</h2>
<table>
<thead><tr><th>Opción</th><th>Calidad</th><th>Comodidad</th><th>Para quién</th></tr></thead>
<tbody>
<tr><td>Micro del portátil</td><td>Baja</td><td>Máxima</td><td>Llamadas puntuales</td></tr>
<tr><td>Auriculares con micro de brazo</td><td>Buena</td><td>Alta</td><td>La mayoría</td></tr>
<tr><td>Solapa con cable</td><td>Buena</td><td>Media</td><td>Si sales en cámara sin cascos</td></tr>
<tr><td>Micro de escritorio</td><td>Muy buena</td><td>Media</td><td>Quien además graba o emite</td></tr>
</tbody></table>
<p>La fila que resuelve más casos es la segunda. No es glamurosa, pero pone la cápsula a
tres centímetros de tu boca y elimina el eco de un plumazo.</p>

<h2 id="ajustes">Ajustes que te sabotean</h2>
<ul class="checks">
<li><strong>Supresión de ruido al máximo</strong> en un cuarto tranquilo: te corta
sílabas.</li>
<li><strong>Ajuste automático de volumen</strong>: sube el ruido cuando callas.</li>
<li><strong>Altavoces en lugar de auriculares</strong>: la causa número uno del eco.</li>
<li><strong>Dispositivo «predeterminado»</strong>: cambia solo cuando conectas algo.
Elige tu micro por su nombre.</li>
<li><strong>Micrófono de la webcam</strong> estando a un metro: capta toda la sala.</li>
</ul>

<h2 id="checklist">Checklist de dos minutos</h2>
<ol>
<li>Selecciona tu micrófono <strong>por nombre</strong> en la aplicación.</li>
<li>Haz una <strong>grabación de prueba</strong> de diez segundos y escúchala.</li>
<li>Ponte <strong>auriculares</strong>.</li>
<li><strong>Acércate</strong>: 20 cm es mejor que 60.</li>
<li>Silencia el <strong>móvil</strong> y cierra la ventana.</li>
<li>Si vas a hablar mucho rato, <strong>silencia cuando no hables</strong>.</li>
</ol>
<p>Si además grabas contenido, mira
<a href="../mejores-micros-streaming/">la comparativa por presupuesto</a>.</p>
""",
    }

    PAGES["microfono-para-voz-en-off/"] = {
        "title": "Micrófono para voz en off: qué pide este trabajo en concreto",
        "desc": ("Micrófono para voz en off y locución: por qué aquí sí manda el "
                 "condensador, qué silencio necesitas y cómo preparar una cabina "
                 "casera."),
        "h1": "Micrófono para voz en off: el único caso donde el detalle manda",
        "crumb": "Voz en off",
        "article": True, "kind": "Guía",
        "lede": ("A diferencia del directo, aquí puedes controlar el entorno, repetir "
                 "la toma y editar. Eso cambia por completo qué micrófono conviene."),
        "toc": [
            ("distinto", "Por qué aquí sí cambia"),
            ("silencio", "El listón del silencio"),
            ("cabina", "Cabina casera que sí funciona"),
            ("tecnica", "Técnica de locución"),
        ],
        "faq": [
            ("¿Qué micrófono se usa para voz en off?",
             "Habitualmente un condensador de diafragma grande con patrón cardioide, "
             "porque aporta detalle y cuerpo. Es el escenario donde ese tipo de "
             "micrófono rinde mejor, siempre que el espacio de grabación sea silencioso."),
            ("¿Cuánto silencio necesita una grabación de voz en off?",
             "El suficiente para que, al subir el volumen de un silencio de la toma, no "
             "aparezca un ruido audible. En la práctica significa apagar aire, nevera y "
             "ventiladores, y grabar en horas tranquilas."),
            ("¿Sirve un armario como cabina de voz?",
             "Sí, y es de las mejores soluciones gratuitas. La ropa colgada absorbe "
             "reflexiones en un volumen pequeño, que es justo lo que necesita una toma de "
             "voz. Deja espacio detrás del micrófono y evita que la ropa lo roce."),
        ],
        "body": """
<h2 id="distinto">Por qué aquí sí cambia</h2>
<table>
<thead><tr><th></th><th>Directo</th><th>Voz en off</th></tr></thead>
<tbody>
<tr><td>Puedes repetir</td><td>No</td><td>Sí</td></tr>
<tr><td>Controlas el entorno</td><td>A medias</td><td>Totalmente</td></tr>
<tr><td>Hay edición posterior</td><td>Mínima</td><td>Completa</td></tr>
<tr><td>Ruido admisible</td><td>Algo</td><td>Casi ninguno</td></tr>
<tr><td>Micrófono recomendado</td><td>Dinámico</td><td>Condensador</td></tr>
</tbody></table>
<p>Es el único caso del sitio donde recomendamos condensador sin matices, y es porque
puedes cumplir su condición: silencio.</p>

<h2 id="silencio">El listón del silencio</h2>
<p>La prueba es simple. Graba treinta segundos sin hablar, sube ese fragmento de volumen
y escúchalo con auriculares. Lo que oigas, estará en todas tus tomas.</p>
<ul class="checks">
<li>Apaga aire acondicionado y calefacción durante la sesión.</li>
<li>Desenchufa o aleja la torre del ordenador.</li>
<li>Elige la franja horaria más tranquila del día.</li>
<li>Silencia el móvil del todo, también la vibración.</li>
<li>Avisa en casa de que estás grabando.</li>
</ul>

<h2 id="cabina">Cabina casera que sí funciona</h2>
<ol>
<li><strong>Un armario con ropa colgada</strong> es la mejor opción gratuita: volumen
pequeño y absorción por todos lados.</li>
<li><strong>Deja espacio detrás del micrófono</strong>, no lo pegues a la ropa.</li>
<li><strong>Si no tienes armario</strong>, cuelga una manta gruesa delante y otra detrás
de ti.</li>
<li><strong>Evita cabinas improvisadas con superficies duras</strong>: una caja de cartón
rígida crea resonancias peores que el cuarto.</li>
<li><strong>Prueba y escucha.</strong> Cada espacio reacciona distinto.</li>
</ol>
<div class="note">
<strong>Lo que no funciona:</strong> los reflectores pequeños que se montan detrás del
micrófono ayudan algo con las reflexiones traseras, pero no con el ruido aéreo ni con el
eco general de la sala.
</div>

<h2 id="tecnica">Técnica de locución</h2>
<ul class="checks">
<li><strong>Distancia constante.</strong> Marca en el suelo o el brazo dónde va tu
cabeza.</li>
<li><strong>Fuera de eje</strong>, apuntando a la comisura.</li>
<li><strong>Agua a temperatura ambiente</strong> cerca; evita lácteos antes de grabar.</li>
<li><strong>Si te equivocas, no pares:</strong> haz una pausa, repite la frase entera y
marca el error con una palmada.</li>
<li><strong>Graba una toma de ambiente</strong> de treinta segundos al final: sirve para
rellenar silencios en la edición.</li>
</ul>
<p>Para la cadena de proceso, <a href="../ecualizar-la-voz/">cómo ecualizar la voz</a> y
<a href="../compresor-de-voz/">el compresor</a>.</p>
""",
    }
