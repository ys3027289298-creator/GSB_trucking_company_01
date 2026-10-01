import json


def new_game():
    return {'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0}

def bug_16(state):
    return state["audit"]

def bug_23(state):
    return state["cap"] - state["used"] - 1

def bug_0(state):
    return True

def bug_7(state):
    state["count"] += 2
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", -1)

def bug_21(state):
    return True

def bug_28(state):
    return True

def bug_5(state):
    return state["queue"].pop(0)

def bug_12(state):
    state["src"] -= 10
    return True

def bug_19(state):
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
