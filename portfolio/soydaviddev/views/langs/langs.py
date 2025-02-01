import reflex as rx
from soydaviddev.styles.styles import Size as Size
from soydaviddev.components.title import title
from soydaviddev.components.link_langs import link_langs

def langs() -> rx.Component:
    return rx.vstack(

        title("Lenguajes de programación"),
        rx.hstack(
            link_langs("icons/python.svg"),
            link_langs("icons/square-js.svg"),
            link_langs("icons/typescript.svg"),
            link_langs("icons/html5.svg"),
            link_langs("icons/css3-alt.svg"),
            spacing=Size.VERY_BIG2.value,
        ),
        title("Frameworks y Librerías"),
        rx.hstack(
            link_langs("icons/django.svg"),
            link_langs("icons/vuejs.svg"),
            link_langs("icons/nuxt.svg"),
            link_langs("icons/angular.svg"),
            spacing=Size.VERY_BIG2.value,
        ),
        title("Bases de datos"),
        rx.hstack(
            link_langs("icons/mysql.svg"),
            link_langs("icons/mongo-db.svg"),
            link_langs("icons/postgresql.svg"),
            link_langs("icons/dynamodb.svg"),
            spacing=Size.VERY_BIG2.value,
        ),
        title("Herramientas y Tecnologías de infraestructura"),
        rx.hstack(
            link_langs("icons/icons8-aws-96.png"),
            link_langs("icons/docker.svg"),
            link_langs("icons/github.svg"),
            link_langs("icons/clean-code.svg"),
            link_langs("icons/api.svg"),
            spacing=Size.BIG.value,
        ),
        width="100%",
        align_items="center",
        spacing=Size.MEDIUM.value,
    )