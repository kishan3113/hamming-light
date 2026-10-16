# Validation and proposed hardware tests

## Completed mathematical reference checks

Run from the repository root:

```bash
python3 reference/hamming74.py --self-test
```

The accompanying reference model checks all 16 possible four-bit data words without errors and all seven possible single-bit flips for each word: **16 clean cases + 112 error cases = 128 checks**. It verifies the recovered data, corrected codeword and syndrome location. It also checks one double-bit example that demonstrates miscorrection.

These are newly performed software checks of the documented model. They are not measurements of the photographed hardware.

## Current hardware evidence

| Item | Record |
| --- | --- |
| Physical breadboard assemblies | Visible in supplied photos |
| Illuminated displays and indicators | Visible in supplied photos |
| Transmission over a measured distance | Not recorded |
| Single-bit correction trials | Reported as a feature; no input/output log supplied |
| Data rate and timing | Not recorded |
| Bit-error rate (BER) | Not recorded |
| Ambient-light tolerance | Not recorded |
| Power consumption | Not recorded |

## Proposed test procedure

1. Identify all IC markings, optical devices and supply requirements. Trace supply rails and confirm any open-collector pull-ups.
2. Verify each optical sensing path with fixed light ON and OFF; record the analog level and recovered digital state. Keep input words stable during settling.
3. Confirm the actual Hamming bit ordering and parity convention before applying these reference vectors.
4. Test each valid input word without introduced errors. Compare intended data, received codeword, syndrome and recovered output.
5. Introduce one controlled inversion at the digital receiver input, one bit at a time. Confirm the syndrome and recovered word. Blocking a beam is not always a bit flip and may affect several paths.
6. Introduce two controlled inversions to demonstrate the limit of ordinary Hamming correction.
7. Increase separation and vary room lighting while logging the same test word. Measure speed separately with a defined update/sample interval.

If the confirmed circuit is Hamming(7,4), the complete codeword test set contains 128 clean/single-error cases. A BCD-only display path may accept only the ten decimal inputs; inspect binary nodes or LEDs when testing all 16 words.

## Suggested log format

| Input | Sent codeword | Received codeword | Introduced flip | Syndrome | Recovered data | Distance / light | Pass? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| To measure | To measure | To measure | To measure | To measure | To measure | To measure | To measure |

BER is incorrectly received bits divided by total transmitted bits at a specified observation point. Log raw channel BER separately from residual errors after correction. Report range only with a stated lighting condition and an explicit acceptance criterion.

## Reference example

With positions 1-7 written left to right, input `1001` encodes to `0011001`. Flip position 5 to obtain `0011101`: syndrome `101` identifies position 5, correction restores `0011001`, and data extraction returns `1001`.
