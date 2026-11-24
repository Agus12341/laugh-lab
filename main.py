import os

TEXT = "I told my plants I'd water them tomorrow. That was in March. They've started a support group."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check against the gate: 1-200 code points, not only whitespace,
    # and the bytes on disk are exactly TEXT encoded as UTF-8.
    assert 1 <= len(TEXT) <= 200, "entry must be 1 to 200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
