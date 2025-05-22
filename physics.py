#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : MAY 2025
# Given the initial and final velocity, as well as the change in time, calculate its acceleration


# Function that is used to calculate for acceleration using formula
def physics_calc(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time


def main():

    # Greeting line
    print(
        "Top of the morning lad, this drunken calculator calculates how fast that object is going, the acceleration to be exact.\n",
        "Just give me the initial and final velocity, aswell as how long it took (the time ya moron). ",
    )

    # Lives/ chances you have for wrong guesses
    # if lives -= 1 (removes 1 from lives until its  to 0)
    lives = 3

    while True:

        # Asks for initial velocity
        print("")
        initial_velocity_str = input("What is ya initial velocity lad? ")

        try:

            # Converts initial_velocity into a float
            initial_velocity = float(initial_velocity_str)

            while True:

                # Asks for final velocity
                print("")
                final_velocity_str = input("Now for your final_velocity: ")

                try:

                    # Converts input into float
                    final_velocity = float(final_velocity_str)

                    while True:

                        # Asks for time
                        print("")
                        time_str = input(
                            "Alright mate how give me the time it took from point a to point b in seconds: "
                        )

                        # Checks if time is less or = to 0
                        if time_str <= "0":
                            print(
                                "You cant divide by zero lad, are you drunk or something"
                            )
                            lives -= 1

                            print(
                                f"Ok listen here ill let you try again but you only have {lives} chance(s)"
                            )

                            if lives <= 0:
                                print("")
                                print(
                                    f"I might be drunk, BUT YOU'RE DRUNKER GET OUTTTTTT!!!!!"
                                )
                                break

                        else:

                            # Converts to float
                            try:
                                time = float(time_str)

                                # Calls the function and assigns returned value to variable
                                aceleration = physics_calc(
                                    initial_velocity, final_velocity, time
                                )

                                # Final output
                                print(
                                    f" Using the formula ({final_velocity} - {initial_velocity}) / {time} the answer = {aceleration} m/s²"
                                )

                                break

                            except ValueError:
                                print("")
                                print(f"{final_velocity_str} is an invalid number lad")
                                lives -= 1

                                print(
                                    f"Ok listen here ill let you try again but you only have {lives} chance(s)"
                                )

                                if lives <= 0:
                                    print("")
                                    print(
                                        f"I might be drunk, BUT YOU'RE DRUNKER GET OUTTTTTT!!!!!"
                                    )
                                    break

                    break

                except ValueError:
                    print("")
                    print(f"{final_velocity_str} is an invalid number lad")
                    lives -= 1

                    print(
                        f"Ok listen here ill let you try again but you only have {lives} chance(s)"
                    )

                    if lives <= 0:
                        print("")
                        print(f"I might be drunk, BUT YOU'RE DRUNKER GET OUTTTTTT!!!!!")
                        break

            break
        except ValueError:
            print(f"{initial_velocity_str} is an invalid number lad")
            lives -= 1

            print(
                f"Ok listen here ill let you try again but you only have {lives} chance(s)"
            )

            if lives <= 0:
                print("")
                print(f"I might be drunk, BUT YOU'RE DRUNKER GET OUTTTTTT!!!!!")
                break


if __name__ == "__main__":
    main()
    hi = "I hate this class"
