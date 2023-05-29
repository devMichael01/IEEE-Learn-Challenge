def main():
	Time =  convert(input("What is the time ? "))
	if Time >= 7.0 and Time <= 8.0:
            print("Breakfast time") 
	elif Time >= 12.0 and Time <= 13.0:
            print("Lunch time")
	elif Time >= 18.0 and Time <= 19.0:
            print("Dinner time")


def convert(T):
    hours, minutes = T.split(":")
    minutes = float(minutes)/60
    total_time = float(hours) + minutes
    return  (total_time)


if __name__ == "__main__":
    main()
