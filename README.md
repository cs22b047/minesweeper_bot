[Screencast from 14-05-24 04:35:45 PM IST.webm](https://github.com/cs22b047/minesweeper_bot/assets/145146625/5b8cad5f-97dc-4eee-aab3-26b73e9fdb54)

## How it works
1. Take a screenshot of the game board
2. crop the image
3. run a classsifer algorithm to extract contents of the board and store them in a 2d-array
4. analyze the array
5. send clicks
6. go to 1

## What can be improved

- right now i'm using hard coded values for cropping the game board. there must be a better way to do this.
- There are many redundent clicks. This can be reduced.
- the guess function can be improved to increase accuracy
