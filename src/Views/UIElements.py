import flet as ft

from Dependencies.Constants import crypt_drive_blue_semilight, crypt_drive_purple


def error_alert(error_message: str):
    return ft.SnackBar(
        duration=5000,
        content=ft.Row(
            controls=[ft.Icon(ft.Icons.CLOSE_ROUNDED, color=ft.Colors.RED),
                      ft.Text(error_message, color=ft.Colors.RED)],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        ),
        behavior=ft.SnackBarBehavior.FLOATING,
        bgcolor=ft.Colors.RED_100,
        shape=ft.ContinuousRectangleBorder(radius=10),
        margin=ft.margin.all(10),
    )

def success_alert(success_message: str):
    return ft.SnackBar(
        duration=5000,
        content=ft.Row(
            controls=[ft.Icon(ft.Icons.CHECK_ROUNDED, color=ft.Colors.GREEN),
                      ft.Text(success_message, color=ft.Colors.GREEN)],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        ),
        behavior=ft.SnackBarBehavior.FLOATING,
        bgcolor=ft.Colors.GREEN_100,
        shape=ft.ContinuousRectangleBorder(radius=10),
        margin=ft.margin.all(10),
    )

class FileTile:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size
        self.download = ft.IconButton(
            ft.Icons.FILE_DOWNLOAD_OUTLINED,
            on_click=lambda _: None,
            tooltip="Download File"
        )
        self.edit = ft.IconButton(
            ft.Icons.EDIT,
            on_click=lambda _: None,
            tooltip="Rename File"
        )
        self.delete = ft.IconButton(
            ft.Icons.DELETE,
            on_click=lambda _: None,
            tooltip="Delete File"
        )
        self.tile = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.INSERT_DRIVE_FILE),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls =[
                                    ft.Text(self.name, font_family="Aeonik Bold", size=20),
                                    ft.Text(f"Size: {self.size} bytes", font_family="Aeonik", size=16)
                                ]
                            )
                        ], expand = True
                    ),
                    self.download,
                    self.edit,
                    self.delete,
                ]
            ), border_radius=10, bgcolor=crypt_drive_blue_semilight, padding=ft.padding.only(left=10, right=10, top=10, bottom=10)
        )


class FolderTile:
    def __init__(self, path, item_count, is_current_directory=False):
        self.name = path.split("/")[-1]

        self.path = "/" if self.name == "" else path[:-(len(self.name))]

        self.items = item_count

        self.parent_icon = ft.Icons.DRIVE_FOLDER_UPLOAD_ROUNDED

        self.tooltip = "Click to return to Parent Folder"

        self.is_root = False

        self.rename = ft.IconButton(
            icon=ft.Icons.EDIT,
            tooltip="Rename Folder"
        )
        self.delete = ft.IconButton(
            icon=ft.Icons.DELETE,
            tooltip="Delete Folder"
        )

        if self.path == "/" and self.name == "":
            self.is_root = True
            self.parent_icon = ft.Icons.HOME_ROUNDED
            self.tooltip = "Already at root folder"

        self.has_shadow = False

        self.tile = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.FOLDER),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls =[
                                    ft.Text(self.name, font_family="Aeonik Bold", size=20),
                                    ft.Text(f"{self._get_items_string(self.items)}", font_family="Aeonik", size=16)
                                ],
                                height=40,
                            )
                        ],
                        expand = True,
                    ),
                    self.rename,
                    self.delete,
                ],
            ),
            border_radius=10,
            bgcolor=crypt_drive_blue_semilight,
            padding=ft.padding.only(left=10, right=10, top=10, bottom=12),
            tooltip="Click to open folder",
            # on_hover=lambda e: self.add_shadow(e),
        )

        if is_current_directory:
            if self.is_root:
                self.tile = ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(self.parent_icon, color=crypt_drive_purple),
                            ft.Text(self.path, font_family="Aeonik Bold" if not self.is_root else "Aeonik Black",
                                    size=20),
                            ft.Text(self.name, font_family="Aeonik Black", size=20)
                        ],
                    ),
                    tooltip=self.tooltip,
                    border_radius=10,
                    bgcolor=crypt_drive_blue_semilight,
                    padding=ft.padding.all(10),
                    expand=True,
                )
            else:
                self.tile=ft.FloatingActionButton(
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(self.parent_icon, color=crypt_drive_purple),
                                ft.Text(self.path, font_family="Aeonik Bold" if not self.is_root else "Aeonik Black", size=20),
                                ft.Text(self.name, font_family="Aeonik Black", size=20)
                            ],
                        ),
                        tooltip=self.tooltip,
                        border_radius=10,
                        bgcolor=crypt_drive_blue_semilight,
                        padding=ft.padding.all(10),
                        expand=True,
                    ),
                    bgcolor=crypt_drive_blue_semilight,
                    elevation=0,
                    expand=True,
                    height=50,
                )


    def _get_items_string(self, item_count: int):
        if item_count == 1:
            return "1 item"
        else:
            return f"{item_count} items"


    # def add_shadow(self, event: ControlEvent):
    #     logging.debug("Adding / Removing Shadow")
    #
    #     if not self.has_shadow:
    #         event.control.shadow = ft.BoxShadow(
    #             spread_radius=3,
    #             blur_radius=10,
    #             color=ft.Colors.GREY,
    #             offset=ft.Offset(1, 1),
    #             blur_style=ft.ShadowBlurStyle.NORMAL
    #         )
    #     else:
    #         event.control.shadow = None
    #
    #     self.has_shadow = not self.has_shadow
    #
    #     event.control.update()



def test(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    for i in range(10):
        page.add(FolderTile(f"index: {i}", 0).tile)

if __name__ == "__main__":
    ft.app(test)