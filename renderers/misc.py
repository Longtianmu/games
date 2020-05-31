# -*- coding: utf-8 -*-

import os
from datetime import datetime
from markdown2 import Markdown
from utils.sitemap import openw_with_sm

context= {
    "rr": "..",
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    context["datetime"] = datetime

    markdowner = Markdown()
    with open("README." + language + ".md") as f:
        context["index_content"] = markdowner.convert(f.read())

    context["active_search"] = "actived"
    with open(os.path.join(output, language, "search.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("search.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_search"]

    context["active_index"] = "actived"
    with openw_with_sm(output, os.path.join(language, "index.html"), priority="0.5",
            lastmod_file="README." + language + ".md") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("index.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_index"]

    with open("doc/faq." + language + ".md") as f:
        context["content"] = markdowner.convert(f.read())
    context["active_faq"] = "actived"
    with openw_with_sm(output, os.path.join(language, "faq.html"), priority="0.5",
            lastmod_file="doc/faq." + language + ".md") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_faq"]
    del context["content"]

    with openw_with_sm(output, os.path.join(language, "sensitive.html"), priority="0.3",
            lastmod_file="templates/sensitive.html") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("sensitive.html").render(context))
        f.write(env.get_template("footer.html").render(context))
