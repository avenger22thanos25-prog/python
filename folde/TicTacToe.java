import java.util.Scanner;

public class TicTacToe {
    private static final char EMPTY = ' ';

    public static void main(String[] args) {
        char[] board = {
            EMPTY, EMPTY, EMPTY,
            EMPTY, EMPTY, EMPTY,
            EMPTY, EMPTY, EMPTY
        };
        Scanner scanner = new Scanner(System.in);
        char currentPlayer = 'X';
        int moves = 0;

        System.out.println("Tic-Tac-Toe");
        System.out.println("Choose a position from 1 to 9 as shown below:");
        printBoard(new char[]{'1', '2', '3', '4', '5', '6', '7', '8', '9'});

        while (true) {
            printBoard(board);
            System.out.print("Player " + currentPlayer + ", choose a position: ");

            if (!scanner.hasNextInt()) {
                System.out.println("Please enter a number from 1 to 9.");
                scanner.next();
                continue;
            }

            int position = scanner.nextInt();
            if (position < 1 || position > 9 || board[position - 1] != EMPTY) {
                System.out.println("That position is unavailable. Choose an empty position from 1 to 9.");
                continue;
            }

            board[position - 1] = currentPlayer;
            moves++;

            if (hasWon(board, currentPlayer)) {
                printBoard(board);
                System.out.println("Player " + currentPlayer + " wins!");
                break;
            }

            if (moves == board.length) {
                printBoard(board);
                System.out.println("It's a draw!");
                break;
            }

            currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
        }

        scanner.close();
    }

    private static boolean hasWon(char[] board, char player) {
        int[][] winningLines = {
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
            {0, 4, 8}, {2, 4, 6}
        };

        for (int[] line : winningLines) {
            if (board[line[0]] == player
                    && board[line[1]] == player
                    && board[line[2]] == player) {
                return true;
            }
        }
        return false;
    }

    private static void printBoard(char[] board) {
        System.out.println();
        System.out.println(" " + board[0] + " | " + board[1] + " | " + board[2]);
        System.out.println("---+---+---");
        System.out.println(" " + board[3] + " | " + board[4] + " | " + board[5]);
        System.out.println("---+---+---");
        System.out.println(" " + board[6] + " | " + board[7] + " | " + board[8]);
        System.out.println();
    }
}
