from flask import Blueprint, render_template, request


blueprint = Blueprint("/", __name__)

day_0_keys = [
    "initial-mp-0",
    "collection-limit-0",
    "capacity-limit-0",
    "exploration-mp-0",
]
defaults = {
    day_0_keys[0]: 0,
    day_0_keys[1]: 800,
    day_0_keys[2]: 1600,
    day_0_keys[3]: 300,
}


def dict_to_kwargs(dct: dict[str, int], end_str: int | str):
    return {k[:-2]: v for k, v in dct.items() if k.endswith(f"{end_str}")}


@blueprint.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "GET":
        return render_template("index.html", defaults=defaults)
    else:
        day0 = defaults.copy()
        day0.update(
            {
                k: int(v)
                for k, v in ((k, request.form.get(k)) for k in day_0_keys)
                if v not in (None, "")
            }
        )
        day0 = dict_to_kwargs(day0, 0)
        return render_template("index.html", result="potato")
