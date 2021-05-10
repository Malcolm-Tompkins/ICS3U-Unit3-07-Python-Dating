#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 10, 2021
# Determines if a person fits grandma's dating criteria

import constants


def main():
    # User input
    user_input = (input("Enter your age: "))

    # Process
    try:
        user_age = int(user_input)

        if (user_age >= constants.youngest_age
                and user_age <= constants.oldest_age):
            print("You can date my grandchild")
        elif (user_age < constants.youngest_age):
            print("You are not old enough to date my grandchild!")
        else:
            print("You cannot date my grandchild get younger!")
    except Exception:
        print("{} is not an age".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
