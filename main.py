from handDetector import handDetector


if __name__ == "__main__":
    try:
        detector = handDetector()
        detector.main()
    except Exception as e:
        print(e)