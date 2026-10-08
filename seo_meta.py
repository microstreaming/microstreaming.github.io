# -*- coding: utf-8 -*-
"""Titulos y descripciones de todas las paginas, en un solo sitio.

Por que estan aqui y no junto al contenido: el titulo y la descripcion no
son contenido, son el anuncio del contenido. Se reescriben a menudo
mirando el porcentaje de clics en Search Console, y tenerlos juntos
permite revisarlos de una pasada y detectar repeticiones.

Reglas que sigue este fichero:
  - Titulo de 60 caracteres o menos. Google corta a partir de ahi.
  - La palabra clave primero, el gancho despues.
  - No empezar catorce titulos con la misma palabra: en los resultados
    compiten entre si y el ojo los lee como si fueran lo mismo.
  - Descripcion entre 120 y 158 caracteres, con algo concreto dentro:
    una cifra, una pega, una condicion. No un resumen generico.

build.py aplica estos valores sobre PAGES y falla si alguna clave sobra o
falta, para que no se queden paginas sin revisar.
"""

META = {
    # --- Guias principales ------------------------------------------
    "": (
        "Micros para streaming, podcast y homestudio | Guía 2026",
        "Qué micrófono comprar para streaming, YouTube, podcast o homestudio: "
        "USB o XLR, dinámico o condensador y cuánto gastar. Sin patrocinios."),
    "mejores-micros-streaming/": (
        "Mejores micros para streaming 2026, por presupuesto",
        "Comparativa por rango de precio con el coste real del conjunto y las "
        "pegas que las fichas de producto no cuentan. Cinco categorías."),
    "microfono-condensador/": (
        "Micrófono de condensador: cuándo sí y cuándo no",
        "Cómo funciona, por qué necesita phantom de 48 V y en qué habitaciones "
        "es mala idea comprarlo. Con una prueba práctica para decidirlo."),
    "usb-o-xlr/": (
        "Micrófono USB o XLR: cuál te conviene de verdad",
        "Comparativa con el coste total calculado: micro, interfaz, cable y "
        "brazo. Qué ganas con cada ruta y cuándo merece la pena el salto."),
    "micros-streaming-baratos/": (
        "Micros de streaming baratos que no suenan baratos",
        "Con poco presupuesto, el orden de compra importa más que la marca. "
        "Dónde recortar, dónde no, y ocho mejoras que cuestan cero."),
    "microfono-para-telefono/": (
        "Micrófono para teléfono: grabar bien desde el móvil",
        "Solapa, USB-C, Lightning y el lío de los conectores TRRS. Qué elegir "
        "según grabes quieto, en movimiento o en exteriores."),
    "behringer-c1-vs-c3/": (
        "Behringer C-1 vs C-3: cuál comprar y por qué",
        "Diferencias reales entre los dos: patrones polares, pad, filtro de "
        "graves y todo lo que hay que comprar además del micrófono."),
    "quienes-somos/": (
        "Quiénes somos y cómo evaluamos | MicrosStreaming",
        "Sitio independiente sobre micrófonos: sin tienda, sin afiliados y sin "
        "reseñas inventadas. Cómo elaboramos las guías y tratamos los precios."),

    # --- Indice y fichas Behringer ----------------------------------
    "por-modelo/": (
        "Micrófonos por modelo: todas las fichas",
        "Behringer, Shure, Rode, Neumann, Audio-Technica, HyperX y Blue. Para "
        "qué sirve cada modelo, qué necesita y cuándo es mala compra."),
    "behringer-c1/": (
        "Behringer C-1: precio real y qué necesitas además",
        "Cuesta poco, pero pide interfaz con phantom, cable, araña y antipop. "
        "El coste real del conjunto ronda los 200 USD. Para quién no es."),
    "behringer-c3/": (
        "Behringer C-3: patrones polares y para qué sirve",
        "Añade patrón omnidireccional, pad de -10 dB y filtro de graves sobre "
        "el C-1. Cuándo compensan esas opciones y cuándo no las usarás."),

    # --- Otras fichas -----------------------------------------------
    "microfono-condensador-neumann/": (
        "Condensador Neumann: qué estás pagando realmente",
        "Qué justifica el precio, qué notarás frente a uno barato y en qué "
        "cinco situaciones concretas es dinero mal invertido."),
    "hyperx-quadcast-rgb/": (
        "HyperX QuadCast RGB: análisis sin marketing",
        "Qué hace bien, qué pegas tiene de verdad y si las luces justifican su "
        "precio. Con los seis ajustes que necesita para sonar bien."),
    "microfono-array/": (
        "Micrófono array: qué es y cuándo lo necesitas",
        "Cómo funciona el beamforming y por qué, pese a toda su tecnología, es "
        "mala elección para streaming, podcast o voz en off."),
    "microfono-electronico/": (
        "Micrófono electrónico: qué significa de verdad",
        "No es una categoría técnica. Qué es realmente un electret, en qué se "
        "diferencia de un condensador y cuándo te basta con uno."),
    "shure-antena/": (
        "Antenas Shure: por qué se corta tu inalámbrico",
        "Tipos de antena, por qué los sistemas llevan dos, dónde colocarlas y "
        "cómo diagnosticar cortes, ruido y pérdida de alcance."),

    # --- Guias de apoyo ---------------------------------------------
    "dinamico-vs-condensador/": (
        "Dinámico vs condensador: cuál elegir de verdad",
        "No es cuestión de calidad, sino de cuánto ruido tiene tu habitación. "
        "Test práctico de tres palmadas y veredicto por situación."),
    "mejores-microfonos-podcast/": (
        "Mejores micrófonos para podcast, por nº de voces",
        "El montaje lo decide cuánta gente habla en la sala. Qué necesitas "
        "solo, con invitado presencial o en remoto, y qué errores evitar."),
    "microfono-para-youtube/": (
        "Micrófono para YouTube: elige por formato",
        "Qué usar según el micro pueda salir en plano o no, qué cambia en "
        "vídeo de formato largo y cómo sincronizar audio y vídeo."),
    "configurar-microfono-obs/": (
        "Configurar el micrófono en OBS: paso a paso",
        "La cadena de cinco filtros en el orden que funciona, con valores de "
        "partida para cada uno y una tabla de diagnóstico por síntoma."),
    "quitar-ruido-de-fondo/": (
        "Cómo quitar el ruido de fondo del micrófono",
        "Cuatro niveles, del más eficaz al menos: apagar la fuente, acercarte, "
        "tratar el cuarto y, solo al final, el software. En ese orden."),
    "brazo-y-arana-antivibracion/": (
        "Brazo y araña antivibración: qué comprar",
        "Capacidad de peso, tipos de anclaje y el lío de las roscas 3/8 y 5/8. "
        "Por qué mejora tu sonido más que cambiar de micrófono."),

    # --- Fichas de modelo -------------------------------------------
    "shure-sm58/": (
        "Shure SM58: ¿sigue mereciendo la pena en 2026?",
        "El dinámico más vendido de la historia aplicado a podcast y "
        "streaming. Qué ganancia pide de verdad y en qué casos no es tu micro."),
    "shure-sm7b/": (
        "Shure SM7B: el aviso antes de comprarlo",
        "Pide unos 60 dB de ganancia limpia y muchas interfaces no llegan. Qué "
        "lo justifica, el coste real del conjunto y para quién no es."),
    "rode-podmic/": (
        "Rode PodMic: sonido de radio sin pagar de más",
        "Dinámico de difusión que pide menos ganancia que sus rivales caros. "
        "Lo que hace bien, sus pegas reales y el coste completo del montaje."),
    "audio-technica-at2020/": (
        "Audio-Technica AT2020: la condición que nadie dice",
        "Gran condensador de entrada, pero solo en una sala tranquila. Versión "
        "XLR o USB, coste real y cómo saber si tu cuarto sirve."),
    "blue-yeti/": (
        "Blue Yeti: por qué suena mal y cómo arreglarlo",
        "Se le habla por el lado, no por arriba, y en cardioide. Los tres "
        "errores que arruinan el micro USB más vendido, y sus ajustes."),

    # --- Equipo de apoyo --------------------------------------------
    "interfaz-de-audio/": (
        "Interfaz de audio: qué mirar antes de comprar",
        "Ganancia, phantom, entradas y monitoreo directo. Qué especificaciones "
        "deciden tu compra y cuáles puedes ignorar tranquilamente."),
    "filtro-antipop/": (
        "Filtro antipop: para qué sirve y dónde ponerlo",
        "Resuelve un solo problema y del todo: el golpe de aire de las "
        "explosivas. Nailon o metal, distancia correcta y cuándo no hace falta."),
    "microfono-de-solapa/": (
        "Micrófono de solapa: cómo colocarlo bien",
        "Dónde prenderlo exactamente, cómo evitar el roce de la ropa y qué "
        "conector necesitas. Cuándo gana a un micrófono de escritorio."),
    "microfono-inalambrico/": (
        "Micrófono inalámbrico: la letra pequeña",
        "Alcance real, autonomía, grabación de respaldo y 2,4 GHz frente a "
        "UHF. Qué mirar antes de comprar y por qué se cortan en mitad de una toma."),

    # --- Por situacion ----------------------------------------------
    "microfono-para-gaming/": (
        "Micrófono para gaming: que no se oiga el teclado",
        "Tu problema no es el de un locutor: tienes teclado mecánico y "
        "ventiladores al lado. Qué micro lo evita y cómo ajustarlo en Discord."),
    "microfono-para-cantar/": (
        "Micrófono para cantar en casa: qué necesitas",
        "Cantar delata el cuarto mucho más que hablar. Condensador o dinámico "
        "según tu sala, la cadena mínima y qué hacer con la acústica."),
    "microfono-para-videollamadas/": (
        "Micrófono para videollamadas: que te entiendan",
        "En una reunión no se valora tu timbre, sino que no tengas que "
        "repetir. Las cuatro opciones reales y los ajustes que te sabotean."),
    "microfono-para-voz-en-off/": (
        "Micrófono para voz en off: aquí manda el detalle",
        "El único caso donde recomendamos condensador sin matices. Qué nivel "
        "de silencio necesitas y cómo montar una cabina casera que funcione."),

    # --- Tecnica y procesado ----------------------------------------
    "phantom-48v/": (
        "Phantom 48 V: qué es y cuándo hace falta",
        "La causa número uno de condensadores que parecen defectuosos. Qué "
        "micrófonos la necesitan, el orden correcto y si daña a los dinámicos."),
    "efecto-proximidad/": (
        "Efecto de proximidad: por qué suenas más grave",
        "Ese cuerpo de voz de radio viene de la distancia, no del micrófono. "
        "Qué patrones lo tienen, cómo usarlo a tu favor y cómo corregirlo."),
    "ganancia-del-microfono/": (
        "Ganancia del micrófono: ni al máximo ni al mínimo",
        "Qué nivel buscar, por qué no debe llegar nunca a 0 dB y en qué se "
        "diferencia del volumen. Diagnóstico por síntoma para quitar el ruido."),
    "compresor-de-voz/": (
        "Compresor para voz: ajustarlo sin estropearla",
        "Qué hace cada control explicado sin jerga, valores de partida para "
        "locución, podcast y directo, y las señales de que te has pasado."),
    "ecualizar-la-voz/": (
        "Cómo ecualizar la voz: las cuatro zonas clave",
        "Recortar suena natural, realzar suena artificial. Qué hace cada "
        "banda, recetas por problema y los errores que estropean una toma."),

    # --- Problemas y acustica ---------------------------------------
    "microfono-no-funciona-windows/": (
        "El micrófono no funciona en Windows: solución",
        "Permisos, dispositivo equivocado, uso exclusivo y niveles. "
        "Diagnóstico de lo más probable a lo menos, con tabla por síntoma."),
    "latencia-del-microfono/": (
        "Latencia del micrófono: oírte con retardo",
        "Por qué ocurre, qué es el monitoreo directo y qué tamaño de búfer "
        "usar. Cuánta latencia es tolerable y cuándo deja de importar."),
    "tratamiento-acustico-casero/": (
        "Tratamiento acústico casero: qué sí y qué no",
        "Insonorizar y acondicionar no son lo mismo, y confundirlos cuesta "
        "dinero. Qué funciona gratis, qué no hace nada y dónde colocarlo."),
}

TITULO_MAX = 60
DESC_MIN = 110
DESC_MAX = 158


def apply(PAGES):
    """Vuelca META sobre PAGES y comprueba que no falte ni sobre nada."""
    faltan = set(PAGES) - set(META)
    sobran = set(META) - set(PAGES)
    if faltan:
        raise SystemExit("seo_meta: sin titulo revisado: %s" % sorted(faltan))
    if sobran:
        raise SystemExit("seo_meta: claves que ya no existen: %s" % sorted(sobran))

    problemas = []
    for slug, (titulo, desc) in META.items():
        if len(titulo) > TITULO_MAX:
            problemas.append("titulo %d car. en %r" % (len(titulo), slug or "/"))
        if not (DESC_MIN <= len(desc) <= DESC_MAX):
            problemas.append("desc %d car. en %r" % (len(desc), slug or "/"))
        PAGES[slug]["title"] = titulo
        PAGES[slug]["desc"] = desc
    if problemas:
        raise SystemExit("seo_meta:\n  " + "\n  ".join(problemas))
