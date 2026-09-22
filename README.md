# MicrosStreaming

Sitio estatico de guias sobre micros para streaming. Web nicho SEO: una pagina
por palabra clave, primero posicionar y despues monetizar.

URL publica: https://microstreaming.github.io/

## Como editar

1. Edita `content.py` (guias) o `content_modelos.py` (fichas por modelo).
2. Ejecuta `python build.py`.
3. Commit y push: GitHub Pages publica la rama `main` desde la raiz.

El HTML generado (`index.html` de cada carpeta), `404.html`, `sitemap.xml` y
`robots.txt` se crean automaticamente. **No los edites a mano.**

La plantilla, el menu y los iconos estan en `build.py`; el diseno en
`assets/style.css` y `assets/app.js`.

## Cambiar la URL publica

GitHub Pages decide la URL por el nombre de la **cuenta**, no del repositorio:

| Cuenta | Repositorio | URL publicada |
|---|---|---|
| `microstreaming` | `microstreaming.github.io` | **`microstreaming.github.io/`** (actual) |
| `otracuenta` | `microstreaming.github.io` | `otracuenta.github.io/microstreaming.github.io/` |

Para publicar en `https://microstreaming.github.io/`:

1. Crea una organizacion gratuita de GitHub llamada exactamente `microstreaming`.
2. Crea dentro un repositorio publico llamado `microstreaming.github.io`.
3. Empuja este mismo codigo a ese repositorio y activa Pages en `main` / raiz.
4. Genera el sitio apuntando a la URL nueva:

```
MS_BASE=https://microstreaming.github.io python build.py
```

Esa variable de entorno cambia canonical, Open Graph, JSON-LD, el sitemap,
`robots.txt` y la pagina 404 de golpe. Cuando la mudanza sea definitiva,
cambia `BASE_DEFAULT` en `content.py` y deja de pasar la variable.

Conviene decidir la URL **antes** de que Google indexe: cambiarla despues
obliga a reindexar y se pierde parte del avance.

## Verificacion de Google Search Console

El fichero `google02704c519b649822.html` de la raiz es el comprobante de
propiedad de Google Search Console. **No lo borres ni lo renombres**: si
desaparece, Google retira la verificacion y se pierde el acceso a los
datos de la propiedad. `build.py` no lo toca.
