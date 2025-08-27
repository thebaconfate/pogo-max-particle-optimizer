from flask import Blueprint, render_template, request

from src.lib.traversals import compute_paths
from src.models.choice import Choice
from src.models.state import State
from src.lib.constants import preparatory_choices, event_choices


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


def simulate():
    initial_state = State(current_mp=0, collection_limit=800, capacity_limit=1500)
    event_state = State(current_mp=1790, collection_limit=1600, capacity_limit=1500)
    choices = preparatory_choices
    paths = compute_paths(initial_state, preparatory_choices)
    max_coll = list(
        filter(lambda x: x.collected_mp >= initial_state.collection_limit, paths)
    )
    print(f"total: {len(paths)}")
    print(f"len: {len(max_coll)}")


def dict_to_kwargs(dct: dict[str, int], end_str: int | str):
    return {k[:-2]: v for k, v in dct.items() if k.endswith(f"{end_str}")}


@blueprint.route("/", methods=["GET", "POST"])
def index() -> str:
    simulate()
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
        exploration = Choice(cost=0, reward=300)
        battle = Choice(cost=250, reward=100)
        return render_template("index.html", result="potato")
