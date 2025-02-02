import reflex as rx

from soydaviddev_portfolio.styles.styles import Size

def link_card(title:str, body:str, image:str, url:str ) -> rx.Component:
    return(
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(src=image),
                    rx.box(
                        rx.heading(title),
                        rx.text(
                            body
                        ),
                    ),
                    spacing=Size.MID_SMALL.value,
                ),
                href=url,
            ),
            as_child=True,
        ),
        # rx.box(
        #     rx.container(
        #         rx.card(
        #             "This content is constrained to a max width of 448px.",
        #             width="100%",
        #         ),
        #         size="1",
        #     ),
        #     rx.container(
        #         rx.card(
        #             "This content is constrained to a max width of 688px.",
        #             width="100%",
        #         ),
        #         size="2",
        #     ),
        #     rx.container(
        #         rx.card(
        #             "This content is constrained to a max width of 880px.",
        #             width="100%",
        #         ),
        #         size="3",
        #     ),
        #     rx.container(
        #         rx.card(
        #             "This content is constrained to a max width of 1136px.",
        #             width="100%",
        #         ),
        #         size="4",
        #     ),
        #     background_color="var(--gray-3)",
        #     width="100%",
        # ),
    )