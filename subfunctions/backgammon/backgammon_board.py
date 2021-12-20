#!/bin/python3
from sys import path
import pathlib
path.append(f'{pathlib.Path( __file__ ).parent.resolve()}/../misc');
from MDCG_log import db_log, investigate

class BackgammonBoard():
    def __init__(self):
        #initialize in default configuration
        self.spikes = 24;
        self.tilesPerPlayer = 15;

        self.state = [
            'ww', '', '', '', '', 'bbbbb', \
            '', 'bbb', '', '', '', 'wwwww', \
            'bbbbb', '', '', '', 'www', '', \
            'wwwww', '', '', '', '', 'bb'    
        ]; #initial configuration, written like a "C"
        for i, v in enumerate( self.state ):
            self.state[i] = self.state[i].ljust( self.tilesPerPlayer );
        db_log( self.state );

    def __str__(self):
        spaBetSpike = 2; #spaces between spikes
        maxRows = self.tilesPerPlayer; #can't have more than <> tiles stacked in one space
        rowsBetSides = 2;
        boardWidth = int( (spaBetSpike + 1)*self.spikes/2 - 1 );

        # Print Header
        headerStr = 'BACKGAMMON BOARD'.center(boardWidth, '=');
        print( headerStr );

        # Print side 1
        for iRow in range( maxRows ):
            for iSpike in range( int( self.spikes / 2 ) - 1, -1, -1 ):
                if( self.state[iSpike][iRow] == ' ' ):
                    print('|', end = '{: ^{width}}'.format( '', width = spaBetSpike ) );
                else:
                    print(self.state[iSpike][iRow], end = '{: ^{width}}'.format( '', width = spaBetSpike ) );
            print(); #newline

        # Gap between sides
        [print() for spaces in range( rowsBetSides )];

        # Print side 2
        for iRow in range( maxRows - 1, -1, -1 ):
            for iSpike in range( int( self.spikes / 2 ), int( self.spikes ) ):
                if( self.state[iSpike][iRow] == ' ' ):
                    print('|', end = '{: ^{width}}'.format( '', width = spaBetSpike ) );
                else:
                    print(self.state[iSpike][iRow], end = '{: ^{width}}'.format( '', width = spaBetSpike ) );
            print(); #newline
        # Close header
        print( ''.center( boardWidth, '=' ) );

        return '';

if __name__ == '__main__':
    # Test it
    testBoard = BackgammonBoard();
    print( testBoard );