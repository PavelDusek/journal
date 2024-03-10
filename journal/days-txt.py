import re
import argparse
from rich import print
import pathlib
import os

def savefile( filename: str, text: str ) -> None:
    print(filename)
    print(text)
    print("-----"*3)
    print("\n"*5)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=str, help="directory where source filename will be searched for and where output files will be produced")
parser.add_argument("-s", "--source", type=str, help="source filename that should be separated into txt for each day")
args = parser.parse_args()

directory = pathlib.Path( args.dir )
source = pathlib.Path( args.source )
path = directory / source
if not os.path.exists( path ):
    print(f"[red][bold]File {path} not found!!![/bold][/red]")
    raise FileNotFoundError(f"File {path} not found!!!")
with open(path) as f:
    txt = f.read()

daysIter = re.finditer("== ?(\d+-\d+-\d+) ?==", txt)
previous = 0
for match in daysIter:
    day = match.groups()[0]
    start = match.start()

    if start == 0:
        pass
    else:
        savefile( filename = filename, text = txt[previous:start] )

    filename = directory / pathlib.Path( f"{day}.txt" )
    previous = start
savefile( filename = filename, text = txt[previous:] )
