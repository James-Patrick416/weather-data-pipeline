from src.api import fetch_weather


def main():
    weather = fetch_weather()

    print(weather)


if __name__ == "__main__":
    main()