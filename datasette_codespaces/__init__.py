from datasette import hookimpl
import os


def get_codespace_name():
    return os.environ.get("CODESPACE_NAME", "")


@hookimpl
def startup():
    codespace_name = get_codespace_name()
    if codespace_name:
        print("Running on GitHub Codespace:", codespace_name)
        print("https://{}-8001.preview.app.github.dev/".format(codespace_name))


@hookimpl
def actor_from_request():
    if get_codespace_name():
        return {"id": "root"}
