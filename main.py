
import datetime


def main():

    now = datetime.datetime.now()
    date = (now.strftime("%Y%m%d-%H%M"))

    frequencies = ["536125", "577875"]

    with open(f"{date}_frequencies.csv", 'w') as file:  # tälle joku hyvä tallennussijainti
        file.write("name;type;frequency;tolerance;minfrequency;maxfrequency;priority;squelchlevel\n")
        i = 1
        for frequency in frequencies:
            file.write(f"Frequency {str(i).zfill(3)};2;{frequency};0;{frequency};{frequency};2;5\n")
            i += 1


if __name__ == "__main__":
    main()
