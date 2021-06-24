
import cx_Freeze
executables = [cx_Freeze.Executable(
    script="game.py", icon="icon.ico")]

cx_Freeze.setup(
    name="Sitio da Emilia Pika",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["game"]
        }},
    executables=executables
)