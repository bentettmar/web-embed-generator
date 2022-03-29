import flask


import flask
import urllib.parse

blueprint = flask.Blueprint("general", __name__, url_prefix="/")

@blueprint.route("/")
def index():
    args = flask.request.args

    title = args.get("title", "")
    description = args.get("description", "")
    url = args.get("url", "")
    colour = args.get("colour", "") or args.get("color", "") or "000000"
    image = args.get("image", "")
    author_name = args.get("author_name", "")
    author_url = args.get("author_url", "")
    provider_name = args.get("provider_name", "")
    provider_url = args.get("provider_url", "")

    oembed_params = {
        "title": title,
        "author_name": author_name,
        "author_url": author_url,
        "provider_name": provider_name,
        "provider_url": provider_url
    }

    oembed_link = flask.url_for("oembed.generator") + "?" + urllib.parse.urlencode(oembed_params)

    return flask.render_template(
        "embed.html",
        embed_title=title,
        embed_description=description,
        embed_url=url,
        embed_colour=colour,
        embed_image=image,
        oembed_link=oembed_link
    )