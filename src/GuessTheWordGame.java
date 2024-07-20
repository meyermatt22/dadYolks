import java.util.*;

public class GuessTheWordGame {
    private static List<String> wordList = Arrays.asList("programming", "java", "computer", "algorithm", "datastructure");
    private static String secretWord;
    private static Set<Character> guessedLetters = new HashSet<>();
    private static int maxAttempts = 6;

    public static void main(String[] args) {
        startGame();
        playGame();
    }

    private static void startGame() {
        // Choose a random word from the list
        secretWord = wordList.get(new Random().nextInt(wordList.size()));

        // Initialize guessed letters
        guessedLetters.clear();

        // Display a welcoming message
        System.out.println("Welcome to Guess the Word Game!");
        System.out.println("Try to guess the word. It could be related to programming.");

        // Display the initial state of the word
        showWordState();
    }

    private static void playGame() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Get user input
            System.out.print("Enter a letter: ");
            char guess = scanner.next().charAt(0);

            // Check if the letter has already been guessed
            if (guessedLetters.contains(guess)) {
                System.out.println("You already guessed that letter. Try again.");
                continue;
            }

            // Add the guessed letter to the set
            guessedLetters.add(guess);

            // Check if the guessed letter is in the secret word
            if (secretWord.contains(String.valueOf(guess))) {
                System.out.println("Good guess!");
            } else {
                System.out.println("Incorrect guess. Try again.");
                maxAttempts--;

                // Check if the player has run out of attempts
                if (maxAttempts == 0) {
                    System.out.println("Sorry, you've run out of attempts. The word was: " + secretWord);
                    break;
                }
            }

            // Display the current state of the word
            showWordState();

            // Check if the player has guessed all letters
            if (isWordGuessed()) {
                System.out.println("Congratulations! You've guessed the word: " + secretWord);
                break;
            }
        }

        // Close the scanner
        scanner.close();
    }

    private static void showWordState() {
        // Display the current state of the word with underscores for unguessed letters
        for (char letter : secretWord.toCharArray()) {
            if (guessedLetters.contains(letter)) {
                System.out.print(letter + " ");
            } else {
                System.out.print("_ ");
            }
        }

        // Display the number of attempts remaining
        System.out.println("\tAttempts remaining: " + maxAttempts);
    }

    private static boolean isWordGuessed() {
        // Check if all letters in the word have been guessed
        for (char letter : secretWord.toCharArray()) {
            if (!guessedLetters.contains(letter)) {
                return false;
            }
        }
        return true;
    }
}
