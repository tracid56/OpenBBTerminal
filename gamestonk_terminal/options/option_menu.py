import argparse
import requests

from gamestonk_terminal import config_terminal as cfg
from gamestonk_terminal.helper_funcs import get_flair, parse_known_args_and_warn
from gamestonk_terminal.options import get_volume_graph

def volume(l_args, s_ticker):
    """ Show traded options volume. [Source: Yahoo Finance] """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="volume",
        description="""Display volume graph for a date. [Source: Yahoo Finance].""",
    )

    l_similar = []
    try:
        ns_parser = parse_known_args_and_warn(parser, l_args)
        if not ns_parser:
            return

    except Exception as e:
        print(e)

    print("")
    return l_similar

def opt_menu(df_stock, s_ticker, s_start, s_interval):

    # Add list of arguments that the options parser accepts
    opt_parser = argparse.ArgumentParser(prog="opt", add_help=False)
    choices = [
        "help",
        "q",
        "quit",
        "volume"
    ]
    opt_parser.add_argument("cmd", choices=choices)
    completer = NestedCompleter.from_nested_dict({c: None for c in choices})

    print_technical_analysis(s_ticker, s_start, s_interval)

    # Loop forever and ever
    while True:
        # Get input command from user
        if session and gtff.USE_PROMPT_TOOLKIT:
            as_input = session.prompt(
                f"{get_flair()} (opt)> ",
                completer=completer,
            )
        else:
            as_input = input(f"{get_flair()} (opt)> ")

        # Images are non blocking - allows to close them if we type other command
        plt.close()

        # Parse fundamental analysis command of the list of possible commands
        try:
            (ns_known_args, l_args) = opt_parser.parse_known_args(as_input.split())

        except SystemExit:
            print("The command selected doesn't exist\n")
            continue

        if ns_known_args.cmd == "help":
            print_technical_analysis(s_ticker, s_start, s_interval)

        elif ns_known_args.cmd == "q":
            # Just leave the FA menu
            return False

        elif ns_known_args.cmd == "quit":
            # Abandon the program
            return True

        else:
            print("Command not recognized!")
