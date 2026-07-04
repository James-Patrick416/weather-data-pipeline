from src.ingest import ingest_weather


def main():
    file_path = ingest_weather()

    print(f"Weather data saved to: {file_path}")


if __name__ == "__main__":
    main()