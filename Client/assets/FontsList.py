import enum
import os


class FontsList(enum.Enum):
    Aeonik =  f"{os.path.dirname(__file__)}/assets/Aeonik/AeonikExtendedLatinHebrew-Regular.otf",
    Aeonik_Bold =  f"{os.path.dirname(__file__)}/assets/Aeonik/AeonikExtendedLatinHebrew-Bold.otf",
    Aeonik_Black =  f"{os.path.dirname(__file__)}/assets/Aeonik/AeonikExtendedLatinHebrew-Black.otf",
    Aeonik_Thin = f"{os.path.dirname(__file__)}/assets/Aeonik/AeonikExtendedLatinHebrew-Thin.otf"
    