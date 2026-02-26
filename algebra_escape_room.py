"""Text-based Algebra Escape Room game."""


def ask_with_hint(prompt, expected_answer, hint_text, lives):
    """Ask the player if they want a hint, then ask the room question."""
    want_hint = input("Do you want a hint? (yes/no): ").strip().lower()

    # Show a hint only when the player explicitly asks for one.
    if want_hint == "yes":
        print(f"Hint: {hint_text}")

    answer = input(prompt).strip().lower()

    # Compare using lowercase strings so answers like "X=4" and "x=4" both work.
    if answer == expected_answer:
        print("Correct! The door unlocks...\n")
        return True, lives

    # Wrong answer costs one life.
    lives -= 1
    print(f"Incorrect. You lose 1 life. Lives remaining: {lives}\n")
    return False, lives


def main():
    """Run the Algebra Escape Room game loop."""
    lives = 3

    print("=" * 55)
    print("      WELCOME TO THE ALGEBRA ESCAPE ROOM")
    print(" Solve each puzzle to unlock all 3 rooms and escape!")
    print("=" * 55)
    print(f"You start with {lives} lives.\n")

    rooms = [
        {
            "name": "Room 1",
            "question": "Room 1 - Solve 2x + 6 = 14. What is x? ",
            "answer": "4",
            "hint": "Subtract 6 from both sides, then divide by 2.",
        },
        {
            "name": "Room 2",
            "question": "Room 2 - Simplify 3x + 2x - 4: ",
            "answer": "5x-4",
            "hint": "Combine like terms: 3x and 2x.",
        },
        {
            "name": "Room 3",
            "question": (
                "Room 3 - Twice a number plus 3 equals 15. "
                "What is the number? "
            ),
            "answer": "6",
            "hint": "Set it up as 2n + 3 = 15.",
        },
    ]

    for room in rooms:
        print(f"--- {room['name']} ---")

        # Keep asking the same room until the player solves it or loses all lives.
        while True:
            correct, lives = ask_with_hint(
                room["question"], room["answer"], room["hint"], lives
            )

            if correct:
                break

            # End the game immediately when lives reach zero.
            if lives == 0:
                print("Game Over")
                return

    # Big victory message after all rooms are cleared.
    print("\n" + "*" * 60)
    print("*** CONGRATULATIONS! YOU ESCAPED THE ALGEBRA ESCAPE ROOM! ***")
    print("*** You solved every puzzle and made it out safely!       ***")
    print("*" * 60)


if __name__ == "__main__":
    main()
