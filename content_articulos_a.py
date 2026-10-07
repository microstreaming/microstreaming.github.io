# -*- coding: utf-8 -*-
"""Bloque A: fichas de modelo y equipo de apoyo.

Paginas de intencion comercial. Son las que recibiran enlaces de afiliado
cuando el sitio tenga posicionamiento, asi que llevan siempre una seccion
de precio y una de "para quien NO es".
"""


def add_pages(PAGES, SITE):

    PAGES["shure-sm58/"] = {
        "title": "Shure SM58 para streaming y podcast: ¿sigue mereciendo la pena?",
        "desc": ("Shure SM58 en 2026: por qué el micrófono de directo más vendido "
                 "funciona para podcast y streaming, qué ganancia pide y cuándo no "
                 "es la compra correcta."),
        "h1": "Shure SM58: el micrófono que lleva cincuenta años sin cambiar",
        "crumb": "Shure SM58",
        "article": True, "kind": "Ficha",
        "lede": ("Es el dinámico más vendido de la historia y no por moda: rechaza "
                 "el cuarto, aguanta lo que le eches y suena igual el primer día "
                 "que el año quince."),
        "toc": [
            ("que-es", "Qué es"),
            ("streaming", "Para streaming y podcast"),
            ("ganancia", "El problema de la ganancia"),
            ("precio", "Precio y coste real"),
            ("no-es", "Para quién NO es"),
        ],
        "faq": [
            ("¿El Shure SM58 sirve para grabar podcast?",
             "Sí. Es un dinámico cardioide pensado para voz, así que rechaza muy bien "
             "el ambiente de una habitación sin tratar. Su limitación no es el sonido, "
             "sino que pide bastante ganancia limpia: con una interfaz de entrada muy "
             "básica puede quedarse corto de volumen."),
            ("¿Qué diferencia hay entre el SM58 y el SM57?",
             "La cápsula es prácticamente la misma. El SM58 lleva una rejilla esférica "
             "con filtro antiviento integrado, pensada para voz de cerca; el SM57 tiene "
             "la cápsula más expuesta, pensada para instrumentos y amplificadores."),
            ("¿El SM58 necesita alimentación phantom?",
             "No. Es dinámico y genera su propia señal. El phantom no le aporta nada, "
             "aunque dejarlo encendido no lo daña si el cable XLR está en buen estado."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>Shure SM58</strong> es un micrófono dinámico cardioide de mano, diseñado
para voz en directo. Lleva décadas siendo el estándar de los escenarios, y eso explica
tanto sus virtudes como sus límites.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Dinámico</td></tr>
<tr><td>Patrón polar</td><td>Cardioide</td></tr>
<tr><td>Conexión</td><td>XLR</td></tr>
<tr><td>Alimentación</td><td>No necesita</td></tr>
<tr><td>Filtro antiviento</td><td>Integrado en la rejilla</td></tr>
<tr><td>Rango orientativo</td><td>100-130 USD</td></tr>
</tbody></table>

<h2 id="streaming">Para streaming y podcast</h2>
<p>Funciona, y bien. Al ser dinámico y cardioide deja fuera buena parte del cuarto, que
es exactamente el problema de la mayoría de la gente que graba en casa. Su respuesta
está pensada para la voz: recorta graves por debajo de la voz y realza ligeramente la
zona de presencia, lo que ayuda a entender las palabras.</p>
<ul class="checks">
<li><strong>Distancia:</strong> de 2 a 8 cm. Es un micrófono de hablar cerca.</li>
<li><strong>Ángulo:</strong> ligeramente fuera de eje para evitar explosivas.</li>
<li><strong>Soporte:</strong> en brazo con araña, nunca en la mano si vas a grabar
largo.</li>
</ul>
<div class="note">
<strong>Su rejilla esférica engaña:</strong> parece que puedes hablarle de lejos porque
es grande. No. Sigue siendo un dinámico y necesita cercanía.
</div>

<h2 id="ganancia">El problema de la ganancia</h2>
<p>Es el punto que casi nadie menciona al recomendarlo. El SM58 tiene una sensibilidad
baja, así que pide mucha ganancia. Con una interfaz de gama de entrada puedes acabar con
el mando al tope y un siseo audible de fondo.</p>
<p>Soluciones, de menor a mayor coste:</p>
<ol>
<li><strong>Acércate más.</strong> Gratis y sorprendentemente eficaz.</li>
<li><strong>Una interfaz con preamplificadores más silenciosos.</strong></li>
<li><strong>Un preamplificador en línea</strong> intercalado, que suma unos 25 dB
limpios.</li>
</ol>

<h2 id="precio">Precio y coste real</h2>
<table>
<thead><tr><th>Concepto</th><th>¿Obligatorio?</th><th>Rango</th></tr></thead>
<tbody>
<tr><td>Shure SM58</td><td>Sí</td><td>100-130 USD</td></tr>
<tr><td>Interfaz con buena ganancia</td><td>Sí</td><td>120-200 USD</td></tr>
<tr><td>Cable XLR</td><td>Sí</td><td>10-25 USD</td></tr>
<tr><td>Brazo y araña</td><td>Muy recomendable</td><td>40-95 USD</td></tr>
<tr><td>Preamplificador en línea</td><td>Según interfaz</td><td>70-150 USD</td></tr>
</tbody></table>

<h2 id="no-es">Para quién NO es</h2>
<ul class="checks">
<li><strong>Si no quieres interfaz.</strong> Es XLR puro; mira
<a href="../usb-o-xlr/">la ruta USB</a>.</li>
<li><strong>Si tu cuarto ya está tratado</strong> y buscas detalle: ahí rinde más un
<a href="../microfono-condensador/">condensador</a>.</li>
<li><strong>Si tiendes a alejarte del micro</strong> mientras hablas.</li>
<li><strong>Si tu interfaz es de las más básicas</strong> y no piensas cambiarla.</li>
</ul>
<p>Comparado con otros dinámicos: <a href="../mejores-micros-streaming/">guía por
presupuesto</a>. Y si dudas del tipo de cápsula,
<a href="../dinamico-vs-condensador/">dinámico vs condensador</a>.</p>
""",
    }

    PAGES["shure-sm7b/"] = {
        "title": "Shure SM7B: por qué cuesta tanto y qué necesitas además",
        "desc": ("Shure SM7B: el dinámico de difusión más conocido. Qué lo justifica, "
                 "cuánta ganancia pide de verdad y el coste real del conjunto."),
        "h1": "Shure SM7B: el micrófono que casi nadie monta bien",
        "crumb": "Shure SM7B",
        "article": True, "kind": "Ficha",
        "lede": ("Es el dinámico de difusión más visto en estudios y en directos "
                 "grandes. También el que más gente compra sin presupuestar lo que "
                 "hace falta para que funcione."),
        "toc": [
            ("que-es", "Qué es"),
            ("por-que", "Por qué suena así"),
            ("ganancia", "La ganancia: el aviso importante"),
            ("precio", "El coste real del conjunto"),
            ("no-es", "Para quién NO es"),
        ],
        "faq": [
            ("¿El Shure SM7B necesita un preamplificador?",
             "Con la mayoría de interfaces de gama media o baja, sí. Es un dinámico de "
             "sensibilidad muy baja y puede pedir unos 60 dB de ganancia limpia para "
             "voz hablada normal. Si tu interfaz no los da sin ruido, necesitarás un "
             "preamplificador en línea o una interfaz con más margen."),
            ("¿El SM7B necesita phantom de 48 V?",
             "No para funcionar: es dinámico. Lo que sí puede necesitar phantom es el "
             "preamplificador en línea que muchos usuarios añaden, porque ese accesorio "
             "se alimenta precisamente de los 48 V."),
            ("¿Merece la pena el SM7B para empezar?",
             "Como primer micrófono rara vez. El micro es solo parte del gasto y su "
             "ventaja principal —rechazar un cuarto imperfecto y aguantar voces "
             "fuertes— la dan también dinámicos de un tercio de precio."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>Shure SM7B</strong> es un micrófono dinámico cardioide de difusión, con
blindaje contra zumbidos eléctricos, suspensión interna y filtros de respuesta
conmutables. Está pensado para locución a corta distancia en entornos reales.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Dinámico de difusión</td></tr>
<tr><td>Patrón polar</td><td>Cardioide</td></tr>
<tr><td>Conexión</td><td>XLR</td></tr>
<tr><td>Controles</td><td>Corte de graves y realce de presencia</td></tr>
<tr><td>Suspensión</td><td>Interna, integrada</td></tr>
<tr><td>Rango orientativo</td><td>370-450 USD</td></tr>
</tbody></table>

<h2 id="por-que">Por qué suena así</h2>
<p>Tres decisiones de diseño explican su reputación:</p>
<ul class="checks">
<li><strong>Blindaje electromagnético.</strong> No capta el zumbido de pantallas ni de
fuentes de alimentación cercanas, que es el ruido típico de un escritorio lleno de
aparatos.</li>
<li><strong>Suspensión interna.</strong> Aísla golpes sin depender de una araña externa.</li>
<li><strong>Rechazo trasero muy limpio.</strong> Lo que queda detrás del micro
prácticamente no entra, y eso perdona habitaciones malas.</li>
</ul>

<h2 id="ganancia">La ganancia: el aviso importante</h2>
<div class="note">
<strong>Este es el dato que decide tu compra.</strong> El SM7B pide alrededor de 60 dB
de ganancia limpia para voz hablada. Muchas interfaces de gama media llegan justas.
</div>
<p>Si tu interfaz no da ese margen, lo que oirás no es un micro malo: es el ruido del
preamplificador de tu interfaz amplificado. La solución es un preamplificador en línea
—un cilindro que se intercala en el cable XLR y aporta ganancia limpia— o una interfaz
con preamplificadores de más nivel.</p>

<h2 id="precio">El coste real del conjunto</h2>
<table>
<thead><tr><th>Concepto</th><th>¿Obligatorio?</th><th>Rango</th></tr></thead>
<tbody>
<tr><td>Shure SM7B</td><td>Sí</td><td>370-450 USD</td></tr>
<tr><td>Interfaz con ganancia alta</td><td>Sí</td><td>150-350 USD</td></tr>
<tr><td>Preamplificador en línea</td><td>Según interfaz</td><td>70-150 USD</td></tr>
<tr><td>Brazo resistente</td><td>Sí, pesa</td><td>60-130 USD</td></tr>
<tr><td>Cable XLR</td><td>Sí</td><td>10-25 USD</td></tr>
</tbody></table>
<p>El micrófono suele ser menos de la mitad del gasto total. Quien no cuenta con eso
acaba con un SM7B sonando peor que un dinámico de 90 dólares.</p>

<h2 id="no-es">Para quién NO es</h2>
<ul class="checks">
<li><strong>Primer micrófono.</strong> El salto de calidad respecto a un dinámico bueno
es pequeño comparado con el salto de precio.</li>
<li><strong>Si tu interfaz es básica</strong> y no piensas añadir preamplificador.</li>
<li><strong>Si grabas lejos del micro.</strong> Es de hablar pegado.</li>
<li><strong>Si tu cuarto ya está tratado</strong> y quieres máximo detalle: un
condensador te dará más.</li>
</ul>
<p>Alternativas razonables en <a href="../mejores-micros-streaming/">la comparativa por
presupuesto</a>.</p>
""",
    }

    PAGES["rode-podmic/"] = {
        "title": "Rode PodMic: análisis para podcast y streaming",
        "desc": ("Rode PodMic: dinámico de difusión con suspensión interna y filtro "
                 "antipop integrado. Qué ofrece frente a alternativas más caras."),
        "h1": "Rode PodMic: el atajo sensato al sonido de radio",
        "crumb": "Rode PodMic",
        "article": True, "kind": "Ficha",
        "lede": ("Un dinámico de difusión que llega casi donde llegan los caros, por "
                 "bastante menos, y que pide menos ganancia que ellos."),
        "toc": [
            ("que-es", "Qué es"),
            ("fuerte", "Lo que hace bien"),
            ("pegas", "Las pegas"),
            ("precio", "Precio y coste real"),
            ("no-es", "Para quién NO es"),
        ],
        "faq": [
            ("¿El Rode PodMic necesita interfaz de audio?",
             "Sí. La versión clásica es XLR pura, así que necesita una interfaz o "
             "mezclador. No requiere alimentación phantom porque es dinámico, pero sí "
             "una entrada con ganancia suficiente."),
            ("¿El PodMic lleva filtro antipop integrado?",
             "Lleva un filtro interno que reduce bastante las explosivas, pero en voces "
             "muy cercanas o con mucha 'p' sigue siendo recomendable un antipop externo."),
            ("¿Es mejor el PodMic o un condensador del mismo precio?",
             "Para una habitación sin tratar, el PodMic casi siempre da mejor resultado "
             "final: deja fuera el eco y el ruido que el condensador amplificaría. En "
             "una sala tratada, el condensador aporta más detalle."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>Rode PodMic</strong> es un dinámico cardioide de difusión, pensado
específicamente para podcast y locución. Lleva suspensión interna, filtro antipop
integrado y un cuerpo metálico pesado.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Dinámico de difusión</td></tr>
<tr><td>Patrón polar</td><td>Cardioide</td></tr>
<tr><td>Conexión</td><td>XLR</td></tr>
<tr><td>Antipop</td><td>Interno</td></tr>
<tr><td>Montaje</td><td>Yugo integrado, rosca estándar</td></tr>
<tr><td>Rango orientativo</td><td>99-150 USD</td></tr>
</tbody></table>

<h2 id="fuerte">Lo que hace bien</h2>
<ul class="checks">
<li><strong>Pide menos ganancia</strong> que otros dinámicos de difusión, así que
funciona con interfaces modestas sin preamplificador extra. Esto es lo que más dinero
te ahorra.</li>
<li><strong>Carácter cálido</strong> con realce de presencia: la voz suena cercana sin
resultar afilada en sesiones largas.</li>
<li><strong>Construcción maciza.</strong> Es un bloque de metal; no se desajusta.</li>
<li><strong>Yugo integrado.</strong> Se monta en cualquier brazo con rosca estándar sin
accesorios.</li>
</ul>

<h2 id="pegas">Las pegas</h2>
<ul class="checks">
<li><strong>Pesa.</strong> Un brazo flojo se vence con él; presupuesta uno sólido.</li>
<li><strong>Exige cercanía.</strong> A más de un palmo pierde el cuerpo que lo hace
atractivo.</li>
<li><strong>El antipop interno no siempre basta</strong> en voces explosivas.</li>
<li><strong>No es USB.</strong> La interfaz es obligatoria.</li>
</ul>
<div class="note">
<strong>Regla práctica:</strong> si tu brazo no aguanta un kilo con holgura, cambia el
brazo antes que el micrófono.
</div>

<h2 id="precio">Precio y coste real</h2>
<table>
<thead><tr><th>Concepto</th><th>¿Obligatorio?</th><th>Rango</th></tr></thead>
<tbody>
<tr><td>Rode PodMic</td><td>Sí</td><td>99-150 USD</td></tr>
<tr><td>Interfaz de audio</td><td>Sí</td><td>110-200 USD</td></tr>
<tr><td>Cable XLR</td><td>Sí</td><td>10-25 USD</td></tr>
<tr><td>Brazo resistente</td><td>Sí</td><td>50-120 USD</td></tr>
<tr><td>Antipop externo</td><td>Según tu voz</td><td>8-20 USD</td></tr>
</tbody></table>

<h2 id="no-es">Para quién NO es</h2>
<ul class="checks">
<li>Si no quieres interfaz: busca un <a href="../usb-o-xlr/">micro USB</a>.</li>
<li>Si grabas instrumentos acústicos o canto delicado.</li>
<li>Si tu escritorio no aguanta un brazo pesado anclado.</li>
<li>Si te mueves mucho mientras hablas: valora un
<a href="../microfono-de-solapa/">micrófono de solapa</a>.</li>
</ul>
<p>Más opciones en <a href="../mejores-microfonos-podcast/">mejores micrófonos para
podcast</a>.</p>
""",
    }

    PAGES["audio-technica-at2020/"] = {
        "title": "Audio-Technica AT2020: análisis y para qué sirve de verdad",
        "desc": ("Audio-Technica AT2020: condensador de diafragma grande muy "
                 "recomendado. Cuándo es buena compra, versión XLR frente a USB y "
                 "qué cuarto necesita."),
        "h1": "Audio-Technica AT2020: el condensador de entrada que todos recomiendan",
        "crumb": "AT2020",
        "article": True, "kind": "Ficha",
        "lede": ("Es probablemente el condensador más recomendado para empezar. La "
                 "recomendación es justa, pero viene con una condición que casi nunca "
                 "se menciona."),
        "toc": [
            ("que-es", "Qué es"),
            ("versiones", "XLR o USB"),
            ("condicion", "La condición que nadie menciona"),
            ("precio", "Precio y coste real"),
            ("no-es", "Para quién NO es"),
        ],
        "faq": [
            ("¿El AT2020 necesita alimentación phantom?",
             "La versión XLR sí: es un condensador y requiere 48 V desde una interfaz o "
             "mezclador. La versión USB no, porque se alimenta por el propio puerto."),
            ("¿Es mejor el AT2020 XLR o el USB?",
             "Depende de si quieres crecer. El USB es más simple y suficiente para una "
             "sola voz; el XLR te permite cambiar interfaz, añadir un segundo micrófono "
             "y mejorar por piezas. La cápsula es de la misma familia en ambos."),
            ("¿El AT2020 sirve para un cuarto sin tratar?",
             "Es su punto débil. Al ser condensador capta el eco y el ruido de fondo con "
             "fidelidad. En una habitación viva, un dinámico del mismo precio suele dar "
             "un resultado final más limpio."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>Audio-Technica AT2020</strong> es un condensador de diafragma grande con
patrón cardioide fijo, pensado para estudio casero. Es el escalón donde mucha gente
entra en el audio con interfaz.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador, diafragma grande</td></tr>
<tr><td>Patrón polar</td><td>Cardioide fijo</td></tr>
<tr><td>Versiones</td><td>XLR y USB</td></tr>
<tr><td>Alimentación</td><td>48 V (XLR) o puerto USB</td></tr>
<tr><td>Rango orientativo</td><td>99-170 USD según versión</td></tr>
</tbody></table>

<h2 id="versiones">XLR o USB</h2>
<table>
<thead><tr><th></th><th>AT2020 XLR</th><th>AT2020 USB</th></tr></thead>
<tbody>
<tr><td>Necesita interfaz</td><td>Sí</td><td>No</td></tr>
<tr><td>Monitoreo directo</td><td>En la interfaz</td><td>Integrado según modelo</td></tr>
<tr><td>Dos micrófonos a la vez</td><td>Sí</td><td>Problemático</td></tr>
<tr><td>Coste de entrada</td><td>Mayor</td><td>Menor</td></tr>
<tr><td>Camino de mejora</td><td>Por piezas</td><td>Cambiar el micro entero</td></tr>
</tbody></table>

<h2 id="condicion">La condición que nadie menciona</h2>
<div class="note">
<strong>El AT2020 es una gran compra, pero en una habitación tranquila.</strong> Su
sensibilidad es justo lo que lo hace atractivo y lo que lo vuelve problemático en un
cuarto con eco.
</div>
<p>Haz la prueba antes de comprarlo: ponte en el centro del cuarto y da tres palmadas
fuertes. Si oyes una cola que rebota, este micrófono te va a grabar esa cola. En ese
caso, trata la sala primero o elige un dinámico.</p>

<h2 id="precio">Precio y coste real</h2>
<table>
<thead><tr><th>Concepto</th><th>Ruta XLR</th><th>Ruta USB</th></tr></thead>
<tbody>
<tr><td>Micrófono</td><td>99-130 USD</td><td>140-170 USD</td></tr>
<tr><td>Interfaz con phantom</td><td>110-200 USD</td><td>—</td></tr>
<tr><td>Cable XLR</td><td>10-25 USD</td><td>—</td></tr>
<tr><td>Araña y antipop</td><td>25-55 USD</td><td>25-55 USD</td></tr>
<tr><td>Brazo</td><td>40-95 USD</td><td>40-95 USD</td></tr>
</tbody></table>

<h2 id="no-es">Para quién NO es</h2>
<ul class="checks">
<li>Habitación con eco o ruido constante.</li>
<li>Teclado mecánico en directo.</li>
<li>Voces muy sibilantes sin intención de usar de-esser.</li>
<li>Quien quiere enchufar y olvidarse, si elige la versión XLR.</li>
</ul>
<p>Si tu cuarto es el problema, lee
<a href="../tratamiento-acustico-casero/">tratamiento acústico casero</a> o pásate a
<a href="../dinamico-vs-condensador/">un dinámico</a>.</p>
""",
    }

    PAGES["blue-yeti/"] = {
        "title": "Blue Yeti: análisis honesto y el error que comete todo el mundo",
        "desc": ("Blue Yeti: el micrófono USB más vendido. Patrones polares, por qué "
                 "suena mal a mucha gente y cómo configurarlo para que suene bien."),
        "h1": "Blue Yeti: buen micrófono, configuración casi siempre equivocada",
        "crumb": "Blue Yeti",
        "article": True, "kind": "Ficha",
        "lede": ("Es el micrófono USB más vendido del mundo y también del que más "
                 "gente se queja. Casi siempre por el mismo motivo, y tiene arreglo "
                 "gratis."),
        "toc": [
            ("que-es", "Qué es"),
            ("error", "El error que comete todo el mundo"),
            ("ajustes", "Cómo configurarlo bien"),
            ("precio", "Precio y coste real"),
            ("no-es", "Para quién NO es"),
        ],
        "faq": [
            ("¿Por qué mi Blue Yeti capta tanto ruido de fondo?",
             "Casi siempre por dos motivos combinados: está en modo omnidireccional en "
             "lugar de cardioide, y le hablas desde arriba en vez de por el lateral. "
             "Corrigiendo ambas cosas el ruido de fondo baja de forma muy notable."),
            ("¿Por dónde se habla al Blue Yeti?",
             "Por el lateral, al lado donde está el logotipo, no por la parte superior. "
             "Es un micrófono de direccionamiento lateral, y hablarle por arriba es el "
             "fallo más extendido con este modelo."),
            ("¿Qué patrón debo usar en el Blue Yeti para streaming?",
             "Cardioide siempre. Los modos omnidireccional, bidireccional y estéreo son "
             "para grabar ambientes o entrevistas presenciales y en un directo solo "
             "añaden ruido de la habitación."),
        ],
        "body": """
<h2 id="que-es">Qué es</h2>
<p>El <strong>Blue Yeti</strong> es un condensador USB de escritorio con cuatro patrones
polares conmutables, control de ganancia, silenciador y salida de auriculares con
monitoreo directo.</p>
<table>
<thead><tr><th>Característica</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo</td><td>Condensador USB</td></tr>
<tr><td>Patrones</td><td>Cardioide, omni, bidireccional, estéreo</td></tr>
<tr><td>Direccionamiento</td><td>Lateral</td></tr>
<tr><td>Monitoreo</td><td>Salida de auriculares integrada</td></tr>
<tr><td>Rango orientativo</td><td>100-150 USD</td></tr>
</tbody></table>

<h2 id="error">El error que comete todo el mundo</h2>
<div class="note">
<strong>Al Yeti se le habla por el lado, no por arriba.</strong> Tiene forma de
micrófono de pie, así que la gente le habla a la parte superior y acaba grabando
sobre todo la habitación.
</div>
<p>El segundo error es dejarlo en un patrón que no es cardioide. Viene con un selector
muy visible y es fácil moverlo sin querer. En omnidireccional capta los 360 grados de tu
cuarto, y entonces aparece la queja clásica: «se oye con eco y mucho ruido».</p>
<p>El tercero es la base de escritorio incluida: transmite cada golpe de la mesa
directamente a la cápsula.</p>

<h2 id="ajustes">Cómo configurarlo bien</h2>
<ol>
<li><strong>Patrón cardioide.</strong> Siempre, para hablar tú solo.</li>
<li><strong>Háblale al lateral del logotipo</strong>, a unos 15 cm.</li>
<li><strong>Ganancia baja</strong>, con picos en torno a -12 dB. Es sensible: casi
nunca necesita el mando alto.</li>
<li><strong>Pásalo a brazo con araña</strong> en cuanto puedas, y abandona la base.</li>
<li><strong>Filtro antipop</strong> a un palmo.</li>
<li><strong>Filtro paso alto en 80 Hz</strong> y compresor suave en
<a href="../configurar-microfono-obs/">OBS</a>.</li>
</ol>

<h2 id="precio">Precio y coste real</h2>
<table>
<thead><tr><th>Concepto</th><th>¿Obligatorio?</th><th>Rango</th></tr></thead>
<tbody>
<tr><td>Blue Yeti</td><td>Sí</td><td>100-150 USD</td></tr>
<tr><td>Brazo articulado</td><td>Muy recomendable</td><td>40-95 USD</td></tr>
<tr><td>Araña compatible</td><td>Recomendable</td><td>25-50 USD</td></tr>
<tr><td>Filtro antipop</td><td>Sí</td><td>8-20 USD</td></tr>
</tbody></table>
<p>Fíjate en el detalle: es USB, así que el coste total se queda muy por debajo de
cualquier ruta XLR equivalente.</p>

<h2 id="no-es">Para quién NO es</h2>
<ul class="checks">
<li><strong>Cuarto ruidoso o con eco.</strong> Es condensador; mira un dinámico.</li>
<li><strong>Dos personas grabando a la vez</strong> en el mismo ordenador con dos Yetis:
se desincronizan.</li>
<li><strong>Escritorios pequeños.</strong> Ocupa, y con brazo ocupa más.</li>
<li><strong>Quien nunca va a tocar la configuración.</strong> Sin ajustar, decepciona.</li>
</ul>
<p>Alternativa USB con araña integrada: <a href="../hyperx-quadcast-rgb/">HyperX
QuadCast</a>. Comparativa general:
<a href="../mejores-micros-streaming/">por presupuesto</a>.</p>
""",
    }
