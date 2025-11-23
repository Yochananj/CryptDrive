import flet as ft

from Client.src.Views.UIElements import FolderTile, FileTile
from Client.src.Dependencies.Constants import crypt_drive_blue_semilight, crypt_drive_purple, crypt_drive_blue, crypt_drive_fonts


class FileContainer:
    def __init__(self):
        self.title = ft.Text(value="Your Files", font_family="Aeonik Black", size=90, color=crypt_drive_blue)
        self.loading = ft.Container(
            content=
            ft.Row(
                controls=[
                    ft.ProgressRing(color=crypt_drive_purple, aspect_ratio=1, stroke_width=8, stroke_cap=ft.StrokeCap.ROUND),
                ],
                height=60,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
            alignment=ft.Alignment(0,0),
        )
        self.column = ft.Column(
            controls=[],
            expand=True,
            scroll=True,
        )
        self.tiles = ft.Column(
            controls=[],
        )
        self.animator = ft.AnimatedSwitcher(
            content=self.loading,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=500,
            switch_in_curve=ft.AnimationCurve.EASE_IN_CIRC,
            switch_out_curve=ft.AnimationCurve.EASE_OUT_CIRC,
            width=1100,
            height=810,
            expand=False,
        )
        self.current_directory: FolderTile = None
        self.directories: list[FolderTile] = []
        self.files: list[FileTile] = []
        self.upload_file_button = ft.FloatingActionButton(
            content=ft.Icon(name=ft.Icons.FILE_UPLOAD_OUTLINED, color=crypt_drive_purple),
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=crypt_drive_blue_semilight,
            elevation=0,
            width=50,
            height=50,
        )
        self.create_dir_button = ft.FloatingActionButton(
            content=ft.Icon(name=ft.Icons.CREATE_NEW_FOLDER, color=crypt_drive_purple),
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=crypt_drive_blue_semilight,
            elevation=0,
            height=50,
            width=50,
        )
        self.subtitle_row = ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.CENTER,
            expand_loose=True
        )
        self.create_dir_dialog_cancel = ft.TextButton(
            text="Cancel",
        )
        self.create_dir_dialog_confirm = ft.TextButton(
            text="Confirm",
        )
        self.create_dir_dialog_text_field = ft.TextField(
            value="",
            width=300,
            label="Directory Name",
            autofocus=True,
            prefix_icon=ft.Icon(ft.Icons.FOLDER_ROUNDED, color=crypt_drive_purple),
        )
        self.create_dir_dialog_content = ft.Container(
            content=
                ft.Column(
                    controls=[
                        ft.Text("Enter the name of the new directory:", font_family="Aeonik"),
                        self.create_dir_dialog_text_field
                    ],
                ),
            alignment=ft.Alignment(0,0),
            width=400,
            height=90,
            expand=False
        )
        self.create_dir_dialog = ft.AlertDialog(
            title=ft.Row([ft.Icon(ft.Icons.CREATE_NEW_FOLDER, color=crypt_drive_purple), ft.Text("Create New Directory", font_family="Aeonik Bold")]),
            modal=False,
            content=self.create_dir_dialog_content,
            actions=[self.create_dir_dialog_cancel, self.create_dir_dialog_confirm],
            bgcolor=crypt_drive_blue_semilight,
        )
        self.delete_file_dialog_cancel = ft.TextButton(text="Cancel")
        self.delete_file_dialog_confirm = ft.TextButton(text="Confirm", col=ft.Colors.RED)
        self.delete_file_dialog_title = ft.Text("Delete File", font_family="Aeonik Bold")
        self.delete_file_dialog = ft.AlertDialog(
            title=ft.Row([ft.Icon(ft.Icons.DELETE, color=crypt_drive_purple), self.delete_file_dialog_title]),
            modal=False,
            actions=[self.delete_file_dialog_cancel, self.delete_file_dialog_confirm],
            bgcolor=crypt_drive_blue_semilight,
        )
        self.file_picker = ft.FilePicker()

    def build(self):
        return self.column



def test(page: ft.Page):
    flc = FileContainer()
    flc.column.width = 900
    page.fonts = crypt_drive_fonts
    page.theme_mode = "light"
    page.add(flc.build())

    flc.current_directory = FolderTile("/", 0, is_current_directory=True)
    flc.subtitle_row.controls.append(flc.current_directory.tile)
    flc.subtitle_row.controls.append(flc.create_dir_button)
    flc.subtitle_row.controls.append(flc.upload_file_button)
    flc.tiles.controls.append(flc.subtitle_row)
    for i in range (10):
        flc.directories.append(FolderTile(f"/test{i}", i))
        flc.files.append(FileTile(f"test{i}.txt", i))

    for directory in flc.directories:
        flc.tiles.controls.append(directory.tile)

    for file in flc.files:
        flc.tiles.controls.append(file.tile)

    flc.column.controls.append(flc.title)
    flc.column.controls.append(flc.animator)
    page.update()
    flc.animator.content = flc.tiles
    flc.animator.update()
    page.update()


if __name__ == "__main__":
    ft.app(test)