"""
The Perfect Backgammon Game
    An experiment in AI

Author: Mickey T Da Silva

Goal: To beat my dad at Backgammon. He gets to use "Backgammon for Blood" and I get a computer

ToDo:
    - Backgammon game
    - 2 Player Mode
    - AI Training Mode
        - AI vs. Random AI
        - AI vs. Previous AI
    - Player vs. AI Mode
    - Guided Gaming Mode
"""
# Setup path
import sys, pathlib
scriptPath = pathlib.Path( __file__ ).parent.resolve();
pathList = [f'{scriptPath}/subfunctions', f'{scriptPath}/subfunctions/AI', f'{scriptPath}/subfunctions/backgammon', f'{scriptPath}/subfunctions/misc']
for reqPath in pathList:
    sys.path.append( reqPath );

# Setup logging
from MDCG_log import investigate, db_log

def main():
    db_log( 'Test log' );


if __name__ == '__main__': main();
