import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from utils import generate_sklearn_loader_snippet

def get_model():
    """
    Reconstruct and return a scikit-learn model from an embedded, base64-encoded compressed blob.

    Security note:
      This uses pickle-compatible loading. Only use if you trust the source.
    """
    import base64
    import pickle as _p
    import zlib as _z; _decomp = _z.decompress
    _blob_b64 = "eNptlHlQU1cUhwlL2Cu44IgZFkWJVNKCFu1Ye6uoOKQibtQFeIa8l/D0kcS8F5Ctgo6y+CBaLksooGyKBCotRUGLp6XVqkXtuAG2dWHKoEUcrVTRgaGvkeo/npl77zkz53z3d+/MORl2hSY7K4vxXux2hlLoNTKG1ggnkaAlKUZGMFo1zXK0EvMTPx1311JqPcWytFaDC/CcTJyOpby9jtIoGC4Z89ZMMOZtSYOCwTm8DadlcBjyDOkdkIQG8qJQIXg8fqGriuYIWsNReiWl43A27/46IFilQpChxnIR76JkFCxLJFG0Op7DEbyLXqEhtQkEyyk4SojFrJZJpPSYt2PiVGoW8w4Jip0ELZDwqvs2vHOCgeFowgLBvBNJ6fSUUqgkMW8vlMVpWQrLrXinJIXewtRzgmyxhtimjWMFugMTROgVHK0V/Hc0hIpScAbh8YJuAstJ3sHCFWLMT9IYEnTJMkKp1VMywaf0/32aM6HSaxPiDCqVoKcAS4vcrN5mj5Gg3wIQTpJL1lFCMm+tWohzsrPwWiyV2/Cij3BERET4mGCWTW7F4Ti59V4c78gJKby9xvJqAsdPlxbZjoNlwsLx3rw1Pf8NKn7mW0Ci1yA7pZZSvcL42LzCeHT+euKz0jQ0MePwo4zAWng270Kj7xYTPHS0WpaPiuGq1DjyIKwVGaXdFyIfFaIOOtp0NTUPeZV0/7RadxxS1zcUHNpTiQq3Ji5wa8mGgY7PB3ZGlYFrZ25Y6qkiMKWGsj8bc+Di1IobPWd1KMmvIdXHkYWXJf5tFd5V6LLkTMq18nZUuUV16UO7bNhtvN+0bHspTE6PGP2LrAbJpcrNQ93VEOLjmxkARWhK10tmsa4c/hYXS67clcOqAjEq7m2CQuv6EttpR5DP8UWx7xtNaPLV2hUT1hyASR1zSvPlx2Cy2PXRkzglCqv/vW/piTLYmODp8XI0D0Y9jE87cr4B59C6hfm9hXDyQWbAySdlsLyxUOqMq8B9Zklu54Z4KGMiNwQkm1ArrDoYu+YIajOays3bvoDM9m319ZE0OrrgXHD2Uwr900mbK2KLYUIW0d67vA5tHhEPVsvyIaqNKVtkU4wWL3wwtdkmCynW2rsnRtagA15Xru2+WQ79W01TgkoqYXTX3T8/9j6AJjVHpE8T1aIjq1/kxkzdB/ZjtzLIgGK47nj7efNZ4X5yvfOzmhSY1W/kpPO/Bt7Lnzz/QwY0DX11L6bOjCI2q1F6EYsGw7M2+bkUQ/qSuS86Burg2Ln99aLtdbAiresDs0czKvOv8lR91wCPc2fFXIw0o33dS9IqYhvg++g5v1X0F8Dw0HlJ+ITdMFfu6XsotRRlip+GjYVXooOzUcr8gXzYb7wTTerMaMzfuj1sei1Eu5gHL42YwWlTzCJndzMil7X04+vVCJHJutD8PNQ6g2GfNYaAKPp5UtTlUlAP+ycRwycA3XY/JQk+CveMObpNQzVQc2PY793BOqCraeV5tgVpvjQ8bztdhX7Ze9rPbFUAeQeNLl1We2FWblDLrZsE8vTVBPa4NaKVS22d8vfUoffWyXbU5B4C2Y6Uvmt3G1GX260Mc9+3aIlz5I+JbAOS6Htcm46FwOyjrbO9d+2HJ5+0biR8a1HaRj+v6qgKGL3zR+A86+MIx8+Qi+Tkvv9byOnNKLP0kcN4O64/vK5vpOfhGUv+64ZzI8ZnLyFMJMtc5e2CZAtkwdgQJ/sXbo6FLQ=="
    _raw = _decomp(base64.b64decode(_blob_b64))
    model = _p.loads(_raw)
    return model


def training_model():
    CIPHERTEXT_PATH = "data/cipher_objective.csv"
    CIPHER_TEXT_PAIRS =  pd.read_csv(CIPHERTEXT_PATH).values.tolist()


    n = len(CIPHER_TEXT_PAIRS)
    d = len(CIPHER_TEXT_PAIRS[0][0])

    X = np.zeros((n, d))
    y = np.zeros(n)

    print("n:",n)
    print("d",d)

    class_to_int = {"default":0, "exit":1}


    print(len(CIPHER_TEXT_PAIRS[0][0]))
    for training_data_number, cipher_text_pair in enumerate(CIPHER_TEXT_PAIRS):
        cipher_text = cipher_text_pair[0]
        for letter_num, c in enumerate(cipher_text):
            # print(c)
            # print(i)
            X[training_data_number,letter_num] = ord(c)
        y[training_data_number] = class_to_int[cipher_text_pair[1]]

    train_num = 2000
    test_num = n/2-train_num
    print("traning data", train_num*2)
    print("testing data", test_num*2)


    X_train = X[2000-train_num:2000+train_num, :]
    y_train = y[2000-train_num:2000+train_num]

    

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    
    print("inaccuracy on training data:", 1-model.score(X,y))

    if train_num != n/2:
        X_test_0 = X[:2000-train_num, :]
        X_test_1 = X[2000+train_num:, :]
        y_pred_0 = model.predict(X_test_0)
        y_pred_1 = model.predict(X_test_1)

        false_1 = np.count_nonzero(y_pred_0 == 1)
        false_0 = np.count_nonzero(y_pred_1 == 0)

        wrong_count = false_1 + false_0

        print("inaccuracy on external data:", (wrong_count)/(test_num*2) )

    sk_snippet = generate_sklearn_loader_snippet(model, compression='zlib')
    print(sk_snippet)

    model = get_model()
    print("inaccuracy on training data after reconstruction:", 1-model.score(X,y))

    

training_model()



def test_model():
    model = get_model()
    CIPHERTEXT_PATH = "data/cipher_objective.csv"
    CIPHER_TEXT_PAIRS =  pd.read_csv(CIPHERTEXT_PATH).values.tolist()

    test_message = CIPHER_TEXT_PAIRS[0][0]
    print(test_message)
    
    X = np.zeros((1,100))

    for i in range(100):
        X[0,i] = ord(test_message[i])

    result = model.predict(X)
    print(result)

# test_model()