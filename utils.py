import datetime

def is_mod10_valid(number):
        """
        Returns whether or not the card's number validates against the mod10
        algorithm (Luhn algorithm), automatically returning False on an empty
        value.
        """
        # Check for empty string
        if not number:
            return False

        # Run mod10 on the number
        dub, tot = 0, 0
        for i in range(len(number) - 1, -1, -1):
            for c in str((dub + 1) * int(number[i])):
                tot += int(c)
            dub = (dub + 1) % 2

        return (tot % 10) == 0

def is_expired(self):
        """
        Returns whether or not the expiration date has passed in American Samoa
        (the last timezone).
        """

        self.expired_after = datetime.datetime(
            year,
            month,
            day_count,
            23,
            59,
            59,
            999999
        )
        
        # Get the current datetime in UTC
        utcnow = datetime.datetime.utcnow()

        # Get the datetime minus 11 hours (Samoa is UTC-11)
        samoa_now = utcnow - datetime.timedelta(hours=11)

        # Return whether the exipred after time has passed in American Samoa
        return samoa_now > self.expired_after
