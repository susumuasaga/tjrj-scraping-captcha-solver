def mixed_decoder(error: UnicodeError) -> (str, int):
    bs: bytes = error.object[error.start: error.end]
    return bs.decode("cp1252"), error.start + 1
