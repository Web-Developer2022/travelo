from locals import lang_pack

def get_language(request):
    url = request.get_full_path()
    lang = url.strip("/").split("/")[0]
    # lang = request.session.get("lang")
    if lang is not None:
        return lang_pack[lang]
    else:
        return lang_pack["uz"]