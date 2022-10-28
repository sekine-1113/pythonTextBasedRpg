import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "-id", "--playerId",
    default=1,
    type=int,
    help="This is a player id"
)
parser.add_argument(
    "-dev", "--develop",
    help="This is a develop mode",
    action="store_true"
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-d", "--debug",
    help="This is a debug flag",
    action="store_true"
)
group.add_argument(
    "-i", "--info",
    help="This is a info flag",
    action="store_true"
)
group.add_argument(
    "-w", "--warning",
    help="This is a warning flag",
    action="store_true"
)
group.add_argument(
    "-e", "--error",
    help="This is a error flag",
    action="store_true"
)
group.add_argument(
    "-c", "--critical",
    help="This is a critical flag",
    action="store_true"
)

args = parser.parse_args()

if __name__ == "__main__":
    print(args)