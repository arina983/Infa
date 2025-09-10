import numpy as np

def generate_bits(num_bits):
    return np.random.randint(0, 2, num_bits)

def bpsk_modulate(bits):
    return np.where(bits == 0, 1, -1)

def bpsk_demodulate(simbol):
    return np.where(np.real(simbol) >= 0, 0, 1)

def generate_channel_gain():
    real = np.random.normal(0, 1 / np.sqrt(2), (2, 2))
    imag = np.random.normal(0, 1 / np.sqrt(2), (2, 2))
    h = real + 1j * imag
    return h

def calculate_ber(orig_bits, received_bits):
    errors_bits = np.sum(orig_bits != received_bits)
    return errors_bits / len(orig_bits)

def mimo_channel(symbols, H, snr_db):
    snr_linear = 10 ** (snr_db / 10)
    noise_variance = 1 / snr_linear
    n = (np.random.normal(0, np.sqrt(noise_variance/2), (2, 100)) +
             1j * np.random.normal(0, np.sqrt(noise_variance/2), (2, 100)))
    return H @ symbols + n


def zf_demodulate(Y, H):
    H_inv = np.linalg.inv(H)
    return H_inv @ Y

def theoretical_ber(snr_db):
    snr_linear = 10 ** (snr_db / 10)
    return 0.5 * (1 - np.sqrt(snr_linear / (1 + snr_linear)))

def main():
    num_bits = 100
    num_trials = 1000
    snr_db_list = [0, 2, 4, 6, 8, 10]

    ber_results = []

    for snr_db in snr_db_list:
        ber_mimo_sum = 0

        for _ in range(num_trials):
            bits1 = generate_bits(num_bits)
            bits2 = generate_bits(num_bits)

            symbols1 = bpsk_modulate(bits1)
            symbols2 = bpsk_modulate(bits2)
            symbols = np.array([symbols1, symbols2])

            H = generate_channel_gain()
            Y = mimo_channel(symbols, H, snr_db)

            X_hat = zf_demodulate(Y, H)

            bits1_hat = bpsk_demodulate(X_hat[0])
            bits2_hat = bpsk_demodulate(X_hat[1])

            ber1 = calculate_ber(bits1, bits1_hat)
            ber2 = calculate_ber(bits2, bits2_hat)
            ber_mimo_sum += (ber1 + ber2) / 2

        ber_mimo = ber_mimo_sum / num_trials
        ber_results.append(ber_mimo)

    print("SNR (дБ) | Экспериментальный BER | Теоретический BER")
    print("----------------------------------------------------")
    for i, snr_db in enumerate(snr_db_list):
        print(f" | {snr_db:8} | {ber_results[i]:18.6f} | {theoretical_ber(snr_db):15.6f} |")
        print("----------------------------------------------------")

if __name__ == "__main__":
    main()