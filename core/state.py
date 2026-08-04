import json
import os


STATE_FILE = "data/state.json"


def load_state():

    if not os.path.exists(STATE_FILE):

        return {}


    with open(
        STATE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_state(data):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        STATE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )



def get_last_message(channel):

    state = load_state()

    return state.get(
        str(channel),
        0
    )



def set_last_message(channel, message_id):

    state = load_state()

    state[str(channel)] = message_id

    save_state(state)
